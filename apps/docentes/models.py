from django.db import models
from apps.usuarios.models import Usuario
from apps.asignaturas.models import Asignatura

class Docente(models.Model):
    ci = models.CharField(unique=True, max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.CharField(unique=True, max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha_contrato = models.DateField()
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'docente'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class DocenteAsignatura(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, db_column='id_docente')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, db_column='id_asignatura')

    class Meta:
        db_table = 'docente_asignatura'
        unique_together = (('docente', 'asignatura'),)

    def __str__(self):
        return f"{self.docente} - {self.asignatura}"
