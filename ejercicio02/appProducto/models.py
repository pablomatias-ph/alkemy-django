from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return self.nombre