from django import forms
from cadastro.models import Cadastro_Pessoa
from django.contrib.auth.models import User

class PerfilForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput(),required=False,label="")
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome do usuário','class':'form-control'}),label="Nome")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),label="Email")
    cpf = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'placeholder':'Cpf','class':'form-control'}),label="Cpf")
    senhaN = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Senha','class':'form-control','id':'senha'}),label="Senha")

    def save(self):
        data = self.cleaned_data
        user_id = data.get("user_id")
        if user_id:
            usuario = User.objects.get(id=user_id)
            usuario.username = data["nome"]
            usuario.email = data["email"]
            usuario.set_password(data["senhaN"])
            usuario.save()
            perfi = Cadastro_Pessoa.objects.get(user=usuario)
            perfi.email = data['email']
            perfi.cpf = data['cpf']
            perfi.save()
        return usuario, perfi

class showPerfil(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','readonly':'readonly'}))

    def save(self):
        data = self.cleaned_data
        user_id = data.get("user_id")
        if user_id:
            usuario = User.objects.get(id=user_id)
            usuario.delete()