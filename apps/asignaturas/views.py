from django.shortcuts import render
from .models import Asignatura

def listar_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignaturas/listar_asignaturas.html', {'asignaturas': asignaturas})
