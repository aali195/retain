from django.db import models
from datetime import datetime

from collecs.models import Collection

class Statement(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='statements/%Y/%m', default='no-image.png')
    statement = models.CharField(max_length=200)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=25)
    def __str__(self):
        return self.statement
