from django.urls import path
from msg.views import *

urlpatterns = [
    path('',MsgLista,name='MsgLista'),
    path('cad/',MsgCad,name='cadMsg'),
    path('atu/<pid>',AtualizarMsg,name='atumsg'),
    path('del/<pid>',ApagarMsg,name='delmsg')
]