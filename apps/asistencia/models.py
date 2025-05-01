from django.db import models
from apps.docentes.models import Docente
from apps.inscripciones.models import Inscripcion

class Asistencia(models.Model):
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, db_column='id_inscripcion')
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, db_column='id_docente')
    fecha = models.DateField()
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'asistencia'

    def __str__(self):
        return f"Asistencia {self.id} - {self.fecha}"
