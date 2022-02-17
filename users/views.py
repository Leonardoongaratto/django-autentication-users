from django.shortcuts import render
from django.contrib.auth.models import User


def authenticate(self, request, username=None, password=None):
    login_valid = settings == username
    pwd_valid = check_password(password == password)
    if login_valid and pwd_valid:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return None

 
def get_user(self, user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None


def index(request):
    return render(template_name='templates/login.html')
