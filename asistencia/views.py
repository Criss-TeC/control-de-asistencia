from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingles, Lenguaje
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
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
    if asignatura == "Ingles":
        modelo = Ingles
    elif asignatura == "Lenguaje":
        modelo = Lenguaje
    else:
        return redirect('dashboard')

    es_lider = request.user.groups.filter(name="Lider").exists()

    if es_lider:
        registros = modelo.objects.all().order_by('usuario__username','fecha')
    else:
        registros = modelo.objects.filter(usuario=request.user).order_by('fecha')

    total_horas = sum(registro.horas_asistidas for registro in registros)

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
@permission_required('asistencia.add_ingles', login_url='/')
def registrar_horas(request):

    es_lider = request.user.groups.filter(name="Lider").exists()
    if es_lider:
        usuarios = User.objects.all()

    else:
        usuarios = None

    try:
        if (request.method == 'POST'):
            asignatura_id = request.POST.get('asignatura')
            fecha = request.POST.get('fecha')
            horas = int(request.POST.get('horas'))
            if es_lider:
                usuario_id = request.POST.get("usuario")
            else:
                usuario_id = request.user.id

            if asignatura_id == '1':  # Ingles
                ingles = Ingles(
                    fecha=fecha,
                    horas_asistidas=horas,
                    usuario_id=usuario_id
                )
                ingles.save()

            elif asignatura_id == '2':  # Lenguaje
                lenguaje = Lenguaje(
                    fecha=fecha,
                    horas_asistidas=horas,
                    usuario_id=usuario_id
                )
                lenguaje.save()

            messages.success(request, "Horas registradas exitosamente.")
            return redirect('dashboard')
    except Exception as ex:
        print(f"error: {ex}")

    asignaturas = [
        {"id": 1, "nombre": "Ingles"},
        {"id": 2, "nombre": "Lenguaje"}
    ]
    return render(request, 'registrar_horas.html', {'asignaturas': asignaturas, "usuarios": usuarios, "es_lider": es_lider})


@login_required
@permission_required('asistencia.change_ingles', login_url='/')
def actualizar_horas(request, asignatura, registro_id):
    try:

        if asignatura == "Ingles":
            modelo = Ingles
        elif asignatura == "Lenguaje":
            modelo = Lenguaje
        registro = get_object_or_404(modelo, id=registro_id)

        if (request.method == "POST"):
            registro.fecha = request.POST.get('fecha')
            registro.horas_asistidas = int(request.POST.get('horas'))
            registro.save()
            return redirect('asignatura_detalle', asignatura=asignatura)

        registro.fecha = registro.fecha.strftime('%Y-%m-%d')
        return render(request, 'actualizar_horas.html', {'registro': registro, 'asignatura': asignatura})
    except Exception as ex:
        print(f"error: {ex}")
        return redirect('dashboard')


@login_required
@permission_required('asistencia.delete_ingles', login_url='/')
def eliminar_horas(request, asignatura, registro_id):
    try:
        if asignatura == "Ingles":
            modelo = Ingles
        elif asignatura == "Lenguaje":
            modelo = Lenguaje
        registro = get_object_or_404(modelo, id=registro_id)

        if request.method == "POST":
            registro.delete()
    except Exception as ex:
        print(f"error: {ex}")
    return redirect('asignatura_detalle', asignatura=asignatura)
