from django.contrib import admin

from .models import Collection

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'image', 'description', 'size', 'is_visible', 'upload_date', 'last_update', 'rating')
    list_display_links = ('id', 'creator')
    list_filter = ('is_visible',)
    list_editable = ('is_visible',)
    search_fields = ('title',  'creator', 'description')
    list_per_page = 25

admin.site.register(Collection, CollectionAdmin)