from django.urls import path
from painel.views import *

urlpatterns = [
    path('',Painel,name="painel"),
    path('atualizar/',AtuInfo,name="atuinfo"),
    path('deletar/',DelUser,name="delinfo")
]