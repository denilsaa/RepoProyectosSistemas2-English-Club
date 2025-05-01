from django.db import models
from apps.usuarios.models import Usuario
from apps.estudiantes.models import Estudiante

class Tutor(models.Model):
    ci = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.EmailField()
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    lugar_trabajo = models.CharField(max_length=100, blank=True, null=True)
    correo_trabajo = models.EmailField(blank=True, null=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='id_usuario', blank=True, null=True)

    class Meta:
        db_table = 'tutor'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class TieneTutor(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, db_column='id_tutor')
    parentesco = models.CharField(max_length=50)

    class Meta:
        db_table = 'tiene_tutor'
        unique_together = (('estudiante', 'tutor'),)

    def __str__(self):
        return f"{self.estudiante} - {self.tutor}"
