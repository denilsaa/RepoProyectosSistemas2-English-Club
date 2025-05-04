from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_docentes, name='listar_docentes'),
]
