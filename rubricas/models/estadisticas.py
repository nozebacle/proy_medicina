# -*- coding: utf-8 -*-

"""
En este módulo se definen clases que son administradas por django:
    ResumenEstudianteSeccion
    ResumenAPEEvaluacion
    ResumenAPESemestre
    ResumenCompetenciaEvaluacion
    ResumenCompetenciaSemestre
"""

from django.db import models


class ResumenEstudianteSeccion(models.Model):
    """
    Esta clase sirve para representar el resultado acumulado
    de un estudiante en una sección
    """

    estudiante = models.ForeignKey("rubricas.Estudiante", null=True, on_delete=models.SET_NULL)
    seccion = models.ForeignKey("rubricas.Seccion", null=True, on_delete=models.SET_NULL)
    ultimo_resultado = models.ForeignKey("rubricas.ResultadoRubrica", null=True, blank=True, on_delete=models.SET_NULL)
    resultado = models.FloatField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)

    def buscar_resumen(id_estudiante, id_seccion):
        return ResumenEstudianteSeccion.objects.filter(estudiante=1, seccion=89).first()

    def resultado_porcentual(self):
        return self.resultado * 20


class ResumenAPEEvaluacion(models.Model):
    """
    Esta clase sirve para representar el resultado acumulado
    de un estudiante para un APE en una evaluación particular (ItemCalificacionSeccion)
    """

    estudiante = models.ForeignKey("rubricas.Estudiante", null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey("rubricas.ItemCalificacionSeccion", null=True, on_delete=models.SET_NULL)
    ape = models.ForeignKey("rubricas.APE", null=True, on_delete=models.SET_NULL)
    resultado = models.FloatField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)


class ResumenCompetenciaEvaluacion(models.Model):
    """
    Esta clase sirve para representar el resultado acumulado
    de un estudiante para una competencia en una evaluación particular (ItemCalificacionSeccion)
    """

    estudiante = models.ForeignKey("rubricas.Estudiante", null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey("rubricas.ItemCalificacionSeccion", null=True, on_delete=models.SET_NULL)
    competencia = models.ForeignKey("rubricas.Competencia", null=True, on_delete=models.SET_NULL)
    resultado = models.FloatField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)


class ResumenAPESemestre(models.Model):
    """
    Esta clase sirve para representar el resultado acumulado
    de un estudiante para un APE en un semestre particular
    """

    estudiante = models.ForeignKey("rubricas.Estudiante", null=True, on_delete=models.SET_NULL)
    semestre = models.CharField(max_length=20, unique=False)
    secciones = models.ManyToManyField("rubricas.Seccion", blank=True)
    ape = models.ForeignKey("rubricas.APE", null=True, on_delete=models.SET_NULL)
    resultado = models.FloatField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)


class ResumenCompetenciaSemestre(models.Model):
    """
    Esta clase sirve para representar el resultado acumulado
    de un estudiante para una competencia en un semestre particular
    """

    estudiante = models.ForeignKey("rubricas.Estudiante", null=True, on_delete=models.SET_NULL)
    semestre = models.CharField(max_length=20, unique=False)
    secciones = models.ManyToManyField("rubricas.Seccion", blank=True)
    competencia = models.ForeignKey("rubricas.Competencia", null=True, on_delete=models.SET_NULL)
    resultado = models.FloatField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)
