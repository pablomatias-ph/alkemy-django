from django.urls import path
from . import views

urlpatterns = [
    #path('', views.cargarUsuario),
    path('', views.mostrarUsuarios),
    path('create/<str:inputnombre>/<str:inputapellido>/<int:inputedad>', views.crearUsuario),
    path('filter/<int:edad>', views.filtrarUsuario),
    path('update/<int:id>', views.actualizarUsuario),
    path('delete/<int:id>', views.deleteUsuario),
    path('delete', views.deleteTodo), 
    path('json', views.ejemploJsonView),
]