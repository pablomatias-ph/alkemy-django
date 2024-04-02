from django.db import models
from django.core.validators import MaxValueValidator

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Legajo")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(validators=[MaxValueValidator(150)])
    nota = models.IntegerField(validators=[MaxValueValidator(10)])
    mail = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.nombre 