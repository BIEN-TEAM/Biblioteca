from django.shortcuts import render

# Create your views here.
def encabezado(request):
  return render(request,"inicio/encabezado.html")

def inicio(request):
  return render(request,"inicio/inicio.html") 

def nosotros(request):
  return render(request,"inicio/nosotros.html")