# Generated by Django 4.0.4 on 2022-06-08 19:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_alter_publicacion_fecha_actualizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, max_length=280, verbose_name='Descripcion'),
        ),
    ]
