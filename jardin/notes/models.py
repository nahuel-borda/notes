from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Dialogo(models.Model):
    nombre = models.CharField(max_length=100)
    enlace = models.CharField(max_length=200)
    edicion = models.CharField(max_length=100)


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)


class Paragrafo(models.Model):
    pagina = models.IntegerField()
    paragrafo = models.CharField(max_length=50)
    dialogo = models.ForeignKey(Dialogo, on_delete=models.PROTECT, related_name='paragrafos')
    personajes = models.ManyToManyField(Personaje, related_name='apariciones')


class Nota(models.Model):
    renglon = models.IntegerField()
    fecha = models.DateField(default=timezone.now, null=True)
    anotacion = models.TextField()
    paragrafo = models.ForeignKey(Paragrafo, on_delete=models.PROTECT, related_name='anotaciones')
    anotador = models.ForeignKey(User, on_delete=models.PROTECT, related_name='anotaciones')
