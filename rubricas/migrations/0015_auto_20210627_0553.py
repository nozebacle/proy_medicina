# Generated by Django 3.1.1 on 2021-06-27 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rubricas', '0014_auto_20210627_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='codigo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='resumenestudianteseccion',
            name='ultimo_resultado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rubricas.resultadorubrica'),
        ),
    ]
