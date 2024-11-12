from django.db import models
from ckeditor.fields import RichTextField

# Apartado Editado por Jazzani
class Libros(models.Model):
    id_libro = models.AutoField(verbose_name="ID: ", primary_key=True)  # Usar AutoField en lugar de IntegerField
    ISBN = models.CharField(max_length=100, verbose_name="ISBN: ")
    nombre = models.CharField(max_length=100, verbose_name="Nombre: ")
    autor = models.CharField(max_length=100, verbose_name="Autor: ")
    año = models.DateField(verbose_name="Año: ")  # Quitar max_length en DateField
    created = models.DateTimeField(auto_now_add=True)  # Agregar campo created

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre


class Grupos (models.Model):
    id_grupo = models.IntegerField( verbose_name="ID", primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del grupo")
    privilegios = models.CharField(max_length=100, verbose_name="Privilegios")
    created = models.DateTimeField(auto_now_add=True)  # Agregar campo created

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ["-created"]

    def __str__(self):

        return self.nombre


# Apartado Editado por Jazzani
class Usuarios(models.Model):
    id_usuario = models.AutoField(verbose_name="ID: ", primary_key=True)  # Usar AutoField
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, verbose_name="Grupo: ")
    nombre = models.CharField(max_length=100, verbose_name="Nombre: ")  # Quitar la coma
    email = models.EmailField(max_length=100, verbose_name="Correo electrónico: ")
    contraseña = models.CharField(max_length=100, verbose_name="Contraseña: ")
    created = models.DateTimeField(auto_now_add=True)  # Agregar campo created

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Reseñas(models.Model):
    id_reseña = models.IntegerField( verbose_name="ID: ", primary_key=True)
    calificacion = models.IntegerField(verbose_name="Calificación: ")
    comentario = models.TextField(verbose_name="Comentario: ")
    created = models.DateTimeField(auto_now_add=True)  # Agregar campo created
    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ["-created"]

    def __str__(self):
        return self.comentario

class Categorias(models.Model):
    id_categoria = models.AutoField(verbose_name="ID: ", primary_key=True)  # Usar AutoField
    nombre = models.CharField(max_length=100, verbose_name="Nombre: ")
    created = models.DateTimeField(auto_now_add=True)  # Agregar campo created

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]

    def _str_(self):
        return self.nombre

class Libros_Categorias(models.Model):
    id_libro_categoria = models.AutoField(verbose_name="ID: ", primary_key=True)
    id_libro = models.ForeignKey('Libros', on_delete=models.CASCADE, verbose_name="Libros: ")
    id_categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE, verbose_name="ID:")
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.id_libro_categoria)

class Descargas(models.Model):
    id_descarga = models.AutoField(verbose_name="ID: ", primary_key=True)  # Usar AutoField
    id_libro = models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name="ID_Libro: ")
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="ID_Usuario")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de descarga: ")
    created = models.DateTimeField(auto_now_add=True)  # Agregar campo created

    class Meta:
        verbose_name = "Descarga"
        verbose_name_plural = "Descargas"
        ordering = ["-created"]

    def _str_(self):
        return str(self.id_descarga)


class Ver_Libros(models.Model):
    id_ver_libro = models.AutoField(verbose_name="ID: ", primary_key=True)
    id_libro = models.ForeignKey('Libros', on_delete=models.CASCADE, verbose_name="ID_Libro: ")
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, verbose_name="ID_Usuario")
    fecha = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Ver Libro"
        verbose_name_plural = "Ver Libros"
        ordering = ["-created"]

    def _str_(self):
        return str(self.id_ver_libro)