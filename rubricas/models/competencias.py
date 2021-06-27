# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Competencia
    GrupoCompetencia
"""

from django.db import models

from rubricas.models.rubricas import RubricaPrograma, RubricaCurso, RubricaSeccion


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

    def buscar_por_programa(programa: str):
        """
        Busca los grupos de competencias tales que al menos una de sus
        competencias aparecen dentro del programa
        """
        return GrupoCompetencia.objects.all()


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

    def buscar_por_programa(programa: str):
        ...

    def buscar_por_id(id_competencia: int):
        """
        Busca la compenteica con el id dado.
        Si no se encuentra la competencia retorna None
        """
        try:
            return Competencia.objects.get(id=id_competencia)
        except:
            return None

    def buscar_rubricas_competencia_programa(self, id_programa):
        """
        Retorna todas las rúbricas del programa indicado que
        están asociadas a esta competencia.
        Este método sólo retorna rúbricas de tipo RubricaPrograma
        """
        print("dummy")
        return RubricaPrograma.objects.all()
        return []

    def buscar_rubricas_competencia_cursos_programa(self, id_programa):
        """
        Retorna todas las rúbricas de cursos que hacen parte
        del programa indicado y que están asociadas a esta competencia.
        Este método sólo retorna rúbricas de tipo RubricaCurso
        """
        print("dummy")
        return RubricaCurso.objects.all()
        return []

    def buscar_rubricas_competencia_curso(self, id_curso):
        """
        Retorna todas las rúbricas del curso indicado
         que están asociadas a esta competencia.
        Este método sólo retorna rúbricas de tipo RubricaCurso
        """
        print("dummy")
        return RubricaCurso.objects.all()
        return []

    def buscar_rubricas_competencia_seccion(self, id_seccion):
        """
        Retorna todas las rúbricas de la sección indicada
        que están asociadas a esta competencia.
        Este método sólo retorna rúbricas de tipo RubricaSeccion
        """
        print("dummy")
        return RubricaSeccion.objects.all()
        return []
