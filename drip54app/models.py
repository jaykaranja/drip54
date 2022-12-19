from django.db import models
from django.contrib.auth.models import User

# Create your models here.

        
class Address(models.Model):
    county = models.CharField(max_length=50, default="Nairobi")
    townorcity = models.CharField(max_length=50, default="Nairobi City")
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        townorcity = self.townorcity
        return townorcity
    
class Userprofile(models.Model):
    user = models.ForeignKey(User, related_name='userprofile', on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, null=True)
    firstname = models.CharField(max_length=50, null=True)
    middlename = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    phonenumber = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.user.username
    

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, blank=False)
    brand_image = models.FileField(null=True)
    
    def __str__(self):
        return self.brand_name

class Clothtype(models.Model):
    clothtype = models.CharField(max_length=50)
    
    def __str__(self):
        name = self.clothtype
        return name
    
class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=False)
    product_price = models.IntegerField(blank=False)
    product_image = models.FileField()
    product_type = models.ForeignKey(Clothtype, on_delete=models.CASCADE, null=True)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    
    
class Cart_item(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        name = self.added_by.username
        return name
    
class Wishlist(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        name = self.item.product_name
        return name
        
class CheckoutItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=1)
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    
    def __str__(self):
        product_name = self.item.product_name
        user = self.belongs_to.username
        identifier = str(product_name + ' - ' + user)
        return identifier
    
class Checkout(models.Model):
    items = models.ManyToManyField(CheckoutItem, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    
    def __str__(self):
        user = self.added_by
        return user.username
    
    
    
class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)
    waiting_confirmation = models.BooleanField(default=False)
    on_delivery = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        name = self.belongs_to.username
        return name

    def total_amount(self):
        total = 0
        for item in OrderItem.objects.filter(order = self):
            price = item.order_item.product_price
            total = total + price

        return total



class OrderItem(models.Model):
    orderitem_id = models.CharField(max_length=50)
    order_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order', null=True)
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        item_name = self.order_item.product_name
        user = self.belongs_to.username
        identifier = str(item_name + ' - ' + user)
        return identifier
    