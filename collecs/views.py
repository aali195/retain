from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CollectionForm
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

def new(request):
    form = CollectionForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            collection = form.save(commit=False)
            collection.creator = request.user
            collection.save()
            messages.success(request, 'Collection has been created')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid details')
            return render(request, 'collecs/new.html', context)
    else:
        return render(request, 'collecs/new.html', context)

def edit(request, collection_id):
    context = get_collection(request, collection_id)
    return render(request, 'collecs/edit.html', context)