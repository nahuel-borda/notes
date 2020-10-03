from django.contrib import admin
from .models import Dialogo, Nota, Personaje, Paragrafo


@admin.register(Dialogo)
class DialogoAdmin(admin.ModelAdmin):
    fields = ["nombre", "enlace", "edicion"]
    model = Dialogo


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    fields = ["fecha", "paragrafo", "renglon", "anotador", "anotacion"]
    model = Nota


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    fields = ["nombre", "descripcion"]
    model = Personaje


@admin.register(Paragrafo)
class ParagrafoAdmin(admin.ModelAdmin):
    fields = ["pagina", "paragrafo", "dialogo", "personajes"]
    model = Paragrafo
