from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='collections'),
    path('<int:collection_id>', views.collection, name='collection'),
    path('search', views.search, name='search')
]