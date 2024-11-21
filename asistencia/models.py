from django.db import models
from django.contrib.auth.models import User
# Create your models here.
""" class Ingles(models.Model):
    usuario = models.CharField(max_length=20)
    horas = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Lenguaje(models.Model):
    usuario = models.CharField(max_length=20)
    horas = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 """

from django.db import models
from django.contrib.auth.models import User


class Ingles(models.Model):
    fecha = models.DateField()  # Fecha de la asistencia
    horas_asistidas = models.PositiveIntegerField()  # Número de horas asistidas
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False
    )  # Usuario que registró las horas

    def __str__(self):
        return f"{self.fecha} - {self.horas_asistidas} horas"


class Lenguaje(models.Model):
    fecha = models.DateField()  # Fecha de la asistencia
    horas_asistidas = models.PositiveIntegerField()  # Número de horas asistidas
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False
    )  # Usuario que registró las horas

    def __str__(self):
        return f"{self.fecha} - {self.horas_asistidas} horas"
