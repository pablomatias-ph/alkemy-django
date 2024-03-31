from django.urls import path
from .views import mostrar_producto

urlpatterns = [
    path('', mostrar_producto, name='mostrar_producto'),
]
