from django.contrib import admin
from .models import VarkResultado

@admin.register(VarkResultado)
class VarkResultadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_estudiante', 'fecha_prueba', 'estilo_predominante')
    search_fields = ('id_estudiante__nombres', 'estilo_predominante')
