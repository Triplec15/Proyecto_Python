from distutils.command.upload import upload
from email.mime import image
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class Categoria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
        
opciones_consultas = [
    [0 , "consulta"],
    [1 , "reclamo"],
    [2 , "sugerencia"],
    [3 , "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo = models.IntegerField (choices=opciones_consultas)
    mensaje = models.TextField()
    Notificarme =models.BooleanField()
    
    def __str__(self) -> str:
        return self.nombre
    
    