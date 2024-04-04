from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaTareas, name='listaTareas'),
    path('templates/<int:tarea_id>/', views.detalleTareas, name='detalleTareas'),
    path('templates/create/', views.crearTareas, name='crearTareas'),
    path('templates/<int:tarea_id>/update/', views.actualizarTarea, name='actualizarTarea'),
    path('templates/<int:tarea_id>/delete/', views.borrarTarea, name='borrarTarea'),
]