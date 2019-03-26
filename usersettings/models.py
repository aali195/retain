from django.db import models

from collecs.models import Collection
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    active_collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, null=True)
    review_num = models.IntegerField(default=5)
