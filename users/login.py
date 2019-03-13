from django.contrib.auth import get_user_model
from django.contrib import auth

User = get_user_model()

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is None:
        return 0
    else:
        auth.login(request, user)
        return 1

