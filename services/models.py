from django.db import models

from store.models import Vendor



class Services(models.Model):
    ACTIVE = 'active'
    DELETEED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (DELETEED,  'deleted')
    )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    image = models.ImageField(upload_to='media/uploads/service_image/', blank=True)
    video = models.FileField(upload_to='media/uploads/service_video/', blank=True)
    price = models.IntegerField()
    service_provider = models.ForeignKey('ServiceProvider', related_name='service_provider', on_delete=models.CASCADE)
    stars = models.IntegerField(null=True)
    def __str__(self):
        return self.title
        
class ServiceProvider(models.Model):
    sp_id = models.IntegerField(null=True)
    sp_name = models.CharField(max_length=50)
    sp_image = models.ImageField(upload_to='media/uploads/service_provider_image/', blank=True)
    sp_contact = models.TextField(max_length=200)
    sp_star = models.IntegerField(null=True)

    def __str__(self):
        return self.sp_name


class ProviderMessage(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, default="Querry about service ")
    email = models.EmailField()
    message = models.TextField(max_length=200) 
    # To Do
    
    vendor = models.ForeignKey(Vendor, related_name='messages', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class AdminMessage(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, default="Request to add service ")
    email = models.EmailField()
    message = models.TextField(max_length=200)
    def __str__(self):
        return self.name

