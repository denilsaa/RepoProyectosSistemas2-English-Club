<<<<<<< HEAD
# Generated by Django 5.0.14 on 2025-05-19 16:16

import django.db.models.deletion
=======
# Generated by Django 5.0.14 on 2025-04-27 18:33

>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
<<<<<<< HEAD
                ('contrasena', models.CharField(max_length=255)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalAdministrativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('directivo', 'Directivo'), ('docente', 'Docente'), ('secretaria', 'Secretaria')], max_length=20)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('ci', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('archivo_documentacion', models.FileField(blank=True, null=True, upload_to='documentacion/personal/')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('ci', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
=======
                ('contrasena', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=50)),
                ('ref_id', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'usuario',
            },
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
        ),
    ]
