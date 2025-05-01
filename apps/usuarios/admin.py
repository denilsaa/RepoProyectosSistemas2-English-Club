from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_usuario', 'rol', 'fecha_creacion', 'activo')
    search_fields = ('nombre_usuario', 'rol')
    list_filter = ('rol', 'activo')
