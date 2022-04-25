import email
from telnetlib import STATUS
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

    


class Product(models.Model):
    name = models.CharField(max_length=255) 
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    
    def __str__(self):
        return self.name 

class Offer(models.Model):
    coupon_code = models.CharField(max_length = 45)
    description = models.CharField(max_length = 150)
    discount = models.FloatField()


class New(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Customer(models.Model):
    user =models.OneToOneField(
    User,
    null=True,
    blank=True,
    on_delete=models.CASCADE,
    related_name="customer"
)
    name = models.CharField(max_length=100, null = True)
    username = models.CharField(max_length= 100, null = True)
    email = models.CharField(max_length = 100, null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return self.name 


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)
    # items = models.ManyToManyField(CartItems)

    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    


    @property
    def get_total(self):
        total = self.quantity * self.product.price
        if total == 0.00:
            self.delete()
        return total

    def __str__(self):
        return self.product.name 


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address 

class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        )
   
    
    
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add= True, null = True)
    status = models.CharField(max_length=200, null = True, choices=STATUS)