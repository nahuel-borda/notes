from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Dialogo(models.Model):
    nombre = models.CharField(max_length=100)
    enlace = models.CharField(max_length=200, null=True, blank=True)
    edicion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre}"

class Paragrafo(models.Model):
    pagina = models.IntegerField()
    paragrafo = models.CharField(max_length=50)
    dialogo = models.ForeignKey(Dialogo, on_delete=models.PROTECT, related_name='paragrafos')
    personajes = models.ManyToManyField(Personaje, related_name='apariciones', blank=True)

    def __str__(self):
        return f"{self.pagina}{self.paragrafo}, {self.dialogo}"

    class Meta:
        ordering = ['dialogo__nombre', '-pagina', '-paragrafo']

class Nota(models.Model):
    renglon = models.IntegerField()
    fecha = models.DateField(default=timezone.now, null=True)
    anotacion = models.TextField()
    paragrafo = models.ForeignKey(Paragrafo, on_delete=models.PROTECT, related_name='anotaciones')
    anotador = models.ForeignKey(User, on_delete=models.PROTECT, related_name='anotaciones', null=True)

    def __str__(self):
        return f"{self.paragrafo} \"{self.anotacion}\" {self.anotador}"

    class Meta:
        ordering = ['fecha']
