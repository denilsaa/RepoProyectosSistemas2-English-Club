from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)

    class Meta:
        db_table = 'asignatura'
