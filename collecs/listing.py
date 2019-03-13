from django.shortcuts import get_object_or_404

from .models import Collection

def get_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)

    context = {
        'collection': collection,
        'values': request.GET
    }
    return context