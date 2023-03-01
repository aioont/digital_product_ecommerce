"""dpe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core.views import *
from services.views import *
from userprofile.views import *

urlpatterns = [
    path('', frontPage, name='frontPage'),
    path('allsuccess/', allsuccess, name='allsuccess'),
    path('link/', link, name='link'),
    path('admin/', admin.site.urls, name='admin'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('help/', help, name='help'),
    path('shop/', shop, name='shop'),
    path('product-detail/', detail, name='detail'), 
    path('checkout/', checkout, name='checkout'),
    path('',include('services.urls')),
    path('',include('userprofile.urls')),
    path('',include('store.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
