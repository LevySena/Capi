from django import forms
from django.contrib.auth.models import User

class Cadastro_Form(forms.ModelForm):
    cpf = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'placeholder':'Cpf','class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Nome do usuário','class':'form-control'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Senha','class':'form-control'}),
        }