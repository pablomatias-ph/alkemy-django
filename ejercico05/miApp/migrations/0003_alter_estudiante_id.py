# Generated by Django 5.0.3 on 2024-04-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_alter_estudiante_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='Legajo'),
        ),
    ]