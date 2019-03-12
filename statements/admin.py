from django.contrib import admin

from .models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection', 'image', 'statement', 'question', 'answer')
    list_display_links = ('id', 'collection')
    search_fields = ('collection',  'statement', 'question', 'answer')
    list_per_page = 25

admin.site.register(Statement, StatementAdmin)