from django.forms import ModelForm, EmailInput, TextInput
from clientes.models import Clientes

class ClienteForma(ModelForm):
    class Meta:
        model =  Clientes
        fields = '__all__'
        widgets = {
            'email_Cliente': EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
            'nombre_Cliente': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nombre' }),
            'telefono_Cliente': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Telefono'}),
            'direccion_Cliente': TextInput(attrs={'type': 'text', 'class': 'form-control ', 'placeholder': 'Direccion' })
        }
