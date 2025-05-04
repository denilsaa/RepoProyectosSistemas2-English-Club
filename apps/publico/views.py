from django.shortcuts import render

def inicio(request):
    return render(request, 'publico/inicio.html')

def quienes_somos(request):
    return render(request, 'publico/quienes_somos.html')

def servicios(request):
    return render(request, 'publico/servicios.html')

def contacto(request):
    return render(request, 'publico/contacto.html')
