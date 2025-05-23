from django.shortcuts import render
from .models import Asistencia

def listar_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencia/listar_asistencias.html', {'asistencias': asistencias})
