from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=30, null=True)
    mail = models.EmailField(max_length=100)
    msg_subject = models.CharField(max_length=30)
    msg_content = models.TextField(blank=True)
    
    def __str__(self):
        return self.full_name
