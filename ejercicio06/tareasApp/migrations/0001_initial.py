# Generated by Django 5.0.3 on 2024-04-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloTarea', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('estadoFinalizada', models.BooleanField(default=False)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaFinalizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]