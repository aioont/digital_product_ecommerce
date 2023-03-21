from django.contrib import admin

from .models import Category, Product, Order, OrderItem, Vendor, VendorMessage

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)


admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Vendor)
admin.site.register(VendorMessage)

