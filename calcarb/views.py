from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from msg.models import Mensagem
from calcarb.forms import Perguntas
from calcarb.models import PegadaCarb
import random

# Create your views here.

@login_required(login_url='login')
def CalP(request : HttpRequest):
    obj = PegadaCarb.objects.filter(usuario = request.user)
    
    contexto={
        'obj':obj.last()
    }

    return render(request,"calc/calcP.html",context=contexto)

@login_required(login_url='login')
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
                newCarb = PegadaCarb()
                newCarb.usuario = request.user
                newCarb.valorTotal = carbTotal
                newCarb.save()

                print(f"Carbono total = {carbTotal}")
            except ZeroDivisionError:
                formulario.add_error('precRegion','Digite um valor maior que zero')
        else: print(formulario.errors)
    contexto = {
    "forms" : formulario
    }
    return render(request,"calc/calcQ.html",context=contexto)

@login_required(login_url='login')
def CalM(request : HttpRequest):
    obj = PegadaCarb.objects.filter(usuario = request.user)
    listaP=list(obj)
    if len(listaP) == 1:
        if listaP[1].valorTotal < 150:
            msg = "Seus hábitos e escolhas já contribuem significativamente para um futuro mais sustentável. Isso demonstra um compromisso notável com a redução do impacto ambiental. Continue inspirando e mostrando que é possível viver de forma mais consciente. Pequenas ações diárias, como as que você já adota, fazem uma grande diferença para o planeta."
        else: msg = "Este resultado é um convite para refletir sobre o impacto das nossas atividades diárias no meio ambiente. Há diversas maneiras de reduzir essa pegada, começando por mudanças simples no consumo de energia, nos hábitos de transporte ou nas escolhas alimentares. Lembre-se, pequenas alterações podem gerar grandes resultados. Estamos aqui para ajudar você a encontrar caminhos para um estilo de vida mais sustentável."
    else:
        df=listaP[-2].valorTotal - listaP[-1].valorTotal
        if df > 0:
            msg = list(Mensagem.objects.filter(positiva=False))
            msg = random.choice(msg)
        else:
            msg = list(Mensagem.objects.filter(positiva=True))
            msg = random.choice(msg)
    contexto={
        'msg':msg,
        'obj': obj.last()
    }
            
    return render(request,"calc/calcM.html",context=contexto)