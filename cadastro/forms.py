from django import forms
from django.contrib.auth.models import User

class Cadastro_Form(forms.ModelForm):
    cpf = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'placeholde':'Cpf'}))
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Nome do usuário'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Nome do usuário'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Nome do usuário'}),
            
        }