# Generated by Django 5.0.6 on 2024-11-20 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_alter_libros_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='descripción',
            field=models.CharField(default=1, max_length=50, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]
