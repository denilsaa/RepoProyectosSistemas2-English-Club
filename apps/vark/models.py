from django.db import models
from apps.estudiantes.models import Estudiante

class VarkResultado(models.Model):
    id_estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    fecha_prueba = models.DateField()
    visual = models.FloatField()
    auditivo = models.FloatField()
    lectura = models.FloatField()
    kinestesico = models.FloatField()
    estilo_predominante = models.CharField(max_length=50)

    class Meta:
        db_table = 'vark_resultado'

    def __str__(self):
        return f"Resultado VARK de {self.id_estudiante}"
