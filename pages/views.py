from django.shortcuts import render

from .listings import featured_collecs

def index(request):
    context = featured_collecs()
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')