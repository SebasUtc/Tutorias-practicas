from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
def hola(request):
# Create your views here.
   return render(request, 'index.html')
def contact(request):
   return render(request, 'header.html')
def courses(request):
   return render(request, 'footer.html')
