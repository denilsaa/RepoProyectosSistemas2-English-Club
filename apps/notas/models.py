from django.db import models
from apps.docentes.models import Docente
from apps.inscripciones.models import Inscripcion

class Nota(models.Model):
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, db_column='id_inscripcion')
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, db_column='id_docente')
    parcial1 = models.FloatField()
    parcial2 = models.FloatField()
    examen_final = models.FloatField()
    promedio = models.FloatField()

    class Meta:
        db_table = 'nota'

    def __str__(self):
        return f"Notas de {self.id_inscripcion} por {self.id_docente}"
