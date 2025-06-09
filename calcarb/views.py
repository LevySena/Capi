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
    if request.method == 'POST':
        formulario = Perguntas(request.POST)
        # for k,c in request.POST.items():
        #     print(f'{k} = {c}')
        if formulario.is_valid():
            print("Valido")
            carbElec = None
            try:
                carbElec = (formulario.cleaned_data['precMes']/formulario.cleaned_data['precRegion']) * 0.0385
                carbGas = formulario.cleaned_data['gasCoz'] * 2.9380
                if formulario.cleaned_data['veiculoP'] == "carro":
                    if formulario.cleaned_data['tCombC'] == "diesel":
                        carbLKm = (formulario.cleaned_data['krodado'] / 12.3)*2.44
                    elif formulario.cleaned_data['tCombC'] == "etanol":
                        carbLKm = (formulario.cleaned_data['krodado']/11.4)*1.50
                    elif formulario.cleaned_data['tCombC'] == "gasolina":
                        carbLKm = (formulario.cleaned_data['krodado']/17.5)*2.19
                    else:
                        carbLKm = (formulario.cleaned_data['krodado']/16)*1.92
                elif formulario.cleaned_data['veiculoP'] == "moto":
                    if formulario.cleaned_data['tCombC'] == "etanol":
                        carbLKm = (formulario.cleaned_data['krodado']/24.7)*1.50
                    else:
                        carbLKm = (formulario.cleaned_data['krodado']/35)*2.19
                else:
                    carbLKm = 0
                carbTotal = carbLKm + carbGas + carbElec
                print(f"Carbono total = {carbTotal}")
            except ZeroDivisionError:
                formulario.add_error('precRegion','Digite um valor maior que zero')
        else: print(formulario.errors)
    contexto = {
    "forms" : formulario
    }
    return render(request,"calc/calcQ.html",context=contexto)