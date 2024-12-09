# Generated by Django 5.0.6 on 2024-11-03 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id_grupo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del grupo')),
                ('privilegios', models.CharField(max_length=100, verbose_name='Privilegios')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('ISBN', models.CharField(max_length=100, verbose_name='ISBN: ')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre: ')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor: ')),
                ('año', models.DateField(verbose_name='Año: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Reseñas',
            fields=[
                ('id_reseña', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('calificacion', models.IntegerField(verbose_name='Calificación: ')),
                ('comentario', models.TextField(verbose_name='Comentario: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reseña',
                'verbose_name_plural': 'Reseñas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Libros_Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.libros', verbose_name='Libros: ')),
                ('id_libro_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.categorias', verbose_name='ID:')),
            ],
            options={
                'verbose_name': 'Libros Categorías',
                'verbose_name_plural': 'Libros Categorías',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre: ')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo electrónico: ')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.grupos', verbose_name='Grupo: ')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Descargas',
            fields=[
                ('id_descarga', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de descarga: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.libros', verbose_name='ID_Libro: ')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.usuarios', verbose_name='ID_Usuario')),
            ],
            options={
                'verbose_name': 'Descarga',
                'verbose_name_plural': 'Descargas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Ver_Libros',
            fields=[
                ('id_ver_libro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.libros', verbose_name='ID_Libro: ')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.usuarios', verbose_name='ID_Usuario')),
            ],
            options={
                'verbose_name': 'Ver Libro',
                'verbose_name_plural': 'Ver Libros',
                'ordering': ['-created'],
            },
        ),
    ]
