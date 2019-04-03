from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from datetime import datetime
from random import randint

from statements.models import Statement
from usersettings.models import UserSettings
from subscriptions.models import Subscription
from progress.models import Progress


def get_next_learn(user):
    user_settings = get_object_or_404(UserSettings, user=user)
    subscription = get_object_or_404(Subscription, collection=user_settings.active_collection, user=user)
    statements = Statement.objects.filter(collection=subscription.collection)
    if statements.count() < 10:
        raise PermissionDenied(detail="Collection has less than 10 statements.", code=403)
    return statements.order_by('id')[subscription.completed_count:subscription.completed_count+1]


def save_learn_result(user, statement_id, note):
    statement = get_object_or_404(Statement, pk=statement_id)
    subscription = get_object_or_404(Subscription, user=user, collection=statement.collection)
    subscription.completed_count += 1
    subscription.save()
    return Progress.objects.create(user=user, statement=statement, note=note)


def get_next_review(user):
    user_settings = get_object_or_404(UserSettings, user=user)
    active_statements = Statement.objects.filter(collection=user_settings.active_collection)
    if user_settings.active_collection is None:
        raise PermissionDenied(detail="No collection active.", code=403)
    elif active_statements.count() < 10:
        raise PermissionDenied(detail="Collection has less than 10 statements.", code=403)
    else:
        user_collection_progress = Progress.objects.filter(user=user, statement__collection=user_settings.active_collection)
        if user_collection_progress.count() < 4:
            raise PermissionDenied(detail="Need to learn 4 statements before reviewing", code=403)
        else:
            
            active_progress = user_collection_progress.order_by('-priority')[0]
            
            return active_progress


def save_review_result(user, current_statement, is_correct):
    
    subscription = get_object_or_404(Subscription, user=user, collection=current_statement.collection)
    subscription.last_reviewed = datetime.now()
    subscription.save()

    progress = get_object_or_404(Progress, user=user, statement=current_statement)
    progress.update_date = datetime.now()
    progress.review_total += 1
    
    if is_correct:
        progress.review_correct += 1
        if ((progress.streak +2) <= 6):
            progress.streak += 2
    else:
        if (progress.streak >= -6):
            progress.streak -= 1

    variation = randint(-2, 0)
    if (progress.priority + variation) in range(-50, 50):
        progress.priority += variation
    if (progress.priority - progress.streak) in range(-50, 50):
        progress.priority -= progress.streak
    
    progress.save()

    return



