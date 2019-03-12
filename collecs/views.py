from django.shortcuts import render

from . import listings

def index(request):
    context = listings.collections(request)
    return render(request, 'collecs/collections.html', context)

def collection(request, collection_id):
    return render(request, 'collecs/collection.html')

def search(request):
    return render(request, 'collecs/search.html')