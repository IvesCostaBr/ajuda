# Generated by Django 4.0.4 on 2022-04-12 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usuario_data_nascimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='data_criacao',
        ),
    ]
