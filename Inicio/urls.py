from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.hola, name='home'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('cheackout/', views.cheackout, name='cheackout'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('single/', views.single, name='single'),
    path('cart/', views.cart, name='cart'),
    path('error/', views.error, name='error'),
]
