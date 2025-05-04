from django.contrib import admin
from .models import Nota

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_docente', 'get_inscripcion', 'parcial1', 'parcial2', 'examen_final', 'promedio')
    search_fields = ('docente__nombres', 'inscripcion__estudiante__nombres')
    list_filter = ()

    @admin.display(description='Docente')
    def get_docente(self, obj):
        return f"{obj.docente.nombres} {obj.docente.apellidos}"

    @admin.display(description='Inscripcion')
    def get_inscripcion(self, obj):
        return obj.inscripcion.id
