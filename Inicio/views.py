from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
def hola(request):
# Create your views here.
   return render(request, 'index.html')
def header(request):
   return render(request, 'header.html')
def footer(request):
   return render(request, 'footer.html')
