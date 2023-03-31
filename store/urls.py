from django.urls import path
from . import views

urlpatterns = [
 
    path('payment-manage-admin/', views.payment_management, name='payment_management'),
    path('my-store/view-messages/',views.view_messages_vendor, name='view_messages_vendor'),
    
    
    path('search/', views.search, name='search'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/checkout/',views.checkout, name='checkout'),
    path('cart/checkout/success/', views.success, name='success'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
]

