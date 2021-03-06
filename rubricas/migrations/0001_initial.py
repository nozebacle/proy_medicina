# Generated by Django 3.1.1 on 2021-04-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="APE",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre_corto", models.CharField(max_length=120, unique=True)),
                ("nombre_largo", models.TextField()),
                ("sigla", models.CharField(max_length=15, unique=True)),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="CapituloProcedimientos",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("nombre", models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Competencia",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=220, unique=True)),
                ("sigla", models.CharField(max_length=15, unique=True)),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Criterio",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre_interno", models.CharField(max_length=120)),
                ("descripcion", models.TextField()),
                ("numero", models.IntegerField()),
                ("apes", models.ManyToManyField(null=True, to="rubricas.APE")),
                ("competencias", models.ManyToManyField(null=True, to="rubricas.Competencia")),
            ],
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120)),
                ("nombre_interno", models.CharField(max_length=150)),
                ("codigo", models.CharField(default="DEPT-1234", max_length=20)),
                ("semestre", models.CharField(max_length=20)),
                ("descripcion", models.TextField(default="")),
                ("apes", models.ManyToManyField(related_name="_curso_apes_+", to="rubricas.APE")),
                (
                    "competencias",
                    models.ManyToManyField(related_name="_curso_competencias_+", to="rubricas.Competencia"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GrupoCompetencia",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre_corto", models.CharField(max_length=120, unique=True)),
                ("nombre_largo", models.TextField(max_length=1000)),
                ("sigla", models.CharField(max_length=15, unique=True)),
                ("descripcion", models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Patologia",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("nombre", models.CharField(max_length=150, unique=True)),
                ("descripcion", models.TextField(blank=True, default="", null=True)),
                (
                    "contenedora",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.patologia"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Procedimiento",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("nombre", models.CharField(max_length=150)),
                (
                    "capitulo",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.capituloprocedimientos"
                    ),
                ),
                (
                    "contenedora",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.procedimiento"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Programa",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120, unique=True)),
                ("codigo", models.CharField(max_length=10, unique=True)),
                ("apes", models.ManyToManyField(related_name="_programa_apes_+", to="rubricas.APE")),
                (
                    "competencias",
                    models.ManyToManyField(related_name="_programa_competencias_+", to="rubricas.Competencia"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeccionProcedimientos",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("nombre", models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Seccion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("numero", models.IntegerField(default=1)),
                ("identificador_bs", models.CharField(blank=True, max_length=120, null=True)),
                (
                    "curso",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.curso"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rubrica",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120)),
                ("nombre_interno", models.CharField(max_length=120)),
                ("descripcion", models.TextField(blank=True, null=True)),
                ("comentarios", models.TextField(blank=True, null=True)),
                ("debe_tener_procedimientos", models.BooleanField(default=False)),
                ("debe_tener_patologias", models.BooleanField(default=False)),
                ("apes", models.ManyToManyField(null=True, to="rubricas.APE")),
                ("competencias", models.ManyToManyField(null=True, to="rubricas.Competencia")),
                ("cursos", models.ManyToManyField(blank=True, related_name="_rubrica_cursos_+", to="rubricas.Curso")),
                ("patologias", models.ManyToManyField(null=True, to="rubricas.Patologia")),
                ("procedimientos", models.ManyToManyField(null=True, to="rubricas.Procedimiento")),
                (
                    "programa",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.programa"),
                ),
                (
                    "secciones",
                    models.ManyToManyField(blank=True, related_name="_rubrica_secciones_+", to="rubricas.Seccion"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="procedimiento",
            name="seccion",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.seccionprocedimientos"
            ),
        ),
        migrations.CreateModel(
            name="NivelCriterio",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120)),
                ("descripcion", models.TextField()),
                ("puntos", models.IntegerField(default=1)),
                ("numero", models.IntegerField(default=1)),
                ("criterio", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rubricas.criterio")),
            ],
        ),
        migrations.CreateModel(
            name="ItemCalificacion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120)),
                ("peso", models.FloatField(default=100)),
                ("rubrica", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rubricas.rubrica")),
            ],
        ),
        migrations.AddField(
            model_name="curso",
            name="patologias",
            field=models.ManyToManyField(related_name="_curso_patologias_+", to="rubricas.Patologia"),
        ),
        migrations.AddField(
            model_name="curso",
            name="procedimientos",
            field=models.ManyToManyField(related_name="_curso_procedimientos_+", to="rubricas.Procedimiento"),
        ),
        migrations.AddField(
            model_name="curso",
            name="programa",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.programa"),
        ),
        migrations.AddField(
            model_name="criterio",
            name="rubrica",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.rubrica"),
        ),
        migrations.AddField(
            model_name="competencia",
            name="grupo",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.grupocompetencia"
            ),
        ),
        migrations.AddField(
            model_name="capituloprocedimientos",
            name="seccion",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.seccionprocedimientos"
            ),
        ),
        migrations.CreateModel(
            name="ItemCalificacionSeccion",
            fields=[
                (
                    "itemcalificacion_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.itemcalificacion",
                    ),
                ),
                ("seccion", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rubricas.seccion")),
            ],
            bases=("rubricas.itemcalificacion",),
        ),
        migrations.CreateModel(
            name="ItemCalificacionCurso",
            fields=[
                (
                    "itemcalificacion_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.itemcalificacion",
                    ),
                ),
                ("curso", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rubricas.curso")),
            ],
            bases=("rubricas.itemcalificacion",),
        ),
    ]
