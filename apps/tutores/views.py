from django.shortcuts import render
from .models import Tutor
from django.db import connection

def listar_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'tutores/listar_tutores.html', {'tutores': tutores})

def dashboard_tutor(request):
    id_usuario = request.session.get('id_usuario')

    with connection.cursor() as cursor:
        # Obtener datos del tutor
        cursor.execute("""
            SELECT t.nombres, t.apellidos, t.correo
            FROM tutor t
            WHERE t.id_usuario = %s
        """, [id_usuario])
        tutor = cursor.fetchone()

        # Obtener estudiantes asociados
        cursor.execute("""
            SELECT e.nombres, e.apellidos, e.id
            FROM tiene_tutor tt
            JOIN estudiante e ON tt.id_estudiante = e.id
            JOIN tutor t ON tt.id_tutor = t.id
            WHERE t.id_usuario = %s
        """, [id_usuario])
        estudiantes = cursor.fetchall()

    context = {
        'tutor': tutor,
        'estudiantes': estudiantes
    }
    return render(request, 'dashboard_tutor.html', context)