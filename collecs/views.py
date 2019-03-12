from django.shortcuts import render

from .listings import list_collections
from .search import search_collections
from .listing import get_collection

def index(request):
    context = list_collections(request)
    return render(request, 'collecs/collections.html', context)
    
def collection(request, collection_id):
    context = get_collection(request, collection_id)
    return render(request, 'collecs/collection.html', context)

def search(request):
    context = search_collections(request)
    return render(request, 'collecs/search.html', context)