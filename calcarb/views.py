from django.shortcuts import render,redirect
from calcarb.forms import Perguntas

# Create your views here.

def CalP(request):
    return render(request,"calc/calcP.html")

def CalQ(request):
    formulario = Perguntas()
    contexto = {
        "forms" : formulario
    }
    return render(request,"calc/calcQ.html",context=contexto)