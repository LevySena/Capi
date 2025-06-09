from django import forms
from django.core.exceptions import ValidationError

TRANSPORTE_VEIC = {
    "-" : "Escolha seu veículo",
    "carro" : "Carro",
    "moto" : "Moto",
    "bike" : "Bike",
    #"bielec" : "Bicicleta elétrica",
    #"patinete" : "Patinete elétrico"
}
TIPO_COMBUST_CAR = {
    "-" : "Selecione o combustível",
    "diesel" : "Diesel", #12,3 km/l
    "etanol" : "Etanol", #11,4 km/l
    "gasolina" : "Gasolina", #17,5 km/l
    "gnv" : "GNV", #16 km/m3
    #"elec" : "Elétrico"
}
TIPO_COMBUST_MOTO = {
    "-" : "Selecione o combustível",
    "etanol" : "Etanol", #24,7 km/l
    "gasolina" : "Gasolina", #35 km/l
}

def veic_validator(valor):
    if valor == "-":
        raise ValidationError("Selecione um valor")
    

class Perguntas(forms.Form):
    precMes = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Responda em R$','class':'form-control'})) # x 0,0385 mensal
    precRegion = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Responda em R$','class':'form-control'})) # preço cobrado por kwh
    gasCoz = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Responda aqui','class':'form-control'})) # x 2,9380 mensal
    veiculoP = forms.ChoiceField(validators=[veic_validator],choices=TRANSPORTE_VEIC,widget=forms.Select(attrs={'class':'seletor form-control'})) #
    tCombC = forms.ChoiceField(choices=TIPO_COMBUST_CAR,widget=forms.Select(attrs={'class':'form-control'}),required=False) #
    tCombM = forms.ChoiceField(choices=TIPO_COMBUST_MOTO,widget=forms.Select(attrs={'class':'form-control'}),required=False) #
    krodado = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Responda aqui','class':'form-control'}))