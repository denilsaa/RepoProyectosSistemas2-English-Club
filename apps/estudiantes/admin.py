from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'activo', 'tipo_estudiante', 'tipo_inscripcion')
    search_fields = ('nombres', 'apellidos', 'ci', 'correo')
    list_filter = ('activo', 'tipo_estudiante', 'tipo_inscripcion')
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
