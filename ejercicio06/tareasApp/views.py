from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas

# Leer y filtrar

def listaTareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'listaTareas.html', {'tareas': tareas})

def detalleTareas(request, tarea_id):
    tarea = get_object_or_404(Tareas, id=tarea_id)
    return render(request, 'detalleTareas.html', {'tarea': tarea})

# Crear

def crearTareas(request):
    if request.method == 'POST':
        tituloTarea = request.POST.get('tituloTarea')
        descripcion = request.POST.get('descripcion')
        Tareas.objects.create(
            tituloTarea = tituloTarea,
            descripcion = descripcion
        )
        return redirect('listaTareas')
    return render(request, 'formularioTareas.html')

# Actualizar

def actualizarTarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, id=tarea_id)
    if request.method == 'POST':
        tituloTarea = request.POST.get('tituloTarea')
        descripcion = request.POST.get('descripcion')
        tarea.tituloTarea = tituloTarea
        tarea.descripcion = descripcion
        tarea.save()
        return redirect('listaTareas')
    return render(request, 'formularioTareas.html', {'tarea': tarea})

# Borrar

def borrarTarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, id=tarea_id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('listaTareas')
    return render(request, 'confirmacionBorrado.html', {'tarea': tarea})