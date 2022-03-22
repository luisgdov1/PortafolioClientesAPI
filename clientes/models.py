from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre_Cliente = models.CharField(max_length=255)
    direccion_Cliente = models.CharField(max_length=255)
    email_Cliente = models.CharField(max_length=255)
    telefono_Cliente = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre_Cliente}'