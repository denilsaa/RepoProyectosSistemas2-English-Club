from django.urls import path
from . import views
from apps.tutores.views import dashboard_tutor
urlpatterns = [
    path('listar/', views.listar_tutores, name='listar_tutores'),
    path('dashboard/tutor/', views.dashboard_tutor, name='dashboard_tutor'),

]
