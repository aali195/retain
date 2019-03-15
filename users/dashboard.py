from collecs.models import Collection
from subscriptions.models import Subscription

def user_details(request):
    active = current_details(request)
    created = created_list(request)
    subbed= subbed_list(request)

    context = {
        'active': active,
        'created': created,
        'subbed': subbed
    }
    return context

def current_details(request):
    # Need to filter gainst active collection
    return Collection.objects.order_by('-upload_date')

def created_list(request):
    return Collection.objects.order_by('-upload_date').filter(creator=request.user)

def subbed_list(request):
    return Collection.objects.order_by('-subscription__sub_date').filter(subscription__user=request.user)