from django.db import models
from datetime import datetime

from django.conf import settings
from statements.models import Statement

class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    statement = models.ForeignKey(Statement, on_delete=models.DO_NOTHING)
    review_total = models.IntegerField(default=0)
    review_correct = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    priority = models.IntegerField(default=50)
    note = models.CharField(max_length=250, default='N/A')
    update_date = models.DateTimeField(default=datetime.now)