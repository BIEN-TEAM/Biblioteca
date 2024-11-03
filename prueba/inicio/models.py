from django.db import models
from ckeditor.fields import RichTextField

#Modelos hechos por Erick
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
  