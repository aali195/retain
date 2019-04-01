from django.shortcuts import render, get_object_or_404

from usersettings.models import UserSettings
from progress.models import Progress
from subscriptions.models import Subscription


def learn(request):
    user_settings = get_object_or_404(UserSettings, user=request.user)
    subscription = get_object_or_404(Subscription, user=request.user, collection=user_settings.active_collection)

    context = {
        'user_settings': user_settings,
        'subscription': subscription,
    }
    return render(request, 'progress/learn.html', context)

def review(request):
    user_settings = get_object_or_404(UserSettings, user=request.user)
    subscription = get_object_or_404(Subscription, user=request.user, collection=user_settings.active_collection)

    context = {
        'user_settings': user_settings,
        'subscription': subscription,
    }
    return render(request, 'progress/review.html', context)