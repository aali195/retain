from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime

from .forms import NewCollectionForm, EditCollectionForm
from .listings import list_collections
from .search import search_collections
from .listing import get_collection

from .models import Collection
from statements.models import Statement


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
    form = NewCollectionForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            collection = form.save(commit=False)
            collection.creator = request.user
            collection.save()
            messages.success(request, 'Collection has been created successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid details')
            return render(request, 'collecs/new.html', context)
    else:
        return render(request, 'collecs/new.html', context)

def edit(request, collection_id):

    collection = get_object_or_404(Collection, pk=collection_id)
    if collection.creator != request.user:
        messages.error(request, 'Collections can only be edited by their creator')
        return redirect('dashboard')
    else:
        form = EditCollectionForm(request.POST or None, instance=collection)
        statements = Statement.objects.filter(collection=collection_id)
        context = {
            'form': form,
            'statements': statements,
            'collection': collection,
        }
        if request.method == 'POST':
            if form.is_valid():
                edited_collection = form.save(commit=False)
                edited_collection.last_update = datetime.now()
                edited_collection.save()
                messages.success(request, 'Collection has been edited successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid details')
                return render(request, 'collecs/edit.html', context)
        else:
            return render(request, 'collecs/edit.html', context)