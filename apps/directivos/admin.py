from django.contrib import admin
from .models import Directivo

@admin.register(Directivo)
class DirectivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'cargo', 'activo')
    search_fields = ('nombres', 'apellidos', 'ci')
    list_filter = ('activo',)
