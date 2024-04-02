from django.db import models
from django.core.validators import MaxValueValidator

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(validators=[MaxValueValidator(150)])
    nota = models.IntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.nombre
    