# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    APE
"""

from django.db import models
from rubricas.models.secciones import Programa
from rubricas.models.rubricas import RubricaPrograma, RubricaCurso, RubricaSeccion


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
        """
        Busca todas las APEs que pertenecen al programa indicado
        Parámetros:
            programa: El objeto que representa al programa
        """
        apes = APE.objects.filter(programa=programa)
        return apes

    def buscar_por_id(id_ape: int):
        """
        Busca el APE con el id dado.
        Si no se encuentra el APE retorna None
        """
        try:
            return APE.objects.get(id=id_ape)
        except:
            return None

    def buscar_rubricas_ape_programa(self, id_programa):
        """
        Retorna todas las rúbricas del programa indicado que
        están asociadas a este APE.
        Este método sólo retorna rúbricas de tipo RubricaPrograma
        """
        print("dummy")
        return RubricaPrograma.objects.all()
        return []

    def buscar_rubricas_ape_cursos_programa(self, id_programa):
        """
        Retorna todas las rúbricas de cursos que hacen parte
        del programa indicado y que están asociadas a este APE.
        Este método sólo retorna rúbricas de tipo RubricaCurso
        """
        print("dummy")
        return RubricaCurso.objects.all()
        return []

    def buscar_rubricas_ape_curso(self, id_curso):
        """
        Retorna todas las rúbricas del curso indicado
         que están asociadas a este APE.
        Este método sólo retorna rúbricas de tipo RubricaCurso
        """
        print("dummy")
        return RubricaCurso.objects.all()
        return []

    def buscar_rubricas_ape_seccion(self, id_seccion):
        """
        Retorna todas las rúbricas de la sección indicada
        que están asociadas a este APE.
        Este método sólo retorna rúbricas de tipo RubricaSeccion
        """
        print("dummy")
        return RubricaSeccion.objects.all()
        return []
