from django.shortcuts import get_object_or_404

from .models import Collection
from statements.models import Statement


def get_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    statements = Statement.objects.filter(collection=collection)[:10]

    context = {
        'collection': collection,
        'statements': statements,
        'values': request.GET
    }
    return context