from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_asignaturas, name='listar_asignaturas'),
]
