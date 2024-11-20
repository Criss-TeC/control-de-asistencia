from django.db import models

# Create your models here.
class Ingles(models.MODEL):
    usuario = models.CharField(max_length=20)
    horas = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lenguaje(models.MODEL):
    usuario = models.CharField(max_length=20)
    horas = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
