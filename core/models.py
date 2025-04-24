from django.db import models
from pathlib import Path
from datetime import date

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)

    class Meta:
        db_table = 'asignatura'

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

class Usuario(models.Model):
    nombre_usuario = models.CharField(unique=True, max_length=50)
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    ref_id = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuario'


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
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, db_column='id_usuario', blank=True, null=True)

    # Nuevos campos para inscripción técnica y escolar
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



class Tutor(models.Model):
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, db_column='id_usuario', blank=True, null=True)
    ci = models.CharField(unique=True, max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    lugar_trabajo = models.CharField(max_length=100, blank=True, null=True)
    correo_trabajo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tutor'


class TieneTutor(models.Model):
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, db_column='id_estudiante')
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, db_column='id_tutor')
    parentesco = models.CharField(max_length=50)

    class Meta:
        db_table = 'tiene_tutor'
        unique_together = (('estudiante', 'tutor'),)


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
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'docente'


class Secretaria(models.Model):
    ci = models.CharField(unique=True, max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.CharField(unique=True, max_length=100)
    horario_trabajo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'secretaria'


class Directivo(models.Model):
    ci = models.CharField(unique=True, max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    correo = models.CharField(unique=True, max_length=100)
    cargo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'directivo'


class VarkResultado(models.Model):
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, db_column='id_estudiante')
    fecha_prueba = models.DateField()
    visual = models.FloatField()
    auditivo = models.FloatField()
    lectura = models.FloatField()
    kinestesico = models.FloatField()
    estilo_predominante = models.CharField(max_length=50)

    class Meta:
        db_table = 'vark_resultado'


class Inscripcion(models.Model):
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, db_column='id_estudiante')
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE, db_column='id_asignatura')
    secretaria = models.ForeignKey('Secretaria', on_delete=models.CASCADE, db_column='id_secretaria')
    directivo = models.ForeignKey('Directivo', on_delete=models.CASCADE, db_column='id_directivo')
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'inscripcion'


class Nota(models.Model):
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE, db_column='id_inscripcion')
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, db_column='id_docente')
    parcial1 = models.FloatField()
    parcial2 = models.FloatField()
    examen_final = models.FloatField()
    promedio = models.FloatField()

    class Meta:
        db_table = 'nota'


class Asistencia(models.Model):
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE, db_column='id_inscripcion')
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, db_column='id_docente')
    fecha = models.DateField()
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'asistencia'



class DocenteAsignatura(models.Model):
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, db_column='id_docente')
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE, db_column='id_asignatura')

    class Meta:
        db_table = 'docente_asignatura'
        unique_together = (('docente', 'asignatura'),)
