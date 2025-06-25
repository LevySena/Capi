from django.shortcuts import render,redirect
from django.http import HttpRequest,JsonResponse
from empresas.models import Empresas
import json
# Create your views here.

def EmpLista(request : HttpRequest):
    EmpAll = Empresas.objects.all()
    contexto = {
        "emp" : EmpAll
    }
    return render(request,"emp/Empre.html",context=contexto)

def EmpInfo(request :HttpRequest,eid):
    if not Empresas.objects.filter(id=eid):
        return redirect(EmpLista)
    obj = Empresas.objects.get(id=eid)
    contexto = {
        'obj' : obj
    }
    return render(request,"emp/infoemp.html",context=contexto)

def favoritar(request : HttpRequest):
    print(request.body)
    try:
        user = request.user
        valor = json.loads(request.body)
        emp_id=valor.get('empresa_id')
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