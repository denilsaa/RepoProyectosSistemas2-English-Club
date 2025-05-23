from django.shortcuts import render
from .models import Tutor

def listar_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'tutores/listar_tutores.html', {'tutores': tutores})
