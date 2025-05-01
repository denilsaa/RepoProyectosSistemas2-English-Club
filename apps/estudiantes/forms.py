from django import forms
from datetime import date
from django.core.exceptions import ValidationError

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

OCUPACION_CHOICES = [
    ('universidad', 'Universidad'),
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

class EstudianteFormTecnico(forms.Form):
    ci = forms.CharField(max_length=20)
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(max_length=200)
    numero = forms.CharField(max_length=20)
    correo = forms.EmailField()
    colegio = forms.CharField(max_length=100, required=False)
    dias = forms.CharField(max_length=50, required=False)
    hora = forms.CharField(max_length=50, required=False)
    modalidad = forms.CharField(max_length=50, required=False)
    medio_referencia = forms.CharField(max_length=100, required=False)
    motivo_estudio = forms.ChoiceField(choices=MOTIVO_ESTUDIO_CHOICES, required=False)
    archivo_formulario = forms.FileField(required=False)
    ocupacion = forms.ChoiceField(choices=OCUPACION_CHOICES)
    tipo_estudiante = forms.ChoiceField(choices=TIPO_ESTUDIANTE_CHOICES, required=False)
    celular_referencia = forms.CharField(max_length=20, required=False)
    correo_referencia = forms.EmailField(required=False)
    estudios_ingles_previos = forms.CharField(widget=forms.Textarea, required=False)
    institucion_actual = forms.CharField(max_length=100, required=False)
    tipo_inscripcion = forms.ChoiceField(choices=TIPO_INSCRIPCION_CHOICES)
    forma_pago = forms.CharField(max_length=50, required=False)
    fecha_pago = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    clases_particulares = forms.BooleanField(required=False)
    material_entregado = forms.BooleanField(required=False)
    firmado = forms.BooleanField(required=False)
    recibido = forms.BooleanField(required=False)

    def clean_fecha_nacimiento(self):
        fnac = self.cleaned_data['fecha_nacimiento']
        hoy = date.today()
        edad = hoy.year - fnac.year - ((hoy.month, hoy.day) < (fnac.month, fnac.day))
        if edad < 4:
            raise ValidationError("El estudiante debe tener al menos 4 años.")
        return fnac

class EstudianteFormRegular(forms.Form):
    ci = forms.CharField(max_length=20)
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(max_length=200)
    numero = forms.CharField(max_length=20)
    correo = forms.EmailField()
    colegio = forms.CharField(max_length=100, required=False)
    grupo = forms.ChoiceField(choices=GRUPO_CHOICES, required=True)
    dias = forms.CharField(max_length=50, required=False)
    hora = forms.CharField(max_length=50, required=False)
    modalidad = forms.CharField(max_length=50, required=False)
    medio_referencia = forms.CharField(max_length=100, required=False)
    motivo_estudio = forms.ChoiceField(choices=MOTIVO_ESTUDIO_CHOICES, required=False)
    archivo_formulario = forms.FileField(required=False)
    tipo_estudiante = forms.ChoiceField(choices=TIPO_ESTUDIANTE_CHOICES, required=False)
    celular_referencia = forms.CharField(max_length=20, required=False)
    correo_referencia = forms.EmailField(required=False)
    estudios_ingles_previos = forms.CharField(widget=forms.Textarea, required=False)
    institucion_actual = forms.CharField(max_length=100, required=False)
    tipo_inscripcion = forms.ChoiceField(choices=TIPO_INSCRIPCION_CHOICES)
    forma_pago = forms.CharField(max_length=50, required=False)
    fecha_pago = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    clases_particulares = forms.BooleanField(required=False)
    material_entregado = forms.BooleanField(required=False)
    firmado = forms.BooleanField(required=False)
    recibido = forms.BooleanField(required=False)

    def clean_fecha_nacimiento(self):
        fnac = self.cleaned_data['fecha_nacimiento']
        hoy = date.today()
        edad = hoy.year - fnac.year - ((hoy.month, hoy.day) < (fnac.month, fnac.day))
        if edad < 4:
            raise ValidationError("El estudiante debe tener al menos 4 años.")
        return fnac
