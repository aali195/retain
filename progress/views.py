from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


from usersettings.models import UserSettings
from progress.models import Progress
from subscriptions.models import Subscription


def learn(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to start a learning session')
        return redirect('index')
    else:

        user_settings = get_object_or_404(UserSettings, user=request.user)
        subscription = get_object_or_404(Subscription, user=request.user, collection=user_settings.active_collection)
        if subscription.completed_count == subscription.collection.size:
            messages.error(request, 'You have completed learning the currently active collection')
            return redirect('dashboard')
        else:
            context = {
                'user_settings': user_settings,
                'subscription': subscription,
            }
            return render(request, 'progress/learn.html', context)

def review(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to start a reviewing session')
        return redirect('index')
    else:
        user_settings = get_object_or_404(UserSettings, user=request.user)
        subscription = get_object_or_404(Subscription, user=request.user, collection=user_settings.active_collection)

        if subscription.completed_count < 4:
            messages.error(request, 'You need to learn at least 4 statements before a learning session')
            return redirect('dashboard')
        else:
            context = {
                'user_settings': user_settings,
                'subscription': subscription,
            }
            return render(request, 'progress/review.html', context)