from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida', views.hola_mundo, name='Bienvenida'),
    path('despedida', views.chau_mundo, name='Despedida'),
]