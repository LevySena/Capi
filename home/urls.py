from django.urls import path
from home.views import HomeP

urlpatterns = {
    path('',HomeP,name='Home'),
}