from django.shortcuts import render

# Create your views here.
def Cad(request):
    return render(request,'cad/tela-cad.html')