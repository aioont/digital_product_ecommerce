import json
import stripe
import uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from core.models import Contact
# from services.models import ProviderMessage
from store.models import VendorMessage


# Create your views here.
from .cart import Cart
from .forms import OrderForm, MessageSellerForm
from .models import Product, Category, Order, OrderItem, Vendor
from core.forms import ContactForm


from django.shortcuts import render, redirect
from .models import OrderItem


def payment_management(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order_item = OrderItem.objects.get(id=order_id)
        order_item.is_admin_paid_to_vendor = request.POST.get('is_admin_paid_to_vendor') == 'True'
        order_item.save()
        return redirect('payment_management')
    else:
        orders = OrderItem.objects.all()
        return render(request, 'payment_management.html', {'orders': orders})



def view_messages_vendor(request):
    vendor_msg = VendorMessage.objects.all()
    return render(request, 'view_messages_vendor.html',{
        'vendor_msg': vendor_msg,
    })


def success(request, product_id):
    product = Product.objects.filter(id=product_id)
    return render(request, 'success.html', {
        product_id: 'product_id'
    })

def add_to_cart(request, product_id):
    cart = Cart(request)
    print(product_id)
    cart.add(product_id)

    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart_view.html', {
        'cart': cart,
    })

@login_required
def checkout(request):
    cart = Cart(request)

    # Check if the cart is empty
    if cart.get_total_cost() == 0:
        return redirect('cart_view')

    # Process the order
    if request.method == 'POST':
        # Parse the form data from the request body
        data = json.loads(request.body)
        full_name = data['full_name']
        email = data['email']
        mobile = data['mobile']
        address = data['address']

        # Validate the form data
        if full_name and email and mobile and address:
            form = OrderForm(request.POST)
            
            total_price = 0
            # Create the line items for the Stripe checkout session
            items = []
            for product_id, item_data in cart.cart.items():
                item = cart.get_item(product_id)  # Use the get_item() method to get the product info
                if item:

                    product = item['product']
                    total_price += product.discount_price * int(item['quantity']) * 100
                    items.append({
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': product.title,
                            },
                            'unit_amount': total_price,
                        },
                        'quantity': item['quantity']
                    })

            # Create the Stripe checkout session
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=items,
                mode='payment',
                success_url=f'{settings.WEBSITE_URL}{product_id}/cart/checkout/success',
                cancel_url=f'{settings.WEBSITE_URL}/cart/',
            )
            payment_intent = session.payment_intent 

            # Create the order and order items
            order = Order.objects.create(
                full_name=full_name,
                email=email,
                mobile=mobile,
                address=address,
                paid_amount=total_price / 100,
                is_paid=True,
                order_id=uuid.uuid4(),
                payment_intent=payment_intent,
                created_by=request.user,
            )
            #product_id = item['product_id']
            print(product_id)
            for product_id, item_data in cart.cart.items():
                item = cart.get_item(product_id)  # Use the get_item() method to get the product info
                if item:
                    product = item['product']
                    quantity = item['quantity']
                    discount_price = int(product.discount_price * quantity)
                    order_item = OrderItem.objects.create(order=order, product=product, price=discount_price, quantity=quantity)
                    product.quantity -= 1
                    product.save()

            # Clear the cart after the order is complete
            cart.clear()

            # Return the Stripe checkout session and order data as JSON
            return JsonResponse({'session': session, 'order': payment_intent})
        
        # If the form data is invalid, render the checkout page with an error message
        else:
            form = OrderForm()
            return render(request, 'checkout.html', {
                'cart': cart,
                'form': form,
                'error_message': 'Please fill out all fields.',
                'pub_key': settings.STRIPE_PUB_KEY,
            })

    # If the request method is not POST, render the checkout page with the order form and cart data
    else:
        form = OrderForm()
        return render(request, 'checkout.html', {
            'cart': cart,
            'form': form,
            'pub_key': settings.STRIPE_PUB_KEY,
        })

   


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {
        'query': query,
        'products': products,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    vendors = Vendor.objects.filter(status=Product.ACTIVE)[0:6]
    return render(request, 'category_detail.html', { 
        'category': category,
        'products': products,  #refers to related name in models.py of store
        'vendors': vendors,
         })

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    simliar = Product.objects.filter(status=Product.ACTIVE)[0:4]
    
    if request.method == 'POST':
        form = MessageSellerForm(request.POST)
        if form.is_valid():
            # modify subject field by pass the service instance to the form using the instance parameter
            form.instance.msg_subject = "Query about service %s" % product.title
            form.save()
            messages.success(request, "Success")
            form = MessageSellerForm()
        else:
            messages.error(request, "Failed")
    else:
        form = MessageSellerForm()
    

    return render(request, 'product_detail.html', {
        #'category': category,
        'product': product,
        'simliar': simliar,
        'form': form,
    })
