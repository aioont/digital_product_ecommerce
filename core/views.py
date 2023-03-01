from django.shortcuts import render, redirect

from store.models import Product, Vendor
from core.models import Contact
from core.forms import ContactForm
from store.models import *
# Create your views here.

from userprofile import views 
from store import views

from django.contrib import messages

def frontPage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]
    category = Category.objects.all()
    vendors = Vendor.objects.filter(status=Product.ACTIVE)[0:6]
    featured_products = Product.objects.filter(status=Product.ACTIVE).order_by('sold')[0:4]
    product_rating = Product.objects.values_list('rating', flat=True)

    return render(request, 'frontPage.html', {'products': products, 'category':category, 'vendors': vendors, 'featured_products': featured_products, 'product_rating': product_rating})

def about(request):
    return render(request, 'about.html')

def allsuccess(request):
    return render(request, 'allsuccess.html')


def contact(request):

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('frontPage')
    return render(request, 'contact.html', {'form': form})

def help(request):
    return render(request, 'help.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def detail(request):
    return render(request, 'product_detail.html')

def checkout(request):
    return render(request, 'checkout.html')


def link(request):
    return render(request, 'link.html')
    



























