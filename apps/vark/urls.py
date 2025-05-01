from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_varkresultados, name='listar_varkresultados'),
]
