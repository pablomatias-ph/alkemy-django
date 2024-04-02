from django.shortcuts import render, redirect
from .models import Usuario
from django.http import JsonResponse

# Crear usuarios

def crearUsuario(request, inputnombre, inputapellido ,inputedad):
    nuevoUsuario = Usuario.objects.create(
        nombre = inputnombre,
        apellido = inputapellido,
        edad = inputedad
    )
    nuevoUsuario.save()
    return render(request, 'usuarios.html', {'nuevoUsuario': nuevoUsuario})

# Leer y filtrar usuarios

def mostrarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'allUsers.html', {'usuarios': usuarios})

def filtrarUsuario(request, edad):
    datosFiltrados = Usuario.objects.filter(edad = edad)
    return render(request, 'usersFiltrados.html', {'datosFiltrados': datosFiltrados})

# Modificar datos de los usuarios

def actualizarUsuario(request, id):
    userActualizar = Usuario.objects.get(id=id)
    userActualizar.nombre = "Marcos"
    userActualizar.save()
    return render(request, 'updatedUser.html', {'updatedUser': userActualizar})

# Eliminar Usuario mediante ID

def deleteUsuario(request, id):
    userABorrar = Usuario.objects.get(id = id)
    userABorrar.delete()
    usuarios = Usuario.objects.all()
    return render(request, 'allUsers.html', {'usuarios': usuarios})

# Limpiar base borrando todos los datos

def deleteTodo(request):
    usuarios = Usuario.objects.all()
    usuarios.delete()
    return render(request, 'allUsers.html', {'usuarios': usuarios})

# Mostra un  JSON

def ejemploJsonView(request):
    data = list(Usuario.objects.values('nombre', 'apellido', 'edad'))
    return render(request, 'json.html', {'data': data})