from django.urls import path
from . import views

urlpatterns = [
    path('', views.productoLista, name='productoLista'), 
    path('templates/<int:producto_id>/', views.productoDetalle, name='productoDetalle'), 
    path('templates/create/', views.productoCreate, name='productoCreate'), 
    path('templates/<int:producto_id>/update/', views.productoUpdate, name='productoUpdate'), 
    path('templates/<int:producto_id>/delete/', views.productoBorrar, name='productoBorrar'), 

]
