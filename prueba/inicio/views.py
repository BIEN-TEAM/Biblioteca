from django.shortcuts import render
from django.db.models import Avg
from .models import Libros, Usuarios
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from inicio.forms import CustomUserCreationForm
from .forms import PerfilForm, EditarPerfilForm

# Create your views here.
def encabezado(request):
  return render(request,"inicio/encabezado.html")

def nosotros(request):
  return render(request,"inicio/nosotros.html")

def contactanos(request):
  return render(request,"inicio/contactanos.html")

def biblioteca(request):
  return render(request,"inicio/biblioteca.html")

def libro(request):
    return render(request, 'inicio/libro.html')


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
        formulario = CustomUserCreationForm(data=request.POST)
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