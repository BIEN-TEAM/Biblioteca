from django.shortcuts import render
from django.db.models import Avg
from .models import Libros

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