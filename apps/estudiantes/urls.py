from django.urls import path
from . import views
from apps.estudiantes.views import dashboard_estudiante
##AGREGUE LA VISTA DE ESTUDIANTES 
urlpatterns = [
    path('crear/tecnico/', views.crear_estudiante_tecnico, name='crear_estudiante_tecnico'),
    path('crear/regular/', views.crear_estudiante_regular, name='crear_estudiante_regular'),
    path('crear/tutor/', views.crear_tutor, name='crear_tutor'),

    path('registrado/', views.estudiante_registrado, name='estudiante_registrado'),
    path('registrado/tutor/', views.estudiante_tutor_registrado, name='estudiante_tutor_registrado'),
    path('dashboard/estudiante/', dashboard_estudiante, name='dashboard_estudiante'),

]
