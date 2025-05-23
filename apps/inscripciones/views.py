from django.shortcuts import render
from .models import Inscripcion

def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripciones/listar_inscripciones.html', {'inscripciones': inscripciones})
