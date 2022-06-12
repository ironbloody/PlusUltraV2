from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Articulo
from .forms import ArticuloForm

# Create your views here.
def inicio(request):
        return render(request, 'paginas/inicio.html')

def home(request): 
        return render(request, 'paginas/home.html')

def libros(request): 
        libros = Articulo.objects.all()
        return render(request, 'libros/libros.html', {'libros': libros})

def mangas(request): 
        mangas = Articulo.objects.all()
        return render(request, 'libros/mangas.html', {'mangas': mangas})

def comics(request): 
        comics = Articulo.objects.all()
        return render(request, 'libros/comics.html', {'comics': comics})

def crear_libro(request):
        formulario = ArticuloForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
                formulario.save()
                return redirect('libros')

        return render(request, 'libros/crear_libro.html', {'formulario': formulario})

def crear_manga(request):
        formulario = ArticuloForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
                formulario.save()
                return redirect('mangas')

        return render(request, 'libros/crear_manga.html', {'formulario': formulario})
        
def editar(request, id):
        libro = Articulo.objects.get(id=id)
        formulario = ArticuloForm(request.POST or None, request.FILES or None, instance=libro)
        if formulario.is_valid() and request.POST:
                formulario.save()
                return redirect('libros')
        return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
        libro = Articulo.objects.get(id=id)
        libro.delete()
        return render('libro')