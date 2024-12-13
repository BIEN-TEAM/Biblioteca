from django.shortcuts import render
from django.db.models import Avg
from .models import Libros, Usuarios , Reseñas, ComentarioContacto
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from inicio.forms import CustomUserCreationForm
from .forms import PerfilForm, EditarPerfilForm,ComentarioContactoForm
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from django.contrib.auth import logout
from django.shortcuts import redirect
import os

# Create your views here.
def encabezado(request):
  return render(request,"inicio/encabezado.html")

def nosotros(request):
  return render(request,"inicio/nosotros.html")


def contactanos(request):
  return render(request,"inicio/contactanos.html")

from django.shortcuts import render
from .models import Libros, Categorias

def biblioteca(request):
    # Obtener parámetros de búsqueda
    query = request.GET.get('q', '')  # Toma el valor de búsqueda
    genero = request.GET.get('genero', '')  # Toma el valor del género seleccionado
    
    # Filtrar libros
    libros = Libros.objects.all()  # Todos los libros por defecto
    if query:
        libros = libros.filter(nombre__icontains=query)  # Filtrar por nombre del libro
    if genero:
        libros = libros.filter(categorias__nombre=genero)  # Filtrar por género
    
    # Obtener todos los géneros para el filtro
    generos = Categorias.objects.all()

    # Renderizar la plantilla
    return render(request, 'inicio/biblioteca.html', {
        'libros': libros,
        'generos': generos,
        'query': query,
        'genero_seleccionado': genero,
    })

def libro(request):
    libro = get_object_or_404(Libros, id_libro=12)  # Ejemplo para obtener el libro con ID 12
    return render(request, 'inicio/libro.html', {'libro': libro})

def logout_view(request):
    logout(request)
    return redirect('/')

def top_3_libros(request):
    libros = Libros.objects.annotate(promedio=Avg('reseñas__calificacion')).order_by('-promedio')[:3]

    for libro in libros:
        # Calcular las estrellas completas
        libro.estrellas_completas = int(libro.promedio)  # Redondeamos a entero para las estrellas completas
        
        # Determinamos si hay una estrella media
        libro.estrellas_medias = 1 if (libro.promedio - libro.estrellas_completas) >= 0.5 else 0
        
        # Estrellas vacías: el resto de estrellas hasta completar 5
        libro.estrellas_vacias = 5 - libro.estrellas_completas - libro.estrellas_medias

    return render(request, 'inicio/top_libros.html', {'libros': libros})

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()   
            user = authenticate(email=formulario.cleaned_data["email"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('top_libros')
        data["form"] = formulario

    return render(request, "registration/registro.html", data)


# views.py

@login_required
def perfilusuario(request):
    # Obtén el usuario actualmente autenticado
    usuario = request.user
    # Pasa el usuario a la plantilla
    return render(request, 'usuario/perfilusuario.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':    
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente')  # Mensaje de éxito
            return redirect('Perfil Usuario')  # Redirige a la página de perfil después de guardar
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'usuario/editarperfil.html', {'form': form})

def registrar_comentario(request):
  if request.method == 'POST':
      form = ComentarioContactoForm(request.POST)
      if form.is_valid(): 
            form.save() 
            return render(request,'inicio/contactanos.html')
  form = ComentarioContactoForm()
  return render(request,'inicio/contactanos.html',{'form': form})


# views.py
from django.shortcuts import render


def comentarios_view(request):
    # Obtener todos los comentarios
    comentarios = ComentarioContacto.objects.all().order_by('-created')
    
    # Pasar los comentarios al template
    return render(request, 'inicio/tabla.html', {'comentarios': comentarios})


def descargar_pdf(request, id):
    libro = get_object_or_404(Libros, id_libro=id)
    response = FileResponse(libro.pdf.open(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{libro.pdf.name}"'
    return response

def libroCat(request, libro_id):
    libro = get_object_or_404(Libros, id_libro=libro_id)
    categorias = libro.categorias.all()
    
    print(f"Categorias del libro: {categorias}")  # Agrega esta línea para depurar
    
    return render(request, 'inicio/libro.html', {'libro': libro, 'categorias': categorias})

def bibliotecasq(request):
    libros = Libros.objects.all()
    return render(request, 'inicio/biblioteca.html', {'libros': libros})

def libro_detalle(request):
  return render(request,"inicio/libro_detalle.html")

def libro_detallebd(request, id_libro):
    libro = get_object_or_404(Libros, id_libro=id_libro)
    return render(request, 'inicio/libro_detalle.html', {'libro': libro})


def registrar_reseña(request, libro_id):
    libro = get_object_or_404(Libros, id_libro=libro_id)
    
    if request.method == 'POST':
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')

        reseña = Reseñas(
            libro=libro,
            usuario=request.user,
            calificacion=calificacion,
            comentario=comentario
        )
        reseña.save()
        
        return redirect('libro_detalle', libro_id=libro.id_libro)  

    return render(request, 'libro_detalle.html', {'libro': libro})