from django.shortcuts import render
from .models import VarkResultado

def listar_varkresultados(request):
    resultados = VarkResultado.objects.all()
    return render(request, 'vark/listar_varkresultados.html', {'resultados': resultados})
