# Generated by Django 3.1.1 on 2021-06-26 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "rubricas",
            "0007_resultadoapeevaluacion_resultadoapesemestre_resultadocompetenciaevaluacion_resultadocompetenciasemes",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ResultadoAPEEvaluacion",
            new_name="ResumenAPEEvaluacion",
        ),
        migrations.RenameModel(
            old_name="ResultadoAPESemestre",
            new_name="ResumenAPESemestre",
        ),
        migrations.RenameModel(
            old_name="ResultadoCompetenciaEvaluacion",
            new_name="ResumenCompetenciaEvaluacion",
        ),
        migrations.RenameModel(
            old_name="ResultadoCompetenciaSemestre",
            new_name="ResumenCompetenciaSemestre",
        ),
        migrations.RenameModel(
            old_name="ResultadoEstudianteSeccion",
            new_name="ResumenEstudianteSeccion",
        ),
    ]
