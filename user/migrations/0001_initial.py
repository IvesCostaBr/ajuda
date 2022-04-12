# Generated by Django 4.0.4 on 2022-04-12 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cnpj', models.CharField(max_length=20, unique=True)),
                ('nome_completo', models.CharField(max_length=120)),
                ('data_nascimento', models.DateField()),
                ('data_criacao', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('user_system', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
