from django.shortcuts import get_object_or_404

from collecs.models import Collection
from subscriptions.models import Subscription
from usersettings.models import UserSettings


def activate_collection(request):
    selected_collection_id = request.POST.get('activate')
    collection = get_object_or_404(Collection, pk=selected_collection_id)

    user_settings = get_object_or_404(UserSettings, user=request.user)
    user_settings.active_collection = collection
    user_settings.save()

def dashboard_details(request):
    current = current_details(request)
    created = created_list(request)
    subscriptions = subscription_list(request)

    context = {
        'current': current,
        'created': created,
        'subscriptions': subscriptions,
    }
    return context

def current_details(request):
    user_settings = get_object_or_404(UserSettings, user=request.user)
    return Subscription.objects.get(collection=user_settings.active_collection, user=request.user)

def created_list(request):
    return Collection.objects.order_by('-upload_date').filter(creator=request.user)

def subscription_list(request):
    return Subscription.objects.order_by('-sub_date').filter(user=request.user)