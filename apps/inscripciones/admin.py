from django.contrib import admin
from .models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_estudiante', 'get_asignatura', 'get_secretaria', 'get_directivo', 'fecha_inscripcion', 'estado')
    search_fields = ('estudiante__nombres', 'estudiante__apellidos', 'asignatura__nombre')
    list_filter = ('estado',)

    @admin.display(description='Estudiante')
    def get_estudiante(self, obj):
        return f"{obj.estudiante.nombres} {obj.estudiante.apellidos}"

    @admin.display(description='Asignatura')
    def get_asignatura(self, obj):
        return obj.asignatura.nombre

    @admin.display(description='Secretaria')
    def get_secretaria(self, obj):
        return f"{obj.secretaria.nombres} {obj.secretaria.apellidos}"

    @admin.display(description='Directivo')
    def get_directivo(self, obj):
        return f"{obj.directivo.nombres} {obj.directivo.apellidos}"
