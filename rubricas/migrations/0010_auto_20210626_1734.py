# Generated by Django 3.1.1 on 2021-06-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rubricas", "0009_auto_20210626_1731"),
    ]

    operations = [
        migrations.AlterField(
            model_name="criterio",
            name="apes",
            field=models.ManyToManyField(blank=True, null=True, to="rubricas.APE"),
        ),
        migrations.AlterField(
            model_name="criterio",
            name="competencias",
            field=models.ManyToManyField(blank=True, null=True, to="rubricas.Competencia"),
        ),
        migrations.AlterField(
            model_name="curso",
            name="apes",
            field=models.ManyToManyField(blank=True, to="rubricas.APE"),
        ),
        migrations.AlterField(
            model_name="curso",
            name="competencias",
            field=models.ManyToManyField(blank=True, to="rubricas.Competencia"),
        ),
        migrations.AlterField(
            model_name="curso",
            name="patologias",
            field=models.ManyToManyField(blank=True, to="rubricas.Patologia"),
        ),
        migrations.AlterField(
            model_name="curso",
            name="procedimientos",
            field=models.ManyToManyField(blank=True, to="rubricas.Procedimiento"),
        ),
        migrations.AlterField(
            model_name="programa",
            name="apes",
            field=models.ManyToManyField(blank=True, to="rubricas.APE"),
        ),
        migrations.AlterField(
            model_name="programa",
            name="competencias",
            field=models.ManyToManyField(blank=True, to="rubricas.Competencia"),
        ),
        migrations.AlterField(
            model_name="resumencompetenciasemestre",
            name="secciones",
            field=models.ManyToManyField(blank=True, to="rubricas.Seccion"),
        ),
        migrations.AlterField(
            model_name="rubrica",
            name="apes",
            field=models.ManyToManyField(blank=True, null=True, to="rubricas.APE"),
        ),
        migrations.AlterField(
            model_name="rubrica",
            name="competencias",
            field=models.ManyToManyField(blank=True, null=True, to="rubricas.Competencia"),
        ),
        migrations.AlterField(
            model_name="rubrica",
            name="patologias",
            field=models.ManyToManyField(blank=True, null=True, to="rubricas.Patologia"),
        ),
        migrations.AlterField(
            model_name="rubrica",
            name="procedimientos",
            field=models.ManyToManyField(blank=True, null=True, to="rubricas.Procedimiento"),
        ),
    ]
