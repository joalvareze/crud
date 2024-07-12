from django import forms
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'imagen', 'resena', 'cuerpo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la noticia'}),
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*', 'directory': 'noticias'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve reseña de la noticia'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Contenido completo de la noticia'}),
        }


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model= User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]