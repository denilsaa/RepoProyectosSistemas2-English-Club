# Generated by Django 5.0.14 on 2025-05-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_curso_dias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='medio_referencia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='motivo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
