from django.shortcuts import render
from .models import Directivo

def listar_directivos(request):
    directivos = Directivo.objects.all()
    return render(request, 'directivos/listar_directivos.html', {'directivos': directivos})
