from django.shortcuts import render
from django.http import HttpRequest
from msg.models import Mensagem
# Create your views here.

def MsgLista(request : HttpRequest):
    Allmsg = Mensagem.objects.all()
    contexto = {
        'msg' : Allmsg
    }
    return render(request, "msg/mensagem.html",context=contexto)