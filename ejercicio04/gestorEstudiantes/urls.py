from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarEstudiantes),
    path('create/<str:inputnombre>/<str:inputapellido>/<int:inputedad>/<int:inputnota>', views.altaEstudiante),
    path('filter', views.filtrarEdad),
    path('update/<int:id>', views.actualizarEstudiante),
    path('delete/<int:id>', views.borrarEstudiante),
    ]