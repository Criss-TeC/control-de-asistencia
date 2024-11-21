from django.shortcuts import render, redirect,get_object_or_404
from .models import Ingles, Lenguaje
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index (request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    asignaturas = [
        {"nombre": "Ingles", "url": "Ingles_detalle"},
        {"nombre": "Lenguaje", "url": "Lenguaje_detalle"},
    ]
    return render(request, 'dashboard.html', {'asignaturas': asignaturas})

@login_required
def asignatura_detalle(request, asignatura):
    modelo = Ingles if asignatura == "Ingles" else Lenguaje
    
    es_lider = request.user.groups.filter(name="Lider").exists()
    
    if es_lider:
        registros = modelo.objects.all()
    else:
        registros = modelo.objects.filter(registrado_por=request.user)
        
    total_horas = sum(registro.horas_asistidas for registro in registros)
    
    permisos_actualizar = request.user.has_perm('asistencia.change_lenguaje') or request.user.has_perm('asistencia.change_ingles')
    permisos_eliminar = request.user.has_perm('asistencia.delete_lenguaje') or request.user.has_perm('asistencia.delete_ingles')


    return render(
        request,
        'detalle.html',
        {
            'registros': registros,
            'total_horas': total_horas,
            'asignatura': asignatura.capitalize(),
            'es_lider': es_lider,
            }
        )


@login_required
@permission_required('asistencia.add_ingles', raise_exception=False)
def registrar_horas(request):
    es_lider = request.user.groups.filter(name="Lider").exists()
    usuarios = User.objects.all() if es_lider else None
    
    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura')  # Usar get para evitar KeyError
        fecha = request.POST.get('fecha')
        horas = int(request.POST.get('horas'))
        registrado_por_id = request.POST.get("registrado_por") if es_lider else request.user.id

        
        if asignatura_id == '1':  # Ingles
            Ingles.objects.create(fecha=fecha, horas_asistidas=horas, registrado_por_id=registrado_por_id)
        elif asignatura_id == '2':  # Lenguaje
            Lenguaje.objects.create(fecha=fecha, horas_asistidas=horas, registrado_por_id=registrado_por_id)

        messages.success(request, "Horas registradas exitosamente.")
        return redirect('dashboard')

    asignaturas = [
        {"id": 1, "nombre": "Ingles"},
        {"id": 2, "nombre": "Lenguaje"}
    ]
    return render(request, 'registrar_horas.html', {'asignaturas': asignaturas, "usuarios": usuarios, "es_lider": es_lider})

@login_required
def actualizar_horas(request, asignatura, registro_id):
    # Obtener el registro según la asignatura
    modelo = Ingles if asignatura == "Ingles" else Lenguaje
    registro = get_object_or_404(modelo, id=registro_id)

    if request.method == "POST":
        registro.fecha = request.POST.get('fecha')
        registro.horas_asistidas = int(request.POST.get('horas'))
        registro.save()
        return redirect('asignatura_detalle', asignatura=asignatura)

    registro.fecha = registro.fecha.strftime('%Y-%m-%d')
    return render(request, 'actualizar_horas.html', {'registro': registro, 'asignatura': asignatura})

@login_required
def eliminar_horas(request, asignatura, registro_id):
    # Obtener el registro según la asignatura
    modelo = Ingles if asignatura == "Ingles" else Lenguaje
    registro = get_object_or_404(modelo, id=registro_id)

    if request.method == "POST":
        registro.delete()
        return redirect('asignatura_detalle', asignatura=asignatura)
    
    

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