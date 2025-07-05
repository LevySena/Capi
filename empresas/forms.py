from django import forms
from empresas.models import Empresas

class EmpForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['company_name','location','sector','near_term_status','near_term_target_year']
        widgets = {
            'company_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}),
            'location' : forms.TextInput(attrs={'class':'form-control','placeholder':'Localização'}),
            'sector' : forms.TextInput(attrs={'class':'form-control','placeholder':'Setor'}),
            'near_term_status' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Ano'}),
            'near_term_target_year' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Ano alvo'}),
        }