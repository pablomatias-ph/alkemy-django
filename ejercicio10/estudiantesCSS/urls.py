from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.estudiantesCSS, name='estudiantesCSS'),
    path('listadoFilosofia', views.listadoFilosofia, name='listadoFilosofia'),
    path('listadoAprobaron', views.listadoAprobaron, name='listadoAprobaron'),
    path('listadoReprobaron', views.listadoReprobaron, name='listadoReprobaron'), 
    ]