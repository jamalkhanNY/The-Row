from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('products/index', views.index),
    path('new_products', views.new_products),
    path('members', views.members),
    path('exclusive', views.exclusive),
    path('home', views.home),
    path('loginPage', views.loginPage),
    path('logout', views.logoutUser),
    path('register', views.register),
    path('cart', views.cart, name = "cart"),
    path('checkout',views.checkout, name = "checkout")
    
]