from django.contrib import admin
from .models import Secretaria

@admin.register(Secretaria)
class SecretariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'activo')
    search_fields = ('nombres', 'apellidos', 'ci')
    list_filter = ('activo',)
