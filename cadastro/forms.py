from django import forms
from django.contrib.auth.models import User
from cadastro.utils.validador import formatar_cpf,validador
from cadastro.utils.validar_email import validar_email_com_biblioteca
from django.core.exceptions import ValidationError

def cpf_validator(valor):
    if not validador(valor):
        print("Cpf Inválido")
        raise ValidationError("CPF inválido!")

def email_validator(email):
    if not validar_email_com_biblioteca(email):
        print("Email Inválido")
        raise ValidationError("Email inválido!")

class Cadastro_Form(forms.ModelForm):
    cpf = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'placeholder':'Cpf','class':'form-control'}),required=True,validators=[cpf_validator])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control',"required": True}),required=True,validators=[email_validator])
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Nome do usuário','class':'form-control'}),
            #'email' : forms.EmailInput(attrs={'placeholder':'Email','class':'form-control',"required": True}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Senha','class':'form-control','id':'senha'}),
        }