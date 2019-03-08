from django.shortcuts import render

def index(request):
    return render(request, 'collecs/collections.html')

def collection(request):
    return render(request, 'collecs/collection.html')

def search(request):
    return render(request, 'collecs/search.html')