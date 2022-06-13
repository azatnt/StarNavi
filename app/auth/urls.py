from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name='login_url'),
    path('register/', Register.as_view(), name='register_url'),
]
