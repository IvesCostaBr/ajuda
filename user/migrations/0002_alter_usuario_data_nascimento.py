# Generated by Django 4.0.4 on 2022-04-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.CharField(max_length=40),
        ),
    ]
