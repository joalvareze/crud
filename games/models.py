from django.db import models

class Games(models.Model):

    CLASIFICACION_CHOICES = [
        ('PEGI 3', 'Apto para todas las edades'),
        ('PEGI 7', 'Adecuado para niños pequeños'),
        ('PEGI 12', 'Apto para niños mayores de 12 años'),
        ('PEGI 16', 'Apto para niños mayores de 16 años'),
        ('PEGI 18', 'Solo apto para adultos'),
    ]
    
    nombre = models.CharField(max_length=50, help_text='Nombre del juego')
    clasificacion = models.CharField(
        max_length=40, choices=CLASIFICACION_CHOICES, help_text='Clasificación del juego')
        
    resena = models.TextField(
        blank=True, help_text='Breve reseña del contenido del juego')
    
    puntaje_metacritic = models.PositiveIntegerField(help_text='Valor del juego')
    
    fecha_lanzamiento = models.DateField(
        help_text='Fecha de la publicación del juego')
    
    imagen = models.ImageField(upload_to='games/',null=True,blank=True)


    def __str__(self):
        return self.nombre

