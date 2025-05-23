from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_notas, name='listar_notas'),
]
