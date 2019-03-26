from django.db import models

from subscriptions.models import Subscription
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    active_sub = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING, null=True)
    review_num = models.IntegerField(default=5)
