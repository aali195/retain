from django.shortcuts import render, redirect
from django.contrib import messages

from .registeration import register_user
from .login import login_user
from .logout import logout_user
from .dashboard import user_details

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
        login_status = login_user(request)
        if login_status != 1:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        else:
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
    else:
        return render(request, 'users/login.html')

def logout(request):
    logout_user(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
    context = user_details(request)
    return render(request, 'users/dashboard.html', context)