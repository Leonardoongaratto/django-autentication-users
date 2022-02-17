from django.urls import path
from .views import authenticate, index

urlpatterns = [
    path('', authenticate),
]
