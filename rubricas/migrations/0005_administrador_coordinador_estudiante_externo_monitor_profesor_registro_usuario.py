# Generated by Django 3.1.1 on 2021-06-26 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rubricas", "0004_curso_activo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("login", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=200)),
                ("nombre", models.CharField(max_length=120)),
                ("alias", models.CharField(blank=True, max_length=120)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("AD", "Administrador"),
                            ("PR", "Profesor"),
                            ("ES", "Estudiante"),
                            ("MO", "Monitor"),
                            ("EX", "Externo"),
                            ("CO", "Coordinador"),
                        ],
                        default="ES",
                        max_length=2,
                    ),
                ),
                ("ultimo_acceso", models.DateTimeField(auto_now_add=True)),
                ("usuario_local", models.BooleanField(default=False)),
                ("id_brightspace", models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Administrador",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.usuario",
                    ),
                ),
                ("comentario", models.TextField(blank=True)),
            ],
            bases=("rubricas.usuario",),
        ),
        migrations.CreateModel(
            name="Coordinador",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.usuario",
                    ),
                ),
                ("comentario", models.TextField(blank=True)),
            ],
            bases=("rubricas.usuario",),
        ),
        migrations.CreateModel(
            name="Registro",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ip", models.CharField(default="0.0.0.0", max_length=15, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="rubricas.usuario"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.usuario",
                    ),
                ),
                ("secciones", models.ManyToManyField(blank=True, to="rubricas.Seccion")),
            ],
            bases=("rubricas.usuario",),
        ),
        migrations.CreateModel(
            name="Monitor",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.usuario",
                    ),
                ),
                ("secciones", models.ManyToManyField(blank=True, to="rubricas.Seccion")),
            ],
            bases=("rubricas.usuario",),
        ),
        migrations.CreateModel(
            name="Externo",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.usuario",
                    ),
                ),
                ("email", models.CharField(blank=True, max_length=150)),
                ("comentario", models.TextField(blank=True)),
                ("secciones", models.ManyToManyField(blank=True, to="rubricas.Seccion")),
            ],
            bases=("rubricas.usuario",),
        ),
        migrations.CreateModel(
            name="Estudiante",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rubricas.usuario",
                    ),
                ),
                ("preguntas_sin_respuesta", models.BooleanField(default=False)),
                ("solo_nombre", models.CharField(max_length=120)),
                ("solo_apellido", models.CharField(max_length=120)),
                ("secciones", models.ManyToManyField(blank=True, to="rubricas.Seccion")),
            ],
            bases=("rubricas.usuario",),
        ),
    ]
