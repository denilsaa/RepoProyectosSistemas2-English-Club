
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Vistas del directivo
    path('directivo/dashboard/', views.dashboard_directivo, name='dashboard_directivo'),

    # Nuevas rutas para formularios separados
    path('directivo/registrar-estudiante-tecnico/', views.crear_estudiante_tecnico, name='crear_estudiante_tecnico'),
    path('directivo/registrar-estudiante-regular/', views.crear_estudiante_regular, name='crear_estudiante_regular'),
    path('directivo/crear-usuario/tutor/', views.crear_tutor, name='crear_tutor'),
    path('directivo/estudiante-registrado/', views.estudiante_registrado, name='estudiante_registrado'),
    path('directivo/estudiante-tutor-registrado/', views.estudiante_tutor_registrado, name='estudiante_tutor_registrado'),

]
