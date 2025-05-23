from django.db import models
from apps.estudiantes.models import Estudiante
from apps.asignaturas.models import Asignatura
from apps.secretarias.models import Secretaria
from apps.directivos.models import Directivo

class Inscripcion(models.Model):
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, db_column='id_asignatura')
    id_secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, db_column='id_secretaria')
    id_directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE, db_column='id_directivo')
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'inscripcion'

    def __str__(self):
        return f"Inscripción de {self.id_estudiante} a {self.id_asignatura}"
