from django.db import models
from apps.usuarios.models import Usuario

class Secretaria(models.Model):
    ci = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    horario_trabajo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'secretaria'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
