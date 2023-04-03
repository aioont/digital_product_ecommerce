#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# from userprofile.models import BecomeVendor


User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='uploads/category/', blank=True, null=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETEED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'waitingapproval'),
        (ACTIVE, 'active'),
        (DELETEED,  'deleted')
    )

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)  #vendor who added product
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    digital_product = models.FileField(upload_to='uploads/digital_product/')
    image = models.ImageField(upload_to='uploads/product_images/', null=True)
    video = models.FileField(upload_to='uploads/videos/', null=True)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True) #video_url = models.URLField()  URLField stores a string representing the URL of the video.  <iframe width="560" height="315" src="{{ product.video_url }}" frameborder="0" allowfullscreen></iframe>
    quantity = models.IntegerField(blank=True, null=True)
    sold = models.IntegerField(blank=True, null=True,default=0)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
    def get_display_price(self):
        return self.price / 100
    


class Vendor(models.Model):
    ACTIVE = 'active'
    DELETEED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (DELETEED,  'deleted')
    )
    user = models.ForeignKey(User, related_name='vendors', on_delete=models.CASCADE, default=True)
    no_of_product = models.IntegerField(null=True)
    income = models.IntegerField(null=True)
    joined_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    vendor_name = models.CharField(null=True, max_length=255)
    vendor_email = models.EmailField(null=True,max_length=100, unique=True)
    vendor_address = models.CharField(null=True,max_length=255)
    vendor_image = models.ImageField(upload_to='uploads/vendor_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.user:
            raise ValueError('A CustomUser instance is required for saving a BecomeVendor instance')
        super(Vendor, self).save(*args, **kwargs)
        self.user.is_vendor = True
        self.user.save()

    
    def __str__(self):
        return self.vendor_name


class Order(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(blank=True)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=255)
    payment_intent = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_display_price(self):
        return self.price / 100
    
    def __str__(self):
        return self.email  # change this to created_b if possible

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)   
    is_admin_paid_to_vendor = models.BooleanField(default=False, null=True)     

    def __str__(self):
        return self.product.title

    # def get_display_price(self):
    #     return self.price / 100
    
class VendorMessage(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, default="Querry about product ")
    email = models.EmailField()
    message = models.TextField(max_length=200)
    def __str__(self):
        return self.name