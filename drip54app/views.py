import datetime
import random
from django.db.utils import IntegrityError
import string
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Address, CheckoutItem, Clothtype, OrderItem, Product, Cart_item, Brand, Userprofile, Checkout, Order
from .models import Wishlist as mywishlist
from django.contrib.auth.decorators import login_required
from .forms import AddressForm, Cartitemform, WishlistForm, UserprofileFormA, UserprofileFormB, CheckoutItemForm, OrderItemForm


# Create your views here.

class Authentication:
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                context = {
                    'form1' : UserprofileFormA(),
                    'form2' : AddressForm(),
                    'alert' : 'User verification form!',
                }
                return render(request, 'drip54app/signup.html', context)

        else:
            form = UserCreationForm()
            
        return render(request, 'drip54app/signup.html', {'form' : form})
    
    def userprofileverification(request):
        if request.method =='POST':
            address_form = AddressForm()
            address_form = address_form.save(commit=False)
            address_form.county = request.POST['county']
            address_form.townorcity = request.POST['townorcity']
            address_form.owner = request.user
            address_form.save()
            form = UserprofileFormB(request.POST or None)
            firstname = request.POST['firstname']
            middlename = request.POST['middlename']
            lastname = request.POST['lastname']
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.firstname = firstname
            userprofile.middlename = middlename
            userprofile.lastname = lastname
            userprofile.address = Address.objects.get(owner = request.user)
            userprofile.save()
            return redirect('home')
        
    def profilesettings(request):
        userprofile = Userprofile.objects.get(user = request.user)
        wishlistproducts = mywishlist.objects.filter(added_by = request.user)[:3]
        cartproducts = Cart_item.objects.filter(added_by = request.user)[:3]
        address = Address.objects.get(owner = request.user)
        context = {
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : userprofile,
            'wishlistproducts' : wishlistproducts,
            'cartproducts' : cartproducts,
            'address' : address,
        }
        return render(request, 'drip54app/profile.html', context)

@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    context = {
        'products' : products,
        'brands' : brandmodel(),
        'clothetypes' : clothetypes(),
        'userprofile' : usermodel(request),
    }
    return render(request, 'drip54app/index.html', context)    

def brandmodel():
    brands = Brand.objects.all()
    return brands

def clothetypes():
    clothetypes = Clothtype.objects.all()
    return clothetypes

def usermodel(request):
    userprofile = Userprofile.objects.get(user = request.user)
    return userprofile
    

def product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product' : product,
        'brands' : brandmodel(),
        'clothetypes' : clothetypes(),
        'userprofile' : usermodel(request),
    }
    return render(request, 'drip54app/product.html', context)

def checkoutinfodelete(request):
    checkoutitems = CheckoutItem.objects.filter(belongs_to = request.user)
    checkoutitems.delete()
    checkout = Checkout.objects.filter(added_by = request.user)
    checkout.delete()
    
class Cart:
    @login_required(login_url='login')
    def cart(request):
        checkoutinfodelete(request)
        products = Cart_item.objects.filter(added_by = request.user)
        context = {
            'products' : products,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
            
        }
        return render(request, 'drip54app/cart.html', context)

    def addtocart(request, id):
        checkoutinfodelete(request)
        form = Cartitemform()
        cartitem = form.save(commit=False)
        cartitem.item = get_object_or_404(Product, pk=id)
        cartitem.added_by = request.user
        for itemincart in Cart_item.objects.filter(added_by = request.user):
            if itemincart.item == cartitem.item:
                products = Cart_item.objects.filter(added_by = request.user)
                context = {
                    'message' : 'The item is already added to your cart.',
                    'messagetype' : 'danger',
                    'products' : products,
                    'brands' : brandmodel(),
                    'clothetypes' : clothetypes(),
                    'userprofile' : usermodel(request),
                    
                }
                return render(request, 'drip54app/cart.html', context)
        cartitem.save() 
        products = Cart_item.objects.filter(added_by = request.user)
        context = {
            'message' : 'The item has been added to your cart.',
            'messagetype' : 'success',
            'products' : products,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
            
        }
        return render(request, 'drip54app/cart.html', context)
        
    def deletecartitem(request, id):
        item = get_object_or_404(Cart_item, pk=id)
        item.delete()
        return redirect('cart')
    
class Wishlist:
    def wishlist(request):
        products = mywishlist.objects.filter(added_by = request.user)
        context = {
            'products' : products,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
        }
        return render(request, 'drip54app/wishlist.html', context)
    
    def addtowishlist(request, id):
        form = WishlistForm()
        wishlistitem = form.save(commit=False)
        wishlistitem.item = get_object_or_404(Product, pk=id)
        wishlistitem.added_by = request.user
        for cartitem in mywishlist.objects.filter(added_by = request.user):
            if cartitem.item == wishlistitem.item:
                products = mywishlist.objects.filter(added_by = request.user)
                context = {
                'message' : "The item is already added to your wishlist.",
                'messagetype' : 'danger',
                'products' : products,
                'brands' : brandmodel(),
                'clothetypes' : clothetypes(),
                'userprofile' : usermodel(request),
                }
                return render(request, 'drip54app/wishlist.html', context)
        wishlistitem.save()
        products = mywishlist.objects.filter(added_by = request.user)
        context = {
        'message' : "Item has been added to your wishlist.",
        'messagetype' : 'success',
        'products' : products,
        'brands' : brandmodel(),
        'clothetypes' : clothetypes(),
        'userprofile' : usermodel(request),
        }
        return render(request, 'drip54app/wishlist.html', context)

    
    def deletewishlistitem(request, id):
        products = mywishlist.objects.filter(added_by = request.user)
        item = get_object_or_404(mywishlist, pk=id)
        item.delete()
        return redirect('wishlist')

    
