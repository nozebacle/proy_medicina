# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    ResultadoRubrica
    ResultadoCriterio
"""

from django.db import models


class ResultadoRubrica(models.Model):
    """
    Esta clase sirve para representar el resultado de un estudiante
    en una rúbrica particular de un curso
    """

    estudiante = models.ForeignKey(
        "rubricas.Estudiante", null=True, on_delete=models.SET_NULL, related_name="resultados"
    )
    evaluador = models.ForeignKey("rubricas.Usuario", null=True, on_delete=models.SET_NULL, related_name="evaluados")
    item = models.ForeignKey("rubricas.ItemCalificacionSeccion", null=True, on_delete=models.SET_NULL)
    comentario = models.TextField(null=False, blank=True)
    resultado = models.FloatField(default=0)
    puntos = models.IntegerField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        iniciales = self.estudiante.iniciales()
        item = self.item
        resultado = self.resultado
        puntos = self.puntos
        return f"{iniciales}: {item} --> {puntos} ({resultado}%)"

    def buscar_resultado_estudiante_item(estudiante, item):
        return ResultadoRubrica.objects.filter(estudiante=estudiante, item=item).first()

class ResultadoCriterio(models.Model):
    """
    Esta clase sirve para representar un nivel que alcanzón
    un estudiante para un criterio de una rúbrica particular
    """

    estudiante = models.ForeignKey("rubricas.Estudiante", null=True, on_delete=models.SET_NULL)
    resultado_rubrica = models.ForeignKey("rubricas.ResultadoRubrica", null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey("rubricas.ItemCalificacionSeccion", null=True, on_delete=models.SET_NULL)
    criterio = models.ForeignKey("rubricas.Criterio", null=True, on_delete=models.SET_NULL)
    nivel = models.ForeignKey("rubricas.NivelCriterio", null=True, on_delete=models.SET_NULL)
    comentario = models.TextField(null=False, blank=True)
    puntos = models.IntegerField(default=0)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        iniciales = self.estudiante.iniciales()
        criterio = self.criterio
        nivel = self.nivel.numero
        return f"{iniciales}: {criterio} --> {nivel}"
