from django.urls import path
from django.contrib.auth import views as auth_views

from . import views 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('login/forgot/', views.forgot, name='forgot'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('my-store/', views.my_store, name='my_store'),
    path('my-store/order-detail/<int:pk>/', views.my_store_order_detail, name='my_store_order_detail'),
    path('my-store/add-product/', views.add_product, name='add_product'),
    path('my-store/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my-store/delete-product/<int:pk>/', views.delete_product, name='delete_product'), #working
    path('vendors/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),
]