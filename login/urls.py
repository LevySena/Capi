from django.urls import path
from login.views import Login_User,Logout

urlpatterns = [
    path('',Login_User,name='login'),
    path('logout/',Logout,name='logout')
]