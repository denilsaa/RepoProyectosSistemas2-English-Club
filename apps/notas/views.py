from django.shortcuts import render
from .models import Nota

def listar_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/listar_notas.html', {'notas': notas})
