from django.shortcuts import render, redirect
from .models import Ingles, Lenguaje

# Create your views here.
def index (request):
    return render(request, 'index.html')

def registrar_ingles (request):
    if(request.method=='POST'):
        try:
            usuario =request.POST.get('usuario')
            horas =request.POST.get('horas')

            ingles = Ingles(
                usuario = usuario,
                horas = horas
            )
            ingles.save()
        except Exception as ex:
            print(f"error: {ex}")

    return redirect('index') 

def registrar_lenguaje (request):
    if(request.method=='POST'):
        try:
            usuario =request.POST.get('usuario')
            horas =request.POST.get('horas')

            ingles = Lenguaje(
                usuario = usuario,
                horas = horas
            )
            ingles.save()
        except Exception as ex:
            print(f"error: {ex}")
            
    return redirect('index') 