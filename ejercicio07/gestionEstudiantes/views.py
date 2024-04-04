from .models import Estudiante
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Leer Estudiantes

# def listarEstudiantes(request):
#     estudiantes = Estudiante.objects.all()
#     return render(request, 'listaEstudiantes.html', {'estudiantes': estudiantes})

def listarEstudiantes(request):
    apellido = ['Alvarez', 'Belgrade', 'Suarez', 'Farabello']
    nota = 8, 9, 6, 8
    nombre = ['Pablo', 'Maria', 'Sara', 'Andrea']
    estudiantes = zip (nombre, apellido, nota)
    ruta = "D:/Alkemy/ejerciciosdjango/ejercicio07/gestionEstudiantes/templates/listaEstudiantesJinja.html"
    doc_extreno = open(ruta)
    plantilla = Template(doc_extreno.read())
    doc_extreno.close()
    contexto = Context({
        "estudiantes": estudiantes 
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)