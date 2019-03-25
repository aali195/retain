from django.urls import path

from .views import UserSettingsView

urlpatterns = [
    path('user/settings', UserSettingsView.as_view(), name='usersettings'),
]