# Generated by Django 5.0.6 on 2024-11-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_alter_libros_año_libros_inicio_libr_isbn_810b74_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='imagen',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
