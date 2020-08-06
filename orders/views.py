from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone   
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return render(request, 'orders/index.html')

class HomeView(ListView):
    model = Menu_Item
    template_name = 'orders/index.html'

class ItemDetailView(DetailView):
    model = Menu_Item
    template_name = 'orders/product.html'

def menu(request):
    context = {
        'menu': Menu_Item.objects.all(),
    }
    return render(request, 'orders/menu.html', context)

def view_cart(request):
    try:
        cart = Cart.objects.filter(user=request.user)[0]
        context = {
            'cart' : cart
        }
        return render(request, 'orders/view-cart.html', context)
    except:
        return render(request, 'orders/view-cart.html')

def add_to_cart(request, slug):
    if not request.user.is_authenticated:
        return render(request, 'orders/login.html')
    count = request.POST['count']
    item = get_object_or_404(Menu_Item, slug=slug)
    order_item, created = Order_Item.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False,
    )
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    if order_qs.exists(): 
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity = F('quantity') + count
            order_item.save()
        else:
            order_item.quantity = count
            order_item.save()
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Cart.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect('view-cart')


def remove_from_cart(request, slug):
    item = get_object_or_404(Menu_Item, slug=slug)
    order_qs = Cart.objects.filter(
        user = request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = Order_Item.objects.filter(
                item = item,
                user = request.user,
                ordered = False
                )[0]
            order.items.remove(order_item)
            order_item.delete()
        if len(order.items.filter(user=request.user)) < 1:
            order.delete()
    else:
        message = 'Nothing in Cart'
    return redirect('view-cart')
            
def change_quantity(request, slug):
    change = request.POST['change']
    item = get_object_or_404(Menu_Item, slug=slug)
    order_item = Order_Item.objects.get(
        item = item,
        user = request.user,
        ordered = False,
    )
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    # check if the order item is in the order
    if order.items.filter(item__slug=item.slug).exists():
        order_item.quantity = F('quantity') + change
        if order_item.quantity == 0:
            order_item.delete()
        else:
            order_item.save()
    return redirect('view-cart')

def login_view(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    except: 
        user = None
        pass
    if user is not None:
        login(request, user)
        request.session['logged_in'] = True
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'orders/login.html', {'message': 'Invalid credentials.'})

def logout_view(request):
    logout(request)
    request.session['logged_in'] = False
    return render(request, 'orders/login.html', {'message': 'Logged out.'})

def create_user(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username, email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'), {'message': 'New User Created'})
        except:
            return render(request, 'orders/create_user.html', {'message': 'Username already taken!!!'})
    else:
        return render(request, 'orders/create_user.html')

def guest_login(request):
    password = "LW6Ki8wJbwEzgxm"
    username = "guest"
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse('home'))