from django.db import models

# Create your models here.
class Mensagem(models.Model):
    nome = models.CharField(max_length=20)
    cont = models.TextField()
    positiva = models.BooleanField(default=True)
    def __str__(self):
        return self.nome