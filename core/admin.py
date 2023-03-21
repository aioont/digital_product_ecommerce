from django.contrib import admin

# Register your models here.
from .models import Contact, AdminMessage
# Register your models here.
admin.site.register(Contact)
admin.site.register(AdminMessage)