from django.contrib import admin
from .models import Herramienta, Noticia, CategoriaHerramienta

admin.site.register(CategoriaHerramienta)
admin.site.register(Herramienta)
admin.site.register(Noticia)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'fuente')

