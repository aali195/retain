from django.contrib import auth

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is None:
        return 0
    else:
        auth.login(request, user)
        return 1

