from django.shortcuts import render, redirect
from django.contrib import messages

from .registeration import register_user

def register(request):
    if request.method == 'POST':
        register_status = register_user(request)
        if register_status != 1:
            messages.error(request, register_status)
            return redirect('register')
        else:
            messages.success(request, 'You are now registered and can login')
            return redirect('login')
    else:
        return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'users/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'users/dashboard.html')