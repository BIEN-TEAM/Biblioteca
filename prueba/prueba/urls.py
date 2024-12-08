"""
URL configuration for prueba project.

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
from inicio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nosotros/', views.nosotros, name ="Nosotros"),
    path('contactanos/', views.contactanos, name="Contactanos"),
    path('biblioteca/', views.biblioteca, name="Biblioteca"),
    path('libro/', views.libro, name='Libros'),
    path('', views.top_3_libros, name='top_libros'),
    path('perfilusuario/', views.perfilusuario, name='Perfil Usuario'),
    path('editar_perfil/', views.editar_perfil, name='Editar Perfil'),
    path('registro/', views.registro, name='Registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrar/',views.registrar_comentario,name="Registrar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)