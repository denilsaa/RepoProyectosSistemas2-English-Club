
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
    ci = forms.CharField(max_length=20, label="CI")
    nombres = forms.CharField(max_length=100, label="Nombres")
    apellidos = forms.CharField(max_length=100, label="Apellidos")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de nacimiento")
    direccion = forms.CharField(max_length=200, label="Dirección")
    numero = forms.CharField(max_length=20, label="Teléfono")
    correo = forms.EmailField(label="Correo electrónico")
    colegio = forms.CharField(max_length=100, required=False, label="Colegio/Universidad")
    dias = forms.CharField(max_length=50, required=False, label="Días de asistencia")
    hora = forms.CharField(max_length=50, required=False, label="Hora de clase")
    modalidad = forms.CharField(max_length=50, required=False, label="Modalidad")
    medio_referencia = forms.CharField(max_length=100, required=False, label="¿Cómo se enteró?")
    motivo_estudio = forms.ChoiceField(choices=MOTIVO_ESTUDIO_CHOICES, required=False, label="Motivo para aprender inglés")
    archivo_formulario = forms.FileField(
        label="Adjuntar formulario escaneado (PDF o imagen)",
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf,.jpg,.jpeg,.png'})
    )
    ocupacion = forms.ChoiceField(choices=OCUPACION_CHOICES, label="Ocupación")
    tipo_estudiante = forms.ChoiceField(choices=TIPO_ESTUDIANTE_CHOICES, required=False, label="Tipo de estudiante")
    celular_referencia = forms.CharField(max_length=20, required=False, label="Celular de referencia")
    correo_referencia = forms.EmailField(required=False, label="Correo de referencia")
    estudios_ingles_previos = forms.CharField(widget=forms.Textarea, required=False, label="Estudios anteriores en inglés")
    institucion_actual = forms.CharField(max_length=100, required=False, label="Institución en la que estudia o trabaja")
    tipo_inscripcion = forms.ChoiceField(choices=TIPO_INSCRIPCION_CHOICES, label="Tipo de inscripción")
    forma_pago = forms.CharField(max_length=50, required=False, label="Forma de pago")
    fecha_pago = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label="Fecha de pago")
    clases_particulares = forms.BooleanField(required=False, label="¿Recibe clases particulares?")
    material_entregado = forms.BooleanField(required=False, label="¿Se entregó el material?")
    firmado = forms.BooleanField(required=False, label="Firmado")
    recibido = forms.BooleanField(required=False, label="Recibido")

    def clean_fecha_nacimiento(self):
        fnac = self.cleaned_data['fecha_nacimiento']
        hoy = date.today()
        edad = hoy.year - fnac.year - ((hoy.month, hoy.day) < (fnac.month, fnac.day))
        if edad < 4:
            raise ValidationError("El estudiante debe tener al menos 4 años.")
        return fnac

class EstudianteFormRegular(forms.Form):
    ci = forms.CharField(max_length=20, label="CI")
    nombres = forms.CharField(max_length=100, label="Nombres")
    apellidos = forms.CharField(max_length=100, label="Apellidos")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de nacimiento")
    direccion = forms.CharField(max_length=200, label="Dirección")
    numero = forms.CharField(max_length=20, label="Teléfono")
    correo = forms.EmailField(label="Correo electrónico")
    colegio = forms.CharField(max_length=100, required=False, label="Colegio")
    grupo = forms.ChoiceField(choices=GRUPO_CHOICES, required=True, label="Grupo")
    dias = forms.CharField(max_length=50, required=False, label="Días de asistencia")
    hora = forms.CharField(max_length=50, required=False, label="Hora de clase")
    modalidad = forms.CharField(max_length=50, required=False, label="Modalidad")
    medio_referencia = forms.CharField(max_length=100, required=False, label="¿Cómo se enteró?")
    motivo_estudio = forms.ChoiceField(choices=MOTIVO_ESTUDIO_CHOICES, required=False, label="Motivo para aprender inglés")
    archivo_formulario = forms.FileField(
        label="Adjuntar formulario escaneado (PDF o imagen)",
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf,.jpg,.jpeg,.png'})
    )
    tipo_estudiante = forms.ChoiceField(choices=TIPO_ESTUDIANTE_CHOICES, required=False, label="Tipo de estudiante")
    celular_referencia = forms.CharField(max_length=20, required=False, label="Celular de referencia")
    correo_referencia = forms.EmailField(required=False, label="Correo de referencia")
    estudios_ingles_previos = forms.CharField(widget=forms.Textarea, required=False, label="Estudios anteriores en inglés")
    institucion_actual = forms.CharField(max_length=100, required=False, label="Institución en la que estudia o trabaja")
    tipo_inscripcion = forms.ChoiceField(choices=TIPO_INSCRIPCION_CHOICES, label="Tipo de inscripción")
    forma_pago = forms.CharField(max_length=50, required=False, label="Forma de pago")
    fecha_pago = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label="Fecha de pago")
    clases_particulares = forms.BooleanField(required=False, label="¿Recibe clases particulares?")
    material_entregado = forms.BooleanField(required=False, label="¿Se entregó el material?")
    firmado = forms.BooleanField(required=False, label="Firmado")
    recibido = forms.BooleanField(required=False, label="Recibido")

    def clean_fecha_nacimiento(self):
        fnac = self.cleaned_data['fecha_nacimiento']
        hoy = date.today()
        edad = hoy.year - fnac.year - ((hoy.month, hoy.day) < (fnac.month, fnac.day))
        if edad < 4:
            raise ValidationError("El estudiante debe tener al menos 4 años.")
        return fnac

class TutorForm(forms.Form):
    ci = forms.CharField(max_length=20, label="CI del tutor")
    nombres = forms.CharField(max_length=100, label="Nombres del tutor")
    apellidos = forms.CharField(max_length=100, label="Apellidos del tutor")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de nacimiento")
    direccion = forms.CharField(max_length=200, label="Dirección")
    numero = forms.CharField(max_length=20, label="Teléfono")
    correo = forms.EmailField(label="Correo electrónico")
    ocupacion = forms.CharField(max_length=100, label="Ocupación")
    lugar_trabajo = forms.CharField(max_length=100, label="Lugar de trabajo")
    correo_trabajo = forms.EmailField(label="Correo de trabajo")
    parentesco = forms.CharField(max_length=50, label="Parentesco con el estudiante")
