from ast import Add
from django.contrib import admin

from drip54app.models import Brand, Cart_item, CheckoutItem, Checkout, Order, OrderItem, Product, Userprofile, Wishlist, Clothtype, Address

# Register your models here.

admin.site.register(Product)
admin.site.register(Cart_item)
admin.site.register(Brand)
admin.site.register(Userprofile)
admin.site.register(Wishlist)
admin.site.register(Clothtype)
admin.site.register(Address)
admin.site.register(CheckoutItem)
admin.site.register(Checkout)
admin.site.register(Order)
admin.site.register(OrderItem)
