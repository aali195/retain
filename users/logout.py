from django.contrib import auth

def logout_user(request):
     auth.logout(request)