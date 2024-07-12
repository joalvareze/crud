from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia
from .forms import NoticiaForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def noticias_list(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, "noticias/noticias_list.html", {"noticias": noticias})


def noticias_list_crud(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, "noticias/noticias_crud.html", {"noticias": noticias})

def noticia_detail(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.visitas += 1
    noticia.save()
    return render(request, "noticias/noticia_details.html", {'noticia': noticia})


def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Noticia agregada correctamente')
            return redirect('noticias_list')
    else:
        form = NoticiaForm()
    return render(request, "noticias/noticia_form.html", {'form': form})

def eliminar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.delete()
    messages.success(request, f'Se ha eliminado la noticia "{noticia.titulo}"')
    return redirect('noticias_list')

def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Noticia actualizada correctamente')
            return redirect('noticias_list')
        else:
            messages.error(request, 'Formulario no válido. Errores: {form.errors}')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticias/noticia_form.html', {'form': form})


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password2"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="noticias_list")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)