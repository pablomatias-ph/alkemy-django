from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Mostrar producto y detalles

def productoLista(request):
    productos = Producto.objects.all()
    return render(request, '../templates/producto_listas.html', {'productos': productos})

def productoDetalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, '../templates/producto_detalle.html', {'producto': producto})

# Crear un producto nuevo

def productoCreate(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        Producto.objects.create(
            nombre = nombre,
            descripcion = descripcion,
            precio = precio
        )
        return redirect('productoLista')
    return render(request, '../templates/producto_form.html')

# Hacer cambios en el producto

def productoUpdate(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.save()
        return redirect('productoLista')
    return render(request, '../templates/producto_form.html', {'producto': producto})

# Borrar productos

def productoBorrar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productoLista')
    return render(request, '../templates/producto_borrar.html', {'producto': producto})