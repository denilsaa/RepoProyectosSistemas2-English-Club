from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_inscripciones, name='listar_inscripciones'),
]
