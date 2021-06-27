# Generated by Django 3.1.1 on 2021-06-26 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rubricas", "0006_resultadocriterio_resultadorubrica"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResultadoEstudianteSeccion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("resultado", models.FloatField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                (
                    "estudiante",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.estudiante"
                    ),
                ),
                (
                    "seccion",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.seccion"),
                ),
                (
                    "ultimo_resultado",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.resultadorubrica"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResultadoCompetenciaSemestre",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("semestre", models.CharField(max_length=20)),
                ("resultado", models.FloatField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                (
                    "competencia",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.competencia"
                    ),
                ),
                (
                    "estudiante",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.estudiante"
                    ),
                ),
                ("secciones", models.ManyToManyField(to="rubricas.Seccion")),
            ],
        ),
        migrations.CreateModel(
            name="ResultadoCompetenciaEvaluacion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("resultado", models.FloatField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                (
                    "competencia",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.competencia"
                    ),
                ),
                (
                    "estudiante",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.estudiante"
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.itemcalificacionseccion"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResultadoAPESemestre",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("semestre", models.CharField(max_length=20)),
                ("resultado", models.FloatField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                ("ape", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.ape")),
                (
                    "estudiante",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.estudiante"
                    ),
                ),
                ("secciones", models.ManyToManyField(to="rubricas.Seccion")),
            ],
        ),
        migrations.CreateModel(
            name="ResultadoAPEEvaluacion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("resultado", models.FloatField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                ("ape", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.ape")),
                (
                    "estudiante",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.estudiante"
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.itemcalificacionseccion"
                    ),
                ),
            ],
        ),
    ]