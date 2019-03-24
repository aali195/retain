from django.contrib import admin

from .models import UserSettings

class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'active_collection', 'review_num',)
    list_display_links = ('id',)
    list_per_page = 25

admin.site.register(UserSettings, UserSettingsAdmin)