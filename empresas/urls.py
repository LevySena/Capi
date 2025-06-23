from django.urls import path
from empresas.views import *

urlpatterns = [
    path('',EmpLista,name='EmpLista'),
]