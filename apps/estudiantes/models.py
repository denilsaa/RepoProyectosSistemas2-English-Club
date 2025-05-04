from django.db import models
from apps.usuarios.models import Usuario

TIPO_INSCRIPCION_CHOICES = [
    ('anual', 'Anual'),
    ('vacacional', 'Vacacional'),
    ('particular', 'Clases particulares'),
    ('becado', 'Becado'),
]

TIPO_ESTUDIANTE_CHOICES = [
    ('normal', 'Normal'),
    ('profesional', 'Profesional'),
    ('independiente', 'Independiente'),
]

MOTIVO_ESTUDIO_CHOICES = [
    ('academico', 'Académico'),
    ('viaje', 'Viaje'),
    ('laboral', 'Laboral'),
]

GRUPO_CHOICES = [
    ('sweet', 'Sweet'),
    ('smart', 'Smart'),
    ('teens', 'Teens'),
    ('otro', 'Otro'),
]

class Estudiante(models.Model):
    ci = models.CharField(unique=True, max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.CharField(unique=True, max_length=100)
    colegio = models.CharField(max_length=100)
    grupo = models.CharField(max_length=20, choices=GRUPO_CHOICES, blank=True, null=True)
    dias = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=50)
    medio_referencia = models.CharField(max_length=100)
    motivo_estudio = models.CharField(max_length=20, choices=MOTIVO_ESTUDIO_CHOICES, blank=True, null=True)
    archivo_formulario = models.FileField(upload_to='formularios/', blank=True, null=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='id_usuario', blank=True, null=True)

    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    tipo_estudiante = models.CharField(max_length=20, choices=TIPO_ESTUDIANTE_CHOICES, blank=True, null=True)
    celular_referencia = models.CharField(max_length=20, blank=True, null=True)
    correo_referencia = models.CharField(max_length=100, blank=True, null=True)
    estudios_ingles_previos = models.TextField(blank=True, null=True)
    institucion_actual = models.CharField(max_length=100, blank=True, null=True)
    tipo_inscripcion = models.CharField(max_length=20, choices=TIPO_INSCRIPCION_CHOICES, default='anual')
    forma_pago = models.CharField(max_length=50, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    clases_particulares = models.BooleanField(default=False)
    material_entregado = models.BooleanField(default=False)
    firmado = models.BooleanField(default=False)
    recibido = models.BooleanField(default=False)

    class Meta:
        db_table = 'estudiante'
