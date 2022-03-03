from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import check_password


def authenticate(self=None,request=None, username=None, password=None):
     
         try:
             user = User.objects.get(username=username)
             print(user)
         except User.DoesNotExist:
             user = User(username=username)
             user.is_staff = True
             user.is_superuser = True
             user.save()
         except Exception as e:
             print(e)
         else:
             pwd_valid = check_password(password, user.password)
             if user and pwd_valid:
     
                 return user

def index(request):
    x = request.username=request.POST.get('name')
    if x != None:
        authenticate(username=request.POST.get('name'), password=request.POST.get('pass'))

    return render(request, template_name='users/login.html')
