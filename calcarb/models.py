from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class PegadaCarb(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,related_name="PegadaCarbono")
    dataRe = models.DateField(default=now())
    valorTotal = models.FloatField(blank=True,null=True)
    def __str__(self):
        return f"{self.usuario} : {self.dataRe}"