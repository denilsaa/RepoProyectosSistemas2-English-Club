# apps/tutores/forms.py

from django import forms

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
