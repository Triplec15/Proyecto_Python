from django.db import models
from django.contrib.auth.models import User

class DataUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    url_imagen = models.URLField(max_length=200)
    descripcion = models.CharField(max_length=250)