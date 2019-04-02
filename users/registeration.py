from django.contrib.auth import get_user_model

from usersettings.models import UserSettings
User = get_user_model()

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    result = check_input(username, email, password, password2)

    if result != 1:
        return result
    else:
        return save_user(username, email, password, password2)

def check_input(username, email, password, password2):
    if password != password2:
        return 'Passwords do not much'
    else:
        if User.objects.filter(username=username).exists():
            return 'Username is taken'
        else:
            if User.objects.filter(email=email).exists():
                return 'Email is taken'
            else:
                # Success
                return 1

def save_user(username, email, password, password2):
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    UserSettings.objects.create(user=user)
    return 1
