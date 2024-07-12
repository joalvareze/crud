from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, help_text='Título de la noticia')
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True, help_text='Imagen de la noticia')
    resena = models.TextField(blank=True, help_text='Breve reseña del contenido de la noticia')
    cuerpo = models.TextField(help_text='Cuerpo de la noticia')
    fecha_publicacion = models.DateTimeField(auto_now_add=True, help_text='Fecha de publicación de la noticia')
    visitas = models.PositiveIntegerField(default=0, help_text='Número de visitas a la noticia')

    def __str__(self):
        return self.titulo
