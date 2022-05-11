# Generated by Django 4.0.4 on 2022-05-11 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='num_documento',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Numero de documento'),
        ),
    ]