from django.contrib import admin
from .models import Services,ServiceProvider #,ProviderMessage

# Register your models here.
admin.site.register(Services)
admin.site.register(ServiceProvider)

# admin.site.register(ProviderMessage)

