"""
URL configuration for GestionCrudsWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from games import views
from noticias import views as noticias
from noticias.views import noticias_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noticias.urls')),
    path('', noticias.noticias_list, name='noticias_list'),
    path('juegos', views.GamesListView, name='games_list'),
    path('agregarjuego/', views.agregar_game, name='agregar_game'),
    path('<int:id>/', views.game_detail, name='game_detail'),
    path('editar/<int:id>/', views.editar_game, name='editar_game'),
    path('eliminar/<int:id>/', views.eliminar_game, name='eliminar_game'),
    path('gestionjuegos/', views.GamesListCrud, name='gestion_games'),
    path('noticias/', include('noticias.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('registro/', registro, name="registro"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
