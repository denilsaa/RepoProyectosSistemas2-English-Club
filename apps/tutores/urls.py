from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_tutores, name='listar_tutores'),
]
