# Generated by Django 3.2.8 on 2022-06-12 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_alter_usuario_ciudad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='ciudad',
        ),
    ]