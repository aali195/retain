from django.shortcuts import render

from .listings import list_collections

def index(request):
    context = list_collections(request)
    return render(request, 'collecs/collections.html', context)

def collection(request, collection_id):
    return render(request, 'collecs/collection.html')

def search(request):
    return render(request, 'collecs/search.html')