from django.urls import path
from calcarb.views import *

urlpatterns = [
    path('',CalP,name='Calp'),
    path('questions',CalQ,name='CalQ'),
    path('results',CalM,name='CalM')
]