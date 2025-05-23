from django.contrib import admin
from .models import Docente, DocenteAsignatura
from apps.asignaturas.models import Asignatura

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'especialidad', 'activo')
    search_fields = ('nombres', 'apellidos', 'ci')
    list_filter = ('activo',)

@admin.register(DocenteAsignatura)
class DocenteAsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'docente', 'asignatura')
    search_fields = ('docente__nombres', 'asignatura__nombre')
