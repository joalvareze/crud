from django.contrib import admin
from .models import Games

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clasificacion', 'puntaje_metacritic', 'fecha_lanzamiento')
    list_filter = ('clasificacion', 'fecha_lanzamiento')
    search_fields = ('nombre', 'clasificacion')

admin.site.register(Games, GamesAdmin)
