from django.contrib import admin
from .models import Tutor, TieneTutor

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'correo', 'numero')
    search_fields = ('nombres', 'apellidos', 'ci')

@admin.register(TieneTutor)
class TieneTutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'tutor', 'parentesco')
    search_fields = ('estudiante__nombres', 'tutor__nombres')
