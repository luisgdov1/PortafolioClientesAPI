from django.forms import ModelForm, EmailInput, TextInput
from webapp.models import Contacto

class ContactoForma(ModelForm):
    class Meta:
        model =  Contacto
        fields = '__all__'
        widgets = {
            'email_Contacto': EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
            'nombre_Contacto': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nombre' }),
            'telefono_Contacto': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Telefono'}),
            'mensaje_Contacto': TextInput(attrs={'type': 'text', 'class': 'form-control ', 'placeholder': 'Mensaje' })
        }
