from django.db import models

# Create your models here.
class AgendaContacto(models.Model):  
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)  
    email = models.EmailField()  
    class Meta:  
        db_table = "agenda_contacto"
