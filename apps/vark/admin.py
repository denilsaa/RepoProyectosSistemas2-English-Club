from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import VarkResultado

@admin.register(VarkResultado)
class VarkResultadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_estudiante', 'fecha_prueba', 'estilo_predominante')
    search_fields = ('id_estudiante__nombres', 'estilo_predominante')
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
