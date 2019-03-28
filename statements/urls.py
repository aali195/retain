from django.urls import path

from . import views

urlpatterns = [
    path('<int:collection_id>/statements/new', views.new, name='new_statement'),
    path('<int:collection_id>/statements/<int:statement_id>/edit', views.edit, name='edit_statement'),
]