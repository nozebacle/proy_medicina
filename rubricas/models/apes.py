# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    APE
"""

from django.db import models
from rubricas.models.secciones import Programa

class APE(models.Model):
    """
    Esta clase sirve para representar un APE: Actividad Profesional Esencial
    """
    nombre_corto = models.CharField(max_length=120, unique=True)
    nombre_largo = models.TextField(blank=False)
    sigla = models.CharField(max_length=15, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sigla + ": " + self.nombre_corto

    def buscar_por_sigla(sigla: str):
        """
        Busca el APE con la sigla dada y la retorna
        Si no encuentra uno, retorna None
        """
        try:
            return APE.objects.get(sigla=sigla)
        except:
            return None

    def buscar_por_programa(programa: Programa):
        apes = APE.objects.filter(programa=programa)
        return apes
