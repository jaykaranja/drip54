from django.urls import path
from .views import Authentication, Cart, home, product, Wishlist, BrandViews, Administration, ClotheTypes, productsearch, checkout, Orders, order
from django.contrib.auth import views as authviews

urlpatterns = [
    path('', home, name='home'),
    path('cart', Cart.cart, name='cart'),
    path('product/<int:id>', product, name='product'),
    path('addtocart/<int:id>', Cart.addtocart, name='addtocart'),
    path('deletecartitem/<int:id>', Cart.deletecartitem, name='deletecartitem'),
    path('wishlist', Wishlist.wishlist, name='wishlist'),
    path('addtowishlist/<int:id>', Wishlist.addtowishlist, name='addtowishlist'),
    path('deletefromwishlist/<int:id>', Wishlist.deletewishlistitem, name='deletefromwishlist'),
    path('signup', Authentication.signup, name='signup'),
    path('login', authviews.LoginView.as_view(template_name='drip54app/login.html'), name='login'),
    path('logout', authviews.LogoutView.as_view(), name='logout'),
    path('brand/<int:id>', BrandViews.brand, name='brand'),
    path('type/<int:id>', ClotheTypes.clothetype, name='type'),
    path('query', productsearch, name='query'),
    path('userprofilecreation', Authentication.userprofileverification, name='userprofilecreation'),
    path('profile', Authentication.profilesettings, name='profile'),
    path('checkout', checkout, name='checkout'),
    path('order', Orders.order, name='order'),
    path('orders', Orders.orders, name='orders'),
    path('vieworder/<int:order_number>', order, name='vieworder'),
    path('administration', Administration.dashboard, name='administration'),
]

