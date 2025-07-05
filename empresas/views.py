from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,JsonResponse
from empresas.models import Empresas
from empresas.forms import EmpForm
import json
# Create your views here.

@login_required(login_url='login')
def EmpLista(request : HttpRequest):
    EmpAll = Empresas.objects.all()
    favoritas = request.GET.get('favoritas_apenas', 'false').lower() == 'true'
    print(request.user.Emp_fav.all())
    if favoritas:
        EmpAll = request.user.Emp_fav.all()
    contexto = {
        "emp" : EmpAll,
        "favoritas_apenas": favoritas
    }
    return render(request,"emp/Empre.html",context=contexto)

@login_required(login_url='login')
def EmpInfo(request :HttpRequest,eid):
    if not Empresas.objects.filter(id=eid):
        return redirect(EmpLista)
    obj = Empresas.objects.get(id=eid)
    contexto = {
        'obj' : obj
    }
    return render(request,"emp/infoemp.html",context=contexto)

@login_required(login_url='login')
def favoritar(request : HttpRequest):
    try:
        user = request.user
        valor = json.loads(request.body)
        emp_id=valor.get('empresa_id')
        print(emp_id)
        favoritada = valor.get('favoritada')
        emp = Empresas.objects.get(id=emp_id)
        if favoritada:
            print("Checado")
            user.Emp_fav.add(emp)
            message = "Empresa favoritada!"
        else:
            user.Emp_fav.remove(emp)
            message = "Empresa removida!"
        return JsonResponse({'status': 'success','message': message})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Requisição inválida (JSON).'}, status=400)
    except Empresas.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Empresa não encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@login_required(login_url='login')
def CadEmp(request : HttpRequest):
    formulario = EmpForm()
    if request.method == 'POST':
        formulario = EmpForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(EmpLista)
    contexto={
        'forms':formulario
    }
    return render(request,"emp/cadEmp.html",context=contexto)