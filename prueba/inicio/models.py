from django.db import models
from ckeditor.fields import RichTextField

class Grupos (models.Model):
    id_grupo = models.IntegerField(max_length=10000, verbose_name="ID", primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del grupo")
    privilegios = models.CharField(max_length=100, verbose_name="Privilegios")


    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ["-created"]

    def __str__(self):
        return self.privilegios
    

class Reseñas(models.Model):
    id_reseña = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    calificacion = models.IntegerField(max_length=1000, verbose_name="Calificación: ")
    comentario = models.TextField(verbose_name="Comentario: ")

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ["-created"]

    def __str__(self):
        return self.comentario
    
class Libros(models.Model):
    id_libro = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    ISBN = models.CharField(max_length=100, verbose_name="ISBN: ")
    nombre = models.CharField(max_length=100, verbose_name="Nombre: ")
    autor = models.CharField(max_length=100, verbose_name="Autor: ")
    año = models.DateField(max_length=100, verbose_name="Año: ")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
    
class Usuarios(models.Model):
    id_usuario = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, verbose_name="Grupo: ")
    nombre = models.CharField(max_length=100, verbose_name="Nombre: "),
    email = models.EmailField(max_length=100, verbose_name="Correo electrónico: ")
    contraseña = models.CharField(max_length=100, verbose_name="Contraseña: ")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    id_categoria = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre: ")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre


class Libros_Categorias(models.Model):
    id_categoria = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    id_libro= models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name="Libros: ")
    id_libro_categoria=models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="ID:")

    class Meta:
        verbose_name = "Libros Categorías"
        verbose_name_plural = "Libros Categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.id_categoria 

class Descargas(models.Model):
    id_descarga = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    id_libro = models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name="ID_Libro: ")
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="ID_Usuario")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de descarga: ")

    class Meta:
        verbose_name = "Descarga"
        verbose_name_plural = "Descargas"
        ordering = ["-created"]

    def __str__(self):
        return self.id_descarga
class Ver_Libros(models.Model):
    id_ver_libro = models.IntegerField(max_length=10000, verbose_name="ID: ", primary_key=True)
    id_libro = models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name="ID_Libro: ")
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="ID_Usuario")
    fecha = models.DateField(auto_now_add=True)


