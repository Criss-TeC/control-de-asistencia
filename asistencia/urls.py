from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:asignatura>/', views.asignatura_detalle, name='asignatura_detalle'),
    path('registrar-horas/', views.registrar_horas, name='registrar_horas'),
    path('dashboard/<str:asignatura>/actualizar/<int:registro_id>/', views.actualizar_horas, name='actualizar_horas'),
    path('dashboard/<str:asignatura>/eliminar/<int:registro_id>/', views.eliminar_horas, name='eliminar_horas'),
]

