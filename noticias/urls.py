from django.urls import path
from . import views
from .views import registro

urlpatterns = [
    
    path('crud/', views.noticias_list_crud, name='noticias_list_crud'),
    path('<int:id>/', views.noticia_detail, name='noticia_detail'),
    path('agregar/', views.agregar_noticia, name='agregar_noticia'),
    path('editar/<int:id>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar/<int:id>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('registro/', registro, name="registro"),
]
