from django import forms
from django.contrib.auth.models import User
from cadastro.utils.validador import formatar_cpf,validador
from django.core.exceptions import ValidationError

def custom_validator(valor):
    if not validador(valor):
        print("Inválido")
        raise ValidationError("CPF inválido!")

class Cadastro_Form(forms.ModelForm):
    cpf = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'placeholder':'Cpf','class':'form-control'}),required=True,validators=[custom_validator])
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Nome do usuário','class':'form-control'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Email','class':'form-control',"required": True}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Senha','class':'form-control','id':'senha'}),
        }
