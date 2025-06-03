from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PegadaCarb(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,related_name="PegadaCarbono")
    dataRe = models.DateField()
    valorTotal = models.IntegerField(blank=True,null=True)

class Mensagem(models.Model):
    cont = models.TextField()
    positiva = models.BooleanField(default=True)
    