from django.shortcuts import get_object_or_404
from django.db.models import Avg, F

from .models import Collection
from statements.models import Statement
from subscriptions.models import Subscription

def get_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    statements = Statement.objects.filter(collection=collection)[:10]

    if not request.user.is_authenticated:
        context = {
            'collection': collection,
            'statements': statements,
            'values': request.GET
        }
    else:
        subscription = Subscription.objects.filter(user=request.user, collection=collection)

        context = {
            'collection': collection,
            'statements': statements,
            'subscription': subscription,
            'values': request.GET
        }
    return context

def calc_rating(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    subscription = get_object_or_404(Subscription, user=request.user, collection=collection)
    subscription.rating = request.POST['rating-select']
    subscription.save()

    new_rating = Subscription.objects.filter(collection=collection).exclude(rating=0).aggregate(Avg(('rating')))
    collection.rating = int(new_rating['rating__avg'])
    collection.save()
    return

def subscribe_user(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    subscription = Subscription.objects.filter(user=request.user, collection=collection)

    if not subscription.exists():
        Subscription.objects.create(user=request.user, collection=collection)
    else:
        subscription.delete()
    
    return
