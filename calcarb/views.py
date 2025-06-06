from django.shortcuts import render,redirect
from django.http import HttpRequest
from calcarb.forms import Perguntas
from calcarb.models import PegadaCarb

# Create your views here.

def CalP(request : HttpRequest):
    if request.method == 'POST':
        print('Aqui')
    return render(request,"calc/calcP.html")

def CalQ(request : HttpRequest):
    formulario = Perguntas()
    contexto = {
        "forms" : formulario
    }
    if request.method == 'POST':
        formulario = Perguntas(request.POST)
        # for k,c in request.POST.items():
        #     print(f'{k} = {c}')
        if formulario.is_valid():
            print("Valido")
            carbElec = (formulario.cleaned_data['precMes']/formulario.cleaned_data['precRegion']) * 0.0385
            carbGas = formulario.cleaned_data['gasCoz'] * 2,9380
            
        else: print(formulario.errors)

    return render(request,"calc/calcQ.html",context=contexto)