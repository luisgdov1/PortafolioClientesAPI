from django.contrib import messages
from clientes.models import Clientes
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from rest_framework import  viewsets
from webapp.serializers import  ClientesSerializer

#Clases del CRUD
class ListadoCliente(ListView):
    model = Clientes
    template_name = "index.html"
    context_object_name = "clientes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_visits'] = self.request.session['num_visits']
        return context

    def get(self, request, *args, **kwargs):
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return super().get(request, *args, **kwargs)

class CrearCliente(CreateView):
    model = Clientes
    template_name = "CRUD_Operaciones/Agregar.html"
    fields = ('nombre_Cliente', 'direccion_Cliente', 'email_Cliente', 'telefono_Cliente',)

    def get_success_url(self):
        messages.info(self.request, "Cliente " + self.request.POST['nombre_Cliente'] + " ha sido agregado con exito")
        return reverse_lazy('nuevo')

class DetalleCliente(DetailView):
    model = Clientes
    template_name = "CRUD_Operaciones/Detalle.html"
    context_object_name = "Cliente"

class EditarCliente(UpdateView):
    model = Clientes
    template_name = 'CRUD_Operaciones/Editar.html'
    context_object_name = 'formaCliente'
    fields = ('nombre_Cliente', 'direccion_Cliente', 'email_Cliente', 'telefono_Cliente',)

    def get_success_url(self):
        messages.info(self.request, "Cliente " + self.request.POST['nombre_Cliente'] + " se ha editado con exito")
        return reverse_lazy('detalle', kwargs={'pk': self.object.id})

class EliminarCliente(DeleteView):
    model = Clientes
    template_name = 'index.html'
    context_object_name = "eliminar"
    def get_success_url(self):
        myvar = self.request.POST.get('nombre_Cliente', 'eliminado')
        messages.info(self.request, "Cliente " + myvar + " se ha eliminado con exito")
        return reverse_lazy("inicio")

''' OTRO TIPO DE API
class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = ClientesSerializer
    queryset = Clientes.objects.all()
'''
'''
def detalleCliente(request, idCliente):
    cliente = get_object_or_404(Clientes, pk=idCliente)
    return render(request, 'CRUD_Operaciones/Detalle.html', {'Cliente': cliente})

def nuevoCliente(request):
    if request.method=="POST":
        formaCliente = ClienteForma(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            messages.info(request, "Cliente " + request.POST['nombre_Cliente'] + " creado exitosamente")
            return redirect('nuevo')
    else:
        formaCliente = ClienteForma()
    return render(request, 'CRUD_Operaciones/Agregar.html', {'formaCliente': formaCliente})

def editarCliente(request, idCliente):
    cliente = get_object_or_404(Clientes, pk=idCliente)
    if request.method == "POST":
        formaCliente = ClienteForma(request.POST, instance=cliente)
        if formaCliente.is_valid():
            formaCliente.save()
            messages.info(request, "Cambios realizados con exito en  " + request.POST['nombre_Cliente'])
            return redirect("inicio")
    else:
        formaCliente = ClienteForma(instance=cliente)
    return render(request, 'CRUD_Operaciones/Editar.html', {'formaCliente': formaCliente})

def eliminarCliente(request, idCliente):
    clientes = get_object_or_404(Clientes, pk=idCliente)
    if clientes:
        messages.info(request, f'Cliente {clientes.nombre_Cliente} eliminado')
        clientes.delete()
    return redirect("inicio")
'''