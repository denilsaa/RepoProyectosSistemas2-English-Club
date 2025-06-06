# Generated by Django 5.0.14 on 2025-05-19 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('asignatura', models.CharField(choices=[('Grammar', 'Grammar'), ('Reading', 'Reading'), ('Listening', 'Listening'), ('Writing', 'Writing'), ('Speaking', 'Speaking'), ('Responsibility', 'Responsibility'), ('Class Development', 'Class Development')], max_length=50)),
                ('gestion', models.CharField(max_length=10)),
                ('dias', models.CharField(max_length=50)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.personaladministrativo')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('modalidad', models.CharField(max_length=50)),
                ('medio_referencia', models.CharField(max_length=50)),
                ('motivo', models.CharField(max_length=200)),
                ('archivo_formulario', models.FileField(blank=True, null=True, upload_to='documentacion/inscripciones/')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiante')),
                ('inscrito_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.personaladministrativo')),
            ],
        ),
    ]
