from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'estado', 'id_docente', 'id_inscripcion')
    search_fields = ('id_docente__nombres', 'id_inscripcion__estudiante__nombres')
    list_filter = ('estado',)
