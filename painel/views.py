from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from painel.forms import PerfilForm
from cadastro.models import Cadastro_Pessoa

# Create your views here.

def Painel(request : HttpRequest):
    return render(request,"painel/painel-usuario.html")

def AtuInfo(request : HttpRequest):
    obj = User.objects.get(id=request.user.id)
    corObj = Cadastro_Pessoa.objects.get(user=obj)
    ini_data = {
        "user_id": request.user.id,
        "nome": obj.username,
        "email":obj.email,
        "cpf":corObj.cpf
    }
    formulario = PerfilForm(request.POST or ini_data)
    if request.method == 'POST':
        if formulario.is_valid():
            obj,corObj=formulario.save()
    contexto={
        "forms":formulario,
    }
    return render(request,"painel/atualiza-usuario.html",context=contexto)

def DelUser(request):
    return render(request,"painel/deleta-usuario.html")