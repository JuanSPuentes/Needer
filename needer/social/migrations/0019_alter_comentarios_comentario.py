# Generated by Django 4.0.8 on 2022-10-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0018_alter_publicacion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(max_length=520, verbose_name='Comentario'),
        ),
    ]
