from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def testeoApp(request):
    ruta = "D:/Alkemy/ejerciciosdjango/ejercicio09/testeoApp/templates/index.html"
    doc_externo = open (ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)