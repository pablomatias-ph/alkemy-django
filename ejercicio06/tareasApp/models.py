from django.db import models

class Tareas(models.Model):
    tituloTarea = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    estadoFinalizada = models.BooleanField(default=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaFinalizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tituloTarea 