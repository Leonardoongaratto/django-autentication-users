from django.urls import path
from .views import authenticate,index
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/', index)
]
