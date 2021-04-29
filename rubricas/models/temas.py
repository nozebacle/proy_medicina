# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Patologia
    Procedimiento
"""

from django.db import models


class Patologia(models.Model):
    """
    Esta clase sirve para representar una patología que se estudie en uno o muchos cursos
    """
    contenedora = models.ForeignKey("rubricas.Patologia", null=True, on_delete=models.SET_NULL)
    codigo = models.CharField(max_length=20, unique=True, blank=False)
    nombre = models.CharField(max_length=150, unique=True, blank=False)
    descripcion = models.TextField(null=True, blank=True, default="")

    def __str__(self):
        return self.codigo + ": " + self.nombre

    def buscar_por_codigo(codigo: str):
        """
        Busca la Patologia con el codigo y la retorna
        Si no la encuentra, retorna None
        """
        try:
            return Patologia.objects.get(codigo=codigo)
        except:
            return None

class SeccionProcedimientos(models.Model):
    """
    Esta clase sirve para representar una sección que se use para clasificar procedimientos
    """
    codigo = models.CharField(max_length=20, unique=True, blank=False)
    nombre = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return self.nombre

class CapituloProcedimientos(models.Model):
    """
    Esta clase sirve para representar un capítulo que se use para clasificar procedimientos
    """
    seccion = models.ForeignKey("rubricas.SeccionProcedimientos", null=True, on_delete=models.SET_NULL)
    codigo = models.CharField(max_length=20, unique=True, blank=False)
    nombre = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return self.nombre

class Procedimiento(models.Model):
    """
    Esta clase sirve para representar un procedimiento que se estudie o practique en uno o en muchos cursos
    """
    contenedora = models.ForeignKey("rubricas.Procedimiento", null=True, on_delete=models.SET_NULL)
    seccion = models.ForeignKey("rubricas.SeccionProcedimientos", null=True, on_delete=models.SET_NULL)
    capitulo = models.ForeignKey("rubricas.CapituloProcedimientos", null=True, on_delete=models.SET_NULL)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150, unique=False, blank=False)

    def __str__(self):
        return self.codigo + ": " +  self.nombre

    def buscar_por_codigo(codigo: str):
        """
        Busca el Procedimiento con el codigo y lo retorna
        Si no lo encuentra, retorna None
        """
        try:
            return Procedimiento.objects.get(codigo=codigo)
        except:
            return None