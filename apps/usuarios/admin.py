from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_usuario', 'rol', 'fecha_creacion', 'activo')
    search_fields = ('nombre_usuario', 'rol')
    list_filter = ('rol', 'activo')
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
