# Generated by Django 3.2.9 on 2022-06-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=12)),
                ('telefono', models.FloatField()),
                ('correo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=3)),
            ],
        ),
    ]
