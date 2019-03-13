from django.shortcuts import render, redirect

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'users/dashboard.html')