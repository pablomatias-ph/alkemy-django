from django.shortcuts import render
from .models import Producto

def mostrar_producto(request):
    nombre = "Producto de prueba"
    descripcion = "La descripcion del producto de prueba"
    precio = 98653
    producto = Producto.objects.create(
        nombre = nombre,
        descripcion = descripcion,
        precio = precio
    )
    return render(request, 'producto.html', {'producto': producto})
