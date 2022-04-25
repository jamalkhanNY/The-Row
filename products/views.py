from hashlib import new
from multiprocessing import context
from urllib import response
from winreg import REG_WHOLE_HIVE_VOLATILE
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


# call to products call this function  with mapping 
def index (request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new_products(request):
    new = new.objects.all()
    return render(request, 'newProducts.html', {'new': new})


def members(request):
    return render(request, 'exclusive.html')


@login_required(login_url='loginPage')
def exclusive(request):
    return render(request, 'members.html')


def cart(request):
    #cart will return an unbound local error at products/cart for local variable cart being referenced too before assignment 
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     cart, created = cart.objects.filter(customer = customer, completed = False)
    #     cartitems = cart.cartitems_set.all()
    #     # need to use a filter instead of get bc you have more than one instance
    # else:
    cartitems = []
    cart = {"get_cart_total": 0, "get_itemtotal": 0}


    return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})

def checkout(request):
    return render(request, 'checkout.html', {})

def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = cartitem.objects.get_or_create(cart = cart, product = product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    

    return JsonResponse("Cart Updated", safe = False)


def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = cartitem.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)

def home(request):
    return render(request, 'theRow.html')
 

def products (request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def loginPage(request):
    if request.user.is_authenticated:
        return render(request,'members.html')
        
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return render(request,'members.html')
            else: 
                messages.info(request, 'Username OR Password is incorrect')
           


    context={}
    return render(request, 'loginPage.html', context)


def logoutUser(request):
    logout(request)
    return render(request,'loginPage.html')

def register(request):
    if request.user.is_authenticated:
        return render(request, 'loginPage.html')
    else:
        form = UserCreationForm()

        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)
                    return render(request,'loginPage.html',context)
                    



        context = {'form': form}
        return render(request, 'register.html', context)