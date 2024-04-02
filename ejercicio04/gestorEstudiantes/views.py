from django.shortcuts import render, redirect
from .models import Estudiante


# Alta Estudiante

def altaEstudiante(request, inputnombre, inputapellido ,inputedad, inputnota):
    nuevoEstudiante = Estudiante.objects.create(
        nombre = inputnombre,
        apellido = inputapellido,
        edad = inputedad,
        nota = inputnota
    )
    nuevoEstudiante.save()
    return render(request, 'nuevoEstudiante.html', {'nuevoEstudiante': nuevoEstudiante})

# Leer y filtrar Estudiantes

def listarEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'listaEstudiantes.html', {'estudiantes': estudiantes})

def filtrarEdad(request):
    filtradoEstudiantes = Estudiante.objects.filter(edad__gte=20)
    return render(request, 'filtradoEstudiante.html', {'filtradoEstudiantes': filtradoEstudiantes})

# Modificar nota Estudiante

def actualizarEstudiante(request, id):
    actualizarNota = Estudiante.objects.get(id=id)
    actualizarNota.nota = 8
    actualizarNota.save()
    return render(request, 'actualizarNota.html', {'actualizarNota': actualizarNota})

# Eliminar Estudiante mediante ID

def borrarEstudiante(request, id):
    borrarEstudiante = Estudiante.objects.get(id = id)
    borrarEstudiante.delete()
    estudiantes = Estudiante.objects.all()
    return render(request, 'listaEstudiantes.html', {'estudiantes': estudiantes})