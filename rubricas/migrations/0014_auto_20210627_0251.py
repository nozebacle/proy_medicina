# Generated by Django 3.1.1 on 2021-06-27 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rubricas', '0013_auto_20210627_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcalificacion',
            name='rubrica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rubricas.rubrica'),
        ),
    ]
