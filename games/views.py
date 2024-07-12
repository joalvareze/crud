from django.shortcuts import render, redirect, get_object_or_404
from .models import Games
from .forms import GamesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def GamesListView(request):
    games = Games.objects.all().order_by('nombre')
    return render(request, "games_list.html", {"games": games})

def GamesListCrud(request):
    games = Games.objects.all().order_by('nombre')
    return render(request, "games_crud.html", {"games": games})

def game_detail(request, id):
    game = get_object_or_404(Games, id=id)
    return render(request, "game_details.html", {'game': game})

def agregar_game(request):
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return GamesListView(request)
    else:
        form = GamesForm()
    return render(request, "game_form.html", {'form': form})

def eliminar_game(request, id):
    game = Games.objects.get(id=id)
    game.delete()
    messages.success(request, f'Se ha eliminado {game.nombre}')
    return redirect('games-list')

def editar_game(request, id):
    game = get_object_or_404(Games, id=id)
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            print("Formulario válido. Juego guardado.")
            return redirect('games_list')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = GamesForm(instance=game)
    return render(request, 'game_form.html', {'form': form})


def inedex(request):
    return render(request, 'plantilla/base.html')

def registro(request):
    return render(request, 'registration/registro.html')
