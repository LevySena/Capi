from django import forms
from msg.models import Mensagem

class MsgForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome','cont','positiva']
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}),
            'cont' : forms.TextInput(attrs={'class':'form-control','placeholder':'Descrição'}),
            'positiva' : forms.CheckboxInput(attrs={'class':'form-check-input ms-2'})
        }