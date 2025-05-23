from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
<<<<<<< HEAD
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
=======
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
]
