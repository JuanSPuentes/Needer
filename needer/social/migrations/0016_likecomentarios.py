# Generated by Django 4.0.4 on 2022-10-08 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0015_alter_likedpublicacion_id_publicacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Like')),
                ('id_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.publicacion', verbose_name='Publicacion')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
