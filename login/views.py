from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from login.forms import LoginUser

# Create your views here.
def Login_User(request:HttpRequest):
    formulario = LoginUser()
    if request.method == 'POST':
        formulario=LoginUser(request.POST) 
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            senha = formulario.cleaned_data['password']
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login(request,user)
                print("Logado com sucesso")
                #Adicionar redirecionamento quando estiver pronto
            else:
                formulario.add_error('username','Usuário ou Senha incorretas')
    contexto = {
        'form':formulario
    }
    return render(request,'login/login.html',context=contexto)

def Logout(request : HttpRequest):
    logout(request)
    return redirect(Login_User)