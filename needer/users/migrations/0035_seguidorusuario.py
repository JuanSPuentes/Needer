# Generated by Django 4.0.9 on 2023-02-07 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_delete_seguidorusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeguidorUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_follow', models.DateTimeField(auto_now_add=True)),
                ('followed_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followed_id', to=settings.AUTH_USER_MODEL, verbose_name='Seguido')),
                ('follower_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_follower_id', to=settings.AUTH_USER_MODEL, verbose_name='Seguidor')),
            ],
        ),
    ]
