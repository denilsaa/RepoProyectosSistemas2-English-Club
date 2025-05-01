from django.contrib import admin
from .models import Asignatura

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nivel')
    search_fields = ('nombre', 'nivel')
    list_filter = ('nivel',)
