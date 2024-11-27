from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Libros(models.Model):
    id_libro = models.AutoField(verbose_name="ID", primary_key=True)
    ISBN = models.CharField(max_length=100, verbose_name="ISBN")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    año = models.DateField(verbose_name="Año de Publicación")
    descripcion = models.CharField(max_length=50, verbose_name="Descripcion")
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-created"]
        indexes = [
            models.Index(fields=['ISBN']),
            models.Index(fields=['año']),
            models.Index(fields=['autor']),
        ]

    def __str__(self):
        return self.nombre

    def promedio_calificacion(self):
        return self.reseñas.aggregate(Avg('calificacion'))['calificacion__avg']


class Reseñas(models.Model):
    id_reseña = models.AutoField(verbose_name="ID", primary_key=True)
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE, related_name="reseñas", verbose_name="Libro")
    calificacion = models.IntegerField(verbose_name="Calificación")
    comentario = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ["-created"]

    def __str__(self):
        return f"Reseña de {self.libro.nombre} - {self.calificacion} estrellas"

    def clean(self):
        if not 1 <= self.calificacion <= 5:
            raise ValidationError("La calificación debe estar entre 1 y 5.")


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


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(verbose_name="ID: ", primary_key=True)  # Usar AutoField
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='profile_images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidos']

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


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
    
class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    asunto = models.TextField(verbose_name= "asunto")
    mensaje = models.TextField(verbose_name="comentario")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje
