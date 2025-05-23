from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'estado', 'id_docente', 'id_inscripcion')
    search_fields = ('id_docente__nombres', 'id_inscripcion__estudiante__nombres')
    list_filter = ('estado',)
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
