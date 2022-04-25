from django.contrib import admin
from .models import Product, Offer, New, Customer, Orders,Cart, CartItems, ShippingAddress


class OfferAdmin(admin.ModelAdmin):
    list_display = ('coupon_code', 'discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class NewAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'date_created')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'status')


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(ShippingAddress)
admin.site.register(New, ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Orders,OrderAdmin)