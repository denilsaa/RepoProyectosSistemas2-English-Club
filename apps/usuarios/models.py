from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(unique=True, max_length=50)
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    ref_id = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuario'
