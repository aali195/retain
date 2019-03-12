from django.contrib import admin

from .models import Progress

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'statement', 'review_total', 'review_correct', 'update_date', 'note')
    list_display_links = ('id', 'user')
    search_fields = ('user',  'statement', 'note')
    list_per_page = 25

admin.site.register(Progress, ProgressAdmin)
