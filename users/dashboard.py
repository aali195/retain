from collecs.models import Collection
from subscriptions.models import Subscription

def user_details(request):
    active = current_details(request)
    created = created_list(request)
    subscriptions = subscription_list(request)

    context = {
        'active': active,
        'created': created,
        'subscriptions': subscriptions
    }
    return context

def current_details(request):
    # Need to filter gainst active collection
    return Collection.objects.order_by('-upload_date')

def created_list(request):
    return Collection.objects.order_by('-upload_date').filter(creator=request.user)

def subscription_list(request):
    return Subscription.objects.order_by('-sub_date').filter(user=request.user)