from django.db import models
from django.core.validators import MaxValueValidator

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(validators=[MaxValueValidator(150)])
    
    def __str__(self):
        return self.nombre
