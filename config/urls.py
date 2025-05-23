"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.publico.urls')),
    path('', include('apps.usuarios.urls.directivo')),
    path('', include('apps.estudiantes.urls.tecnico')),
    path('', include('apps.estudiantes.urls.regular')),
    path('cursos/', include('apps.cursos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

urlpatterns = [
    path('admin/', admin.site.urls),

    # Público (inicio, quienes somos, servicios, contacto)
    path('', include('apps.publico.urls')),  

    # Usuarios (login, logout, dashboard directivo)
    path('usuarios/', include('apps.usuarios.urls')),

    # Demás apps internas
    path('asignaturas/', include('apps.asignaturas.urls')),
    path('estudiantes/', include('apps.estudiantes.urls')),
    path('tutores/', include('apps.tutores.urls')),
    path('docentes/', include('apps.docentes.urls')),
    path('secretarias/', include('apps.secretarias.urls')),
    path('directivos/', include('apps.directivos.urls')),
    path('inscripciones/', include('apps.inscripciones.urls')),
    path('notas/', include('apps.notas.urls')),
    path('asistencia/', include('apps.asistencia.urls')),
    path('vark/', include('apps.vark.urls')),
]
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
