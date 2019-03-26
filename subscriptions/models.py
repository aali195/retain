from django.db import models
from datetime import datetime

from django.conf import settings
from collecs.models import Collection

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)
    sub_date = models.DateTimeField(default=datetime.now)
    completed_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    class Meta:
        unique_together = ["user", "collection"]