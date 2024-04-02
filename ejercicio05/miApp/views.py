from django.shortcuts import render, redirect
from .models import Estudiante

def listarEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})