from django.urls import path
from calcarb.views import CalP,CalQ

urlpatterns = [
    path('',CalP,name='Calp'),
    path('questions',CalQ,name='CalQ')
]