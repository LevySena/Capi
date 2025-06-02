from django.shortcuts import render,redirect

# Create your views here.

def CalP(request):
    return render(request,"calc/calcP.html")