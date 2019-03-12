from django.contrib import admin

from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'collection', 'sub_date', 'completed_count', 'rating')
    list_display_links = ('id', 'user', 'collection')
    search_fields = ('user',  'collection')
    list_per_page = 25

admin.site.register(Subscription, SubscriptionAdmin)

