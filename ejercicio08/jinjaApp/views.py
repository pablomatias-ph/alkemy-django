from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Ingreso

def controlEstudiantes(request):
    ruta = "d:/Alkemy/ejerciciosdjango/ejercicio08/jinjaApp/templates/controlEstudiantes.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

# Leer y filtrar

def listadoFilosofia(request):
    estudiante = [{'apellido': 'Alvarez', 'nombre': 'Damian', 'edad': 25, 'nota': 7},
                  {'apellido': 'Mercado', 'nombre': 'Sandra', 'edad': 19, 'nota': 9},
                  {'apellido': 'Linio', 'nombre': 'Martina', 'edad': 19, 'nota': 4},
                  {'apellido': 'Alcaraz', 'nombre': 'Luna', 'edad': 19, 'nota': 4},
                  {'apellido': 'Piccoli', 'nombre': 'Leandro', 'edad': 22, 'nota': 10},
                  {'apellido': 'Murielli', 'nombre': 'Ernestina', 'edad': 20, 'nota': 5},
                  {'apellido': 'Gimenez', 'nombre': 'Diego', 'edad': 19, 'nota': 10},
                  {'apellido': 'Benitez', 'nombre': 'Adrian', 'edad': 21, 'nota': 4},
                  {'apellido': 'Amant', 'nombre': 'Ivene', 'edad': 19, 'nota': 3},
                  {'apellido': 'Dandrea', 'nombre': 'Paz', 'edad': 19, 'nota': 3},
                  ]
    ruta = "D:/Alkemy/ejerciciosdjango/ejercicio08/jinjaApp/templates/listadoFilosofia.html"
    doc_extreno = open(ruta)
    plantilla = Template(doc_extreno.read())
    doc_extreno.close()
    contexto = Context({
        "estudiantes": estudiante
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def listadoReprobaron(request):
    estudiantes = [{'apellido': 'Alvarez', 'nombre': 'Damian', 'edad': 25, 'nota': 7},
                  {'apellido': 'Mercado', 'nombre': 'Sandra', 'edad': 19, 'nota': 9},
                  {'apellido': 'Linio', 'nombre': 'Martina', 'edad': 19, 'nota': 4},
                  {'apellido': 'Alcaraz', 'nombre': 'Luna', 'edad': 19, 'nota': 4},
                  {'apellido': 'Piccoli', 'nombre': 'Leandro', 'edad': 22, 'nota': 10},
                  {'apellido': 'Murielli', 'nombre': 'Ernestina', 'edad': 20, 'nota': 5},
                  {'apellido': 'Gimenez', 'nombre': 'Diego', 'edad': 19, 'nota': 10},
                  {'apellido': 'Benitez', 'nombre': 'Adrian', 'edad': 21, 'nota': 4},
                  {'apellido': 'Amant', 'nombre': 'Ivene', 'edad': 19, 'nota': 3},
                  {'apellido': 'Dandrea', 'nombre': 'Paz', 'edad': 19, 'nota': 3},
                  ]
    ruta = "D:/Alkemy/ejerciciosdjango/ejercicio08/jinjaApp/templates/listadoReprobaron.html"
    doc_extreno = open(ruta)
    plantilla = Template(doc_extreno.read())
    doc_extreno.close()
    contexto = Context({
        "estudiantes": estudiantes
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def listadoAprobaron(request):
    estudiantes = [{'apellido': 'Alvarez', 'nombre': 'Damian', 'edad': 25, 'nota': 7},
                  {'apellido': 'Mercado', 'nombre': 'Sandra', 'edad': 19, 'nota': 9},
                  {'apellido': 'Linio', 'nombre': 'Martina', 'edad': 19, 'nota': 4},
                  {'apellido': 'Alcaraz', 'nombre': 'Luna', 'edad': 19, 'nota': 4},
                  {'apellido': 'Piccoli', 'nombre': 'Leandro', 'edad': 22, 'nota': 10},
                  {'apellido': 'Murielli', 'nombre': 'Ernestina', 'edad': 20, 'nota': 5},
                  {'apellido': 'Gimenez', 'nombre': 'Diego', 'edad': 19, 'nota': 10},
                  {'apellido': 'Benitez', 'nombre': 'Adrian', 'edad': 21, 'nota': 4},
                  {'apellido': 'Amant', 'nombre': 'Ivene', 'edad': 19, 'nota': 3},
                  {'apellido': 'Dandrea', 'nombre': 'Paz', 'edad': 19, 'nota': 3},
                  ]
    ruta = "D:/Alkemy/ejerciciosdjango/ejercicio08/jinjaApp/templates/listadoAprobaron.html"
    doc_extreno = open(ruta)
    plantilla = Template(doc_extreno.read())
    doc_extreno.close()
    contexto = Context({
        "estudiantes": estudiantes
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)