# Generated by Django 3.1.1 on 2021-06-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubricas', '0010_auto_20210626_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='semestre',
            field=models.CharField(default='2020-20', max_length=20),
            preserve_default=False,
        ),
    ]
