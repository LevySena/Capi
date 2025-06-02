from django.urls import path
from calcarb.views import CalP

urlpatterns = [
    path('',CalP,name='Calp'),
]