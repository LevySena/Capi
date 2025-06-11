from django.shortcuts import render,redirect
from django.http import HttpRequest
from msg.models import Mensagem
from msg.forms import MsgForm
# Create your views here.

def MsgLista(request : HttpRequest):
    Allmsg = Mensagem.objects.all()
    contexto = {
        'msg' : Allmsg
    }
    return render(request, "msg/mensagem.html",context=contexto)

def MsgCad(request : HttpRequest):
    formulario = MsgForm()
    if request.method == 'POST':
        formulario = MsgForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(MsgLista)
            
    contexto = {
        'forms' : formulario
    }
    return render(request,"msg/cadMsg.html",context=contexto)

def AtualizarMsg(request:HttpRequest,pid):
    verify = Mensagem.objects.filter(id=pid)
    if not verify:
        return redirect(MsgCad)
    obj = Mensagem.objects.get(id=pid)
    fomulario = MsgForm(instance=obj)
    if request.method == 'POST':
        fomulario = MsgForm(request.POST, instance=obj)
        if fomulario.is_valid():
            fomulario.save()
            return redirect(MsgLista)
    contexto = {
        'forms':fomulario,
        'obj':obj
    }
    return render(request,"msg/AtuMsg.html",context=contexto)

def ApagarMsg(request:HttpRequest,pid):
    msg = Mensagem.objects.get(id=pid)
    msg.delete()
    return redirect(MsgLista)