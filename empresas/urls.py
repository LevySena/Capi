from django.urls import path
from empresas.views import *

urlpatterns = [
    path('',EmpLista,name='listaE'),
    path('empinfo/<eid>',EmpInfo,name="infoE"),
    path('cadEmp/',CadEmp,name="cadEmp"),
    path('tog/',favoritar,name='tog')
]