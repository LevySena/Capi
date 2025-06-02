from django.contrib.auth.models import User
from django.db import models

def path_foto(instace, filename):
    extension = filename.split(".")[-1]
    return f"foto_perfil_{instace.id}/perfil_pic.{extension}"
# Create your models here.
class Cadastro_Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='perfil')
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    foto = models.ImageField('Foto do Perfil',
                             null=True,
                             blank=True,
                             upload_to=path_foto,
                             default='perfil/default.png')

    def __str__(self):
        return self.user.username