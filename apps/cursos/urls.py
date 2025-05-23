from django.urls import path
from apps.cursos.views import curso

urlpatterns = [
    path('', curso.listar_cursos, name='listar_cursos'),
    path('crear/', curso.crear_curso, name='crear_curso'),
    path('editar/<int:pk>/', curso.editar_curso, name='editar_curso'),
    path('eliminar/<int:pk>/', curso.eliminar_curso, name='eliminar_curso'),
]
