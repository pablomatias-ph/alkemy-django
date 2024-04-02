from django.contrib import admin
from .models import Estudiante

class EstudianteAdministrador(admin.ModelAdmin):
    list_display = ["apellido", "nombre", "nota", "id", "mail"]
    search_fields = ["apellido", "nombre"]


admin.site.register(Estudiante, EstudianteAdministrador)