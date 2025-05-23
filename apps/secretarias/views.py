from django.shortcuts import render
from .models import Secretaria

def listar_secretarias(request):
    secretarias = Secretaria.objects.all()
    return render(request, 'secretarias/listar_secretarias.html', {'secretarias': secretarias})
