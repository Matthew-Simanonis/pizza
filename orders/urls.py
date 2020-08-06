from django.urls import path
from .views import HomeView, ItemDetailView
from . import views

urlpatterns = [
    path("home", HomeView.as_view(), name="home"),
    path('', views.index, name='home'),
    path('menu', views.menu, name='menu'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('guest-login', views.guest_login, name='guest-login'),
    path('create_user', views.create_user, name='create_user'),
    path('view-cart', views.view_cart, name='view-cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('change-quantity/<slug:slug>', views.change_quantity, name='change-quantity'),
    path('add-to-cart/<slug:slug>', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug:slug>', views.remove_from_cart, name='remove-from-cart')
]
