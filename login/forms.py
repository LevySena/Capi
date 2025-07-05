from django import forms

class LoginUser(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder':'Usuário','class':'form-control'}))
    
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder':'Senha','class':'form-control'}))