from django.urls import path
from login.views import Login_User

urlpatterns = [
    path('',Login_User,name='login'),
]