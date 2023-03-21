from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserAdminCreationForm, BecomeVendorForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .models import *
from django import forms

from store.forms import ProductForm
from store.models import Product, Category, Order, OrderItem, Vendor

from django.utils.text import slugify

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  
            # Get the category from the form data
            category_title = form.cleaned_data['category']
            # Check if a category with the given title already exists
            category, created = Category.objects.get_or_create(title=category_title)
            # Set the category and slug fields for the product
            product.category = category
            product.slug = slugify(product.title)
            product.save()        
            messages.success(request, f'{product.title} added successfully.')
            return redirect('my_store')
        else:
            messages.error(request, f'{product.title} added failed.')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Changes in product {product.title} was saved !')
            return redirect('my_store')

        else:
            messages.error(request, f'Changes in product {product.title} was not saved !')
    else:
        form = ProductForm(instance=product)


    return render(request, 'edit_product.html', {
        'product':product,  
        'form': form 
    })


@login_required
def become_vendor(request):
    if request.method == 'POST':
        form = BecomeVendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()
            
            # set is_vendor to True for the user associated with the vendor instance
            request.user.is_vendor = True
            request.user.save()
            
            vendor_name = vendor.vendor_name
            messages.success(request, f'Added account of {vendor_name} to vendor')
            return redirect('my_store')
        else:
            print(form.errors)
    else:
        form = BecomeVendorForm()
    return render(request, 'become_vendor.html', {'form': form})



# def vendor_detail(request, vendor_name):
#     products = request.user.products.exclude(status=Product.DELETEED)
#     vendor_name = Vendor.objects.all()
#     return render(request, 'vendor_detail.html', {
#         'products': products,
#         'vendor_name': vendor_name,
#     })

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    products = Product.objects.filter(user__vendors=vendor).exclude(status=Product.DELETEED)
    return render(request, 'vendor_detail.html', {
        'products': products,
        'vendor': vendor,
    })


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETEED
    product.save()

    messages.success(request, f'Product {product.title} was deleted !') 
    return redirect('my_store')

@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETEED)
    order_items = OrderItem.objects.filter(product__user=request.user)
    order_items.total = sum(i.order.paid_amount for i in order_items)
    
    return render(request, 'my_store.html', {
        'products': products,
        'order_items': order_items,
        'order_items.total': order_items.total,
    })

@login_required
def my_store_order_detail(request, pk):

    order = get_object_or_404(Order, pk=pk)  # pk matched with pk from url

    return render(request, 'my_store_order_detail.html', {
        'order': order
    })


@login_required
def myaccount(request):
    user = request.user
    orders = Order.objects.filter(created_by=user)

    order_items = []

    for order in orders:
        #print(f"Order ID: {order.id}")
        items = OrderItem.objects.filter(order=order)
        for item in items:
            #print(f"Order item: {item.product.title}")
            order_items.append({
                'product_name': item.product.title,
                'price': item.product.discount_price,
                'paid_amount': order.paid_amount,
                'is_paid': order.is_paid,
            })

    context = {
        'email': user.email,
        'mobile': user.mobile,
        'orders': orders,
        'order_items': order_items,
    }
    return render(request, 'myaccount.html', context)






from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('myaccount')
        else:
            messages.info(request, 'Password or Username is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')



def signup(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')

            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('login')
    return render(request, 'signup.html', {'form': form})

def forgot(request):
    return render(request, 'forgot.html')







