from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'visitas')
    list_filter = ('fecha_publicacion',)
    search_fields = ('titulo', 'resena', 'cuerpo')

admin.site.register(Noticia, NoticiaAdmin)
