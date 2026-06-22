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
def shop (request):
   return render(request, 'shop.html')
def contact(request):
   return render(request, 'contact.html')
def cheackout(request):
   return render(request, 'cheackout.html')
def bestsellers(request):
   return render(request, 'bestsellers.html')
def single(request):
   return render(request, 'single.html')
def cart(request):
   return render(request, 'cart.html')
def error(request):
   return render(request, 'error.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Mandamos directo a la ruta base de la otra app
            return redirect('/dashboard2/') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')