from django.shortcuts import render,redirect
from django.http import HttpRequest
from cadastro.models import Cadastro_Pessoa
from cadastro.forms import Cadastro_Form
from django.contrib.auth.hashers import make_password
from login.views import Login_User

# Create your views here.
def Cad(request: HttpRequest):
    formulario = Cadastro_Form()
    contexto={
        'form' : formulario
    }
    if request.method == 'POST':
        formulario = Cadastro_Form(request.POST)
        if formulario.is_valid():
            novo = formulario.save()
            senha_cryp = make_password(request.POST['password'])
            novo.password = senha_cryp
            novo.save()
            perfil = Cadastro_Pessoa()
            perfil.cpf = formulario.cleaned_data['cpf']
            perfil.user = novo
            perfil.save()
            #Redirecionar quando tela de login estiver pronta
            return redirect(Login_User)
    return render(request,'cad/tela-cadastro2.html',context=contexto)