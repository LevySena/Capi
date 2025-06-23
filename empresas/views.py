from django.shortcuts import render,redirect
from django.http import HttpRequest
from empresas.models import Empresas
# Create your views here.

def EmpLista(request : HttpRequest):
    EmpAll = Empresas.objects.all()
    contexto = {
        "emp" : EmpAll
    }
    return render(request,"emp/Empre.html",context=contexto)