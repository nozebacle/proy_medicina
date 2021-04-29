# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Competencia
    GrupoCompetencia
"""

from django.db import models


class GrupoCompetencia(models.Model):
    """
    Esta clase sirve para representar un Grupo de Competencias
    """
    nombre_corto = models.CharField(max_length=120, unique=True)
    nombre_largo = models.TextField(max_length=1000, blank=False)
    sigla = models.CharField(max_length=15, unique=True)
    descripcion = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.nombre_corto

    def buscar_por_sigla(sigla: str):
        """
        Buscar el GrupoCompetencia con la sigla dada y lo retorna
        Si no encuentra uno, retorna None
        """
        try:
            return GrupoCompetencia.objects.get(sigla=sigla)
        except:
            return None


class Competencia(models.Model):
    """
    Esta clase sirve para representar una Competencia
    """
    grupo = models.ForeignKey("rubricas.GrupoCompetencia", null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=220, unique=True)
    sigla = models.CharField(max_length=15, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sigla + ": " + self.nombre

    def buscar_por_sigla(sigla: str):
        """
        Busca la Competecnia con la sigla dada y la retorna
        Si no encuentra uno, retorna None
        """
        try:
            return Competencia.objects.get(sigla=sigla)
        except:
            return None
