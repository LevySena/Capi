from django.urls import path
from cadastro.views import Cad

urlpatterns = [
    path('',Cad,name='cadastro'),
]