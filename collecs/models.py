from django.db import models
from datetime import datetime
from django.conf import settings

class Collection(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='collections/%Y/%m', default='no-image.png')
    description = models.TextField(blank=True)
    size = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=False)
    upload_date = models.DateTimeField(default=datetime.now)
    last_update = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title