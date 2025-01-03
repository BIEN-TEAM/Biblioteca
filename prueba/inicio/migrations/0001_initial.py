# Generated by Django 3.2.4 on 2024-12-12 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, upload_to='profile_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='ComentarioContacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.TextField(verbose_name='asunto')),
                ('mensaje', models.TextField(verbose_name='comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'Comentario Contacto',
                'verbose_name_plural': 'Comentarios Contactos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Descargas',
            fields=[
                ('id_descarga', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de descarga: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Descarga',
                'verbose_name_plural': 'Descargas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id_grupo', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id_libro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=100, verbose_name='ISBN')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('año', models.DateField(verbose_name='Año de Publicación')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
                ('imagen', models.ImageField(upload_to='')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='libros/archivos/', verbose_name='Archivo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Ver_Libros',
            fields=[
                ('id_ver_libro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.libros', verbose_name='ID_Libro: ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID_Usuario')),
            ],
            options={
                'verbose_name': 'Ver Libro',
                'verbose_name_plural': 'Ver Libros',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Reseñas',
            fields=[
                ('id_reseña', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(verbose_name='Calificación')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to='inicio.libros', verbose_name='Libro')),
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
                ('id_libro_categoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID: ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.categorias', verbose_name='ID:')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.libros', verbose_name='Libros: ')),
            ],
        ),
        migrations.AddIndex(
            model_name='libros',
            index=models.Index(fields=['ISBN'], name='inicio_libr_ISBN_810b74_idx'),
        ),
        migrations.AddIndex(
            model_name='libros',
            index=models.Index(fields=['año'], name='inicio_libr_año_c7e410_idx'),
        ),
        migrations.AddIndex(
            model_name='libros',
            index=models.Index(fields=['autor'], name='inicio_libr_autor_1af898_idx'),
        ),
        migrations.AddField(
            model_name='descargas',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.libros', verbose_name='ID_Libro: '),
        ),
        migrations.AddField(
            model_name='descargas',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID_Usuario'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
