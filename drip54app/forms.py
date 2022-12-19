from django import forms
from .models import Address, Cart_item, Order, OrderItem, Userprofile, Wishlist, CheckoutItem, Checkout

class Cartitemform(forms.ModelForm):
    class Meta:
        model = Cart_item
        fields = [
            'item', 'added_by'
        ]
        
class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = [
             'item', 'added_by'
        ]
        
class UserprofileFormA(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            'firstname' , 'lastname', 'middlename', 'phonenumber', 'email'
        ]
        
        
class UserprofileFormB(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            'firstname' , 'lastname', 'middlename', 'phonenumber', 'email'
        ]
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'county', 'townorcity'
        ]
        
class CheckoutItemForm(forms.ModelForm):
    class Meta:
        model = CheckoutItem
        fields = [
             'item'
        ]
        
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = [
             'items'
        ]
        
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = []
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []