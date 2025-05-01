from django.db import models
from apps.usuarios.models import Usuario

class Estudiante(models.Model):
    ci = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    correo = models.EmailField()
    colegio = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    dias = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=50)
    medio_referencia = models.CharField(max_length=50)
    motivo_estudio = models.CharField(max_length=100)
    archivo_formulario = models.FileField(upload_to='formularios/', null=True, blank=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class TieneTutor(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tutor = models.ForeignKey('tutores.Tutor', on_delete=models.CASCADE)
