from django.urls import path
from .views import ClientesVistas, CrearContacto, BusquedaClienteAPI

urlpatterns = [
    path('clientes/', ClientesVistas.as_view(), name="lista_clientes"),
    path('cliente/<int:id>', ClientesVistas.as_view(), name="cliente"),
    path('contacto/', CrearContacto.as_view(), name='contacto'),
    path('contacto/<int:id>', CrearContacto.as_view(), name="listaContactos"),
    path('busqueda/<str:busqueda>/<int:id>', BusquedaClienteAPI.as_view(), name="busqueda")
]