class BrandViews:
    def brand(request, id):
        brand = get_object_or_404(Brand, pk=id)
        products = Product.objects.filter(product_brand = id)
        context = {
            'brand' : brand,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'products' : products,
            'userprofile' : usermodel(request),
        }
        return render(request, 'drip54app/brand.html', context)       
    
class ClotheTypes:
    def clothetype(request, id):
        clothetypeobj = get_object_or_404(Clothtype, pk=id)
        products = Product.objects.filter(product_type = id)
        context = {
            'clothetype' : clothetypeobj,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'products' : products,
            'userprofile' : usermodel(request),
        }
        return render(request, 'drip54app/type.html', context)
    
def productsearch(request):
    if request.method == "POST":
        query = request.POST['query']
        products = Product.objects.filter(product_name__contains = query)
        context = {
            'query' : query,
            'products' : products,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
        }
        return render(request, 'drip54app/query.html', context)
    
def checkout(request):
    itemsincart = Cart_item.objects.filter(added_by = request.user)
    cartcheck = itemsincart.exists()
    if cartcheck is True:
        checkout = Checkout.objects.filter(added_by = request.user)
        checkout = checkout.exists()
        if checkout is False:
            for item in itemsincart:
                form = CheckoutItemForm()
                checkoutitem = form.save(commit=False)
                itemtosave = item.item
                checkoutitem.belongs_to = request.user
                checkoutitem.item = itemtosave
                checkoutitem.save()
            checkoutitems = CheckoutItem.objects.filter(belongs_to = request.user)
            checkout = Checkout.objects.create(
                added_by = request.user
            )
            for checkoutitem in checkoutitems:
                checkout.items.add(checkoutitem)
            context = {
                'brands' : brandmodel(),
                'clothetypes' : clothetypes(),
                'userprofile' : usermodel(request),
                'checkout' : checkoutitems,
                }
            return render(request, 'drip54app/checkout.html', context)
        else:
            checkout = CheckoutItem.objects.filter(belongs_to = request.user)
            context = {
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
            'checkout' : checkout,
            }
            return render(request, 'drip54app/checkout.html', context)
        
    else:
        products = Cart_item.objects.filter(added_by = request.user)
        context = {
            'products' : products,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
            'message' : 'Add items to your cart first.',
            'messagetype' : 'danger',    
        }
        return render(request, 'drip54app/cart.html', context)
    
def create_random_number():
    return ''.join(random.choices(string.digits, k=10))

class Orders:
    def order(request):
        checkout = CheckoutItem.objects.filter(belongs_to = request.user)
        for item in checkout:
            form = OrderItemForm()
            itemtosave = form.save(commit=False)
            itemtosave.belongs_to =  request.user
            itemtosave.orderitem_id = create_random_number()
            itemtosave.order_item = item.item
            itemtosave.ordered = False
            try:
                itemtosave.save()
            except IntegrityError as e:
                itemtosave.orderitem_id = create_random_number()
                itemtosave()
            
        order_items = OrderItem.objects.filter(belongs_to = request.user, ordered=False)
        datecreated = timezone.now()
        address = Address.objects.get(owner = request.user)
        try:
            order = Order.objects.create(
                order_number = create_random_number(),
                date_created = datecreated,
                belongs_to = request.user,
                address = address,
                waiting_confirmation = True, 
            )
        except IntegrityError as e:
            order = Order.objects.create(
                order_number = create_random_number(),
                date_created = datecreated,
                belongs_to = request.user,
                address = address,
                waiting_confirmation = True, 
            )
        for orderitem in order_items:
            orderitem.ordered = True
            orderitem.order = order
            orderitem.save()
        cartitems = Cart_item.objects.filter(added_by = request.user)
        cartitems.delete()
        return redirect('orders')
    
    def orders(request):
        orders = Order.objects.filter(belongs_to = request.user)
        context = {
            'orders' : orders,
            'brands' : brandmodel(),
            'clothetypes' : clothetypes(),
            'userprofile' : usermodel(request),
        }
    
        return render(request, 'drip54app/orders.html', context)
    
def order(request, order_number):
    order = Order.objects.get(order_number = order_number)
    products = OrderItem.objects.filter(order = order)
    context = {
        'order' : order,
        'products' : products,
        'userprofile' : usermodel(request),
        'brands' : brandmodel(),
        'clothetypes' : clothetypes(),
    }
    return render(request, 'drip54app/order.html', context)
    

class Administration:
    def todaystotals():
        total = 0
        orders = Order.objects.filter(date_created__date =datetime.date.today())
        for order in orders:
            total = order.total_amount() + total
        return total

    def monthstotals(): 
        total = 0
        today = datetime.datetime.now()
        orders = Order.objects.filter(date_created__year = today.year, date_created__month = today.month)
        for order in orders:
            total = order.total_amount() + total
        
        return total

    def totalorders():
        orders = Order.objects.all()
        return orders.count()

    def registeredusers():
        users = User.objects.all()
        return users.count()

    def dashboard(request):
        recentorders = Order.objects.all()[:10]
        return render(request, 'administration/dashboard.html', {
            'recentorders' : recentorders,
            'todayssales' : Administration.todaystotals,
            'monthsales' : Administration.monthstotals,
            'totalorders' : Administration.totalorders,
            'registeredusers' : Administration.registeredusers,
        })

    