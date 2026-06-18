from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('index', views.hola, name='index'),
    path
]
