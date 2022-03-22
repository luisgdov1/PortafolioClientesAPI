from django.db import models

# Create your models here.
class Contacto (models.Model):
    nombre_Contacto = models.CharField(max_length=255)
    email_Contacto = models.CharField(max_length=255)
    telefono_Contacto= models.CharField(max_length=255)
    mensaje_Contacto = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email_contacto}'