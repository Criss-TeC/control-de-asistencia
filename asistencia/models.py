from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ingles(models.Model):
    fecha = models.DateField()  # Fecha
    horas_asistidas = models.PositiveIntegerField()  # horas asistidas
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False
    )  # Usuario

class Lenguaje(models.Model):
    fecha = models.DateField()  # Fecha
    horas_asistidas = models.PositiveIntegerField()  # horas asistidas
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False
    )  # Usuario