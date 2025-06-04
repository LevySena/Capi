from django import forms
from django.core.exceptions import ValidationError

TRANSPORTE_VEIC = {
    "-" : "Escolha seu veículo",
    "carro" : "Carro",
    "moto" : "Moto",
    "bike" : "Bike",
    "bielec" : "Bicicleta elétrica",
    "patinete" : "Patinete elétrico"
}
TIPO_COMBUST_CAR = {
    "-" : "Selecione o combustível",
    "disel" : "Diesel",
    "etanol" : "Etanol",
    "gasolina" : "Gasolina",
    "gnv" : "GNV",
    "elec" : "Elétrico"
}
TIPO_COMBUST_MOTO = {
    "-" : "Selecione o combustível",
    "etanol" : "Etanol",
    "gasolina" : "Gasolina",
}

def veic_validator(valor):
    if valor == "-":
        raise ValidationError("Selecione um valor")


class Perguntas(forms.Form):
    precMes = forms.FloatField(attrs={'placeholder':'Responda aqui','class':'form-control'})
    precRegion = forms.FloatField(attrs={'placeholder':'Responda aqui','class':'form-control'})
    gasCoz = forms.IntegerField(attrs={'placeholder':'Responda aqui','class':'form-control'})
    veiculoP = forms.ChoiceField(validators=veic_validator,choices=TRANSPORTE_VEIC,attrs={'class':'form-control'})
    tCombC = forms.ChoiceField(validators=veic_validator,choices=TIPO_COMBUST_CAR,attrs={'class':'form-control'})
    tCombM = forms.ChoiceField(validators=veic_validator,choices=TIPO_COMBUST_MOTO,attrs={'class':'form-control'})