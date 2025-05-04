from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'activo', 'tipo_estudiante', 'tipo_inscripcion')
    search_fields = ('nombres', 'apellidos', 'ci', 'correo')
    list_filter = ('activo', 'tipo_estudiante', 'tipo_inscripcion')
