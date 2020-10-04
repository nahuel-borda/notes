from django.contrib import admin
from .models import Dialogo, Nota, Personaje, Paragrafo


@admin.register(Dialogo)
class DialogoAdmin(admin.ModelAdmin):
    fields = ["nombre", "edicion", "enlace"]
    list_display = ["nombre", "edicion", "enlace"]
    list_filter = ["nombre", "edicion"]
    model = Dialogo


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    fields = ["fecha", "paragrafo", "renglon", "anotacion"]
    list_display = ["anotacion", "paragrafo", "renglon"]
    list_filter = ["paragrafo__dialogo__nombre", "anotador", "paragrafo"]
    exclude = ["anotador"]
    model = Nota

    def seccion(self):
        return f"{str(self.paragrafo)}"

    def save_model(self, request, obj, form, change):
        obj.anotador = request.user
        super().save_model(request, obj, form, change)


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    fields = ["nombre", "descripcion"]
    model = Personaje


@admin.register(Paragrafo)
class ParagrafoAdmin(admin.ModelAdmin):
    fields = ["pagina", "paragrafo", "dialogo", "personajes"]
    model = Paragrafo
