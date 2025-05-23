from django.shortcuts import render
from .models import Docente

def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/listar_docentes.html', {'docentes': docentes})
