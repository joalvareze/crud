from django import forms
from .models import Games
from datetime import date

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['nombre', 'clasificacion', 'resena', 'puntaje_metacritic', 'fecha_lanzamiento', 'imagen']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del juego'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve reseña del contenido del juego'}),
            'puntaje_metacritic': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Puntaje en Metacritic'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*', 'directory': 'games'}),
        }

    def clean_puntaje_metacritic(self):
        puntaje_metacritic = self.cleaned_data['puntaje_metacritic']
        if puntaje_metacritic < 0 or puntaje_metacritic > 100:
            raise forms.ValidationError('El puntaje debe estar entre 0 y 100.')
        return puntaje_metacritic

    def clean_fecha_lanzamiento(self):
        fecha_lanzamiento = self.cleaned_data['fecha_lanzamiento']
        if fecha_lanzamiento > date.today():
            raise forms.ValidationError('La fecha de lanzamiento no puede ser futura.')
        return fecha_lanzamiento
