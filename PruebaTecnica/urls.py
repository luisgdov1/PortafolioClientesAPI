"""PruebaTecnica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import logout_then_login, LoginView
from clientes.views import ListadoCliente, CrearCliente, DetalleCliente, EditarCliente, EliminarCliente
from webapp.views import exportarExcel

urlpatterns = [
    path('', LoginView.as_view(template_name='login/login.html'), name="login"),
    path('salida/', logout_then_login, name="logout"),
    path('admin/', admin.site.urls),
    path("inicio/", ListadoCliente.as_view(), name="inicio"),
    path("detalle_cliente/<int:pk>", DetalleCliente.as_view(), name="detalle"),
    path("nuevo_cliente", CrearCliente.as_view(), name="nuevo"),
    path("editar_cliente/<int:pk>", EditarCliente.as_view(), name="editar"),
    path("eliminar_cliente/<int:pk>", EliminarCliente.as_view(), name="eliminar"),
    path("descargarExcel/", exportarExcel, name="exportarExcel"),
    path("api/", include('webapp.urls')),
    path('accounts/login/', LoginView.as_view(template_name='login/login.html'), name="login")

]
