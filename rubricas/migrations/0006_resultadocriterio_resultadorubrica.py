# Generated by Django 3.1.1 on 2021-06-26 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rubricas", "0005_administrador_coordinador_estudiante_externo_monitor_profesor_registro_usuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResultadoRubrica",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("comentario", models.TextField(blank=True)),
                ("resultado", models.FloatField(default=0)),
                ("puntos", models.IntegerField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                (
                    "estudiante",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resultados",
                        to="rubricas.estudiante",
                    ),
                ),
                (
                    "evaluador",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="evaluados",
                        to="rubricas.usuario",
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
            name="ResultadoCriterio",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("comentario", models.TextField(blank=True)),
                ("puntos", models.IntegerField(default=0)),
                ("ultima_modificacion", models.DateTimeField(auto_now_add=True)),
                (
                    "criterio",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.criterio"),
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
                (
                    "nivel",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.nivelcriterio"
                    ),
                ),
                (
                    "resultado_rubrica",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.resultadorubrica"
                    ),
                ),
            ],
        ),
    ]
