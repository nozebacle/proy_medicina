# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Rubrica
    Criterio
    Nivel Criterio
    ItemCalificacion
"""

from django.db import models


class Rubrica(models.Model):
    """
    Esta clase sirve para representar una Rúbrica
    """
    nombre = models.CharField(max_length=120, unique=False)
    nombre_interno = models.CharField(max_length=120, unique=False)
    descripcion = models.TextField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    debe_tener_procedimientos = models.BooleanField(default=False)
    debe_tener_patologias = models.BooleanField(default=False)

    patologias = models.ManyToManyField("rubricas.Patologia", null=True)
    procedimientos = models.ManyToManyField("rubricas.Procedimiento", null=True)

    apes = models.ManyToManyField("rubricas.APE", null=True)
    competencias = models.ManyToManyField("rubricas.Competencia", null=True)

    programa = models.ForeignKey("rubricas.Programa", null=True, on_delete=models.SET_NULL)
    cursos = models.ManyToManyField("rubricas.Curso", related_name='+', blank=True)
    secciones = models.ManyToManyField("rubricas.Seccion", related_name='+', blank=True)


    def __str__(self):
        return self.nombre



class Criterio(models.Model):
    """
    Esta clase sirve para representar un criterio en una rúbrica
    """
    nombre_interno = models.CharField(max_length=120)
    descripcion = models.TextField(null=False, blank=False)
    rubrica = models.ForeignKey("rubricas.Rubrica", null=True, on_delete=models.SET_NULL)
    numero = models.IntegerField()
    apes = models.ManyToManyField("rubricas.APE", null=True)
    competencias = models.ManyToManyField("rubricas.Competencia", null=True)

    def __str__(self):
        return self.nombre_interno + " ("  + str(self.rubrica) + ")"


class NivelCriterio(models.Model):
    """
    Esta clase sirve para representar un nivel para un criterio de una rúbrica
    """
    nombre = models.CharField(max_length=120, unique=False)
    criterio = models.ForeignKey("rubricas.Criterio", null=False, on_delete=models.CASCADE)
    descripcion = models.TextField(null=False, blank=False)
    puntos = models.IntegerField(default=1)
    numero = models.IntegerField(default=1)

    def __str__(self):
        return self.criterio.nombre_interno + ": "  + self.nombre + " ("+ str(self.numero) + ")"


class ItemCalificacion(models.Model):
    """
    Esta clase sirve para representar un ítem de calificación dentro de un curso o sección.
    Un Item de calificacion corresponde a una rúbrica
    """
    nombre = models.CharField(max_length=120, unique=False)
    peso = models.FloatField(default=100)
    rubrica = models.ForeignKey("rubricas.Rubrica", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " (" + self.peso + "%) --> " + str(self.rubrica)

class ItemCalificacionCurso(ItemCalificacion):
    """
    Esta clase sirve para representar un ítem de calificación dentro de un curso.
    """
    curso = models.ForeignKey("rubricas.Curso", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " (" + str(self.peso) + "%) --> " + str(self.rubrica) + " / " + str(self.curso)

class ItemCalificacionSeccion(ItemCalificacion):
    """
    Esta clase sirve para representar un ítem de calificación dentro de un curso.
    """
    seccion = models.ForeignKey("rubricas.Seccion", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " (" + str(self.peso) + "%) --> " + str(self.rubrica) + " / " + str(self.seccion)