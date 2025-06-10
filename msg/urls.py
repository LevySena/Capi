from django.urls import path
from msg.views import MsgLista

urlpatterns = [
    path('',MsgLista,name='MsgLista')
]