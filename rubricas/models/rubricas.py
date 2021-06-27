# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Rubrica
    RubricaPrograma
    RubricaCurso
    Criterio
    Nivel Criterio
    ItemCalificacion
    ItemCalificacionCurso
    ItemCalificacionSeccion
"""

from django.db import models
from django.db.models import Max


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

    patologias = models.ManyToManyField("rubricas.Patologia", null=True, blank=True)
    procedimientos = models.ManyToManyField("rubricas.Procedimiento", null=True, blank=True)

    apes = models.ManyToManyField("rubricas.APE", null=True, blank=True)
    competencias = models.ManyToManyField("rubricas.Competencia", null=True, blank=True)

    def clonar_a_rubrica_curso(self):
        clon = RubricaCurso()
        clon.save()
        Rubrica.copiar_rubrica(self, clon)
        return clon

    def clonar_a_rubrica_seccion(self):
        clon = RubricaSeccion()
        clon.save()
        Rubrica.copiar_rubrica(self, clon)
        return clon

    def copiar_rubrica(original, clon):
        clon.nombre = original.nombre
        clon.nombre_interno = original.nombre_interno
        clon.descripcion = original.descripcion
        clon.comentarios = ""
        clon.debe_tener_procedimientos = original.debe_tener_procedimientos
        clon.debe_tener_patologias = original.debe_tener_patologias
        clon.save()

        for ape in original.apes.all():
            clon.agregar_ape(ape)
        for competencia in original.competencias.all():
            clon.agregar_competencia(competencia)
        for patologia in original.patologias.all():
            clon.agregar_patologia(patologia)
        for procedimiento in original.procedimientos.all():
            clon.agregar_procedimiento(procedimiento)

        criterios = original.consultar_criterios()
        for criterio in criterios:
            criterio.clonar_criterio(clon)

        clon.save()

    def __str__(self):
        return self.nombre

    def agregar_ape(self, APE) -> None:
        """
        Agrega una nueva APE a la rubrica.
        Parámetros:
          APE: el APE que se debe agregar
        """
        self.apes.add(APE)

    def agregar_competencia(self, competencia) -> None:
        """
        Agrega una nueva competencia a la rubrica.
        Parámetros:
          competencia: la competencia que se debe agregar
        """
        self.competencias.add(competencia)

    def agregar_patologia(self, patologia) -> None:
        """
        Agrega una nueva patologia a la rubrica.
        Parámetros:
          patologia: el patologia que se debe agregar
        """
        self.patologias.add(patologia)

    def agregar_procedimiento(self, procedimiento) -> None:
        """
        Agrega un nuevo procedimiento a la rubrica.
        Parámetros:
          procedimiento: el procedimiento que se debe agregar
        """
        self.procedimientos.add(procedimiento)

    def consultar_niveles(self) -> None:
        """
        Consulta los niveles asociados a uno de los criterios de la rúbrica.
        Retorna una lista de NivelCriterio
        """
        if self.criterio_set.count() > 0:
            return self.criterio_set.first().nivelcriterio_set.all().order_by("numero")
        else:
            return []

    def contar_niveles(self) -> None:
        """
        Cuenta la cantida de niveles asociados a uno de los criterios de la rúbrica.
        Retorna un entero
        """
        if self.criterio_set.count() > 0:
            return self.criterio_set.first().nivelcriterio_set.count()
        else:
            return 0

    def consultar_criterios(self) -> None:
        """
        Consulta los criterios asociados a la rúbrica.
        Retorna una lista de Criterio
        """
        return self.criterio_set.all().order_by("numero")

    def consultar_total_puntos(self) -> int:
        criterios = self.consultar_criterios()
        total = 0
        for criterio in criterios:
            total += criterio.consultar_total_puntos()
        return total


class RubricaPrograma(Rubrica):
    programa = models.ForeignKey("rubricas.Programa", null=True, on_delete=models.SET_NULL)


class RubricaCurso(Rubrica):
    cursos = models.ManyToManyField("rubricas.Curso", blank=True)

    def agregar_curso(self, curso) -> None:
        """
        Agrega un nuevo curso a la rúbrica
        Parámetros:
          curso: el curso que se debe agregar
        """
        self.cursos.add(curso)


class RubricaSeccion(Rubrica):
    seccion = models.ForeignKey("rubricas.Seccion", null=True, on_delete=models.SET_NULL)


class Criterio(models.Model):
    """
    Esta clase sirve para representar un criterio en una rúbrica
    """

    nombre_interno = models.CharField(max_length=120)
    descripcion = models.TextField(null=False, blank=False)
    rubrica = models.ForeignKey("rubricas.Rubrica", null=True, on_delete=models.SET_NULL)
    numero = models.IntegerField()
    apes = models.ManyToManyField("rubricas.APE", null=True, blank=True)
    competencias = models.ManyToManyField("rubricas.Competencia", null=True, blank=True)


    def __str__(self):
        return self.nombre_interno + " (" + str(self.rubrica) + ")"

    def agregar_ape(self, APE) -> None:
        """
        Agrega una nueva APE al criterio.
        Parámetros:
          APE: el APE que se debe agregar
        """
        self.apes.add(APE)

    def agregar_competencia(self, competencia) -> None:
        """
        Agrega una nueva competencia al criterio.
        Parámetros:
          competencia: la competencia que se debe agregar
        """
        self.competencias.add(competencia)

    def consultar_nombres_apes(self) -> str:
        resumen = ""
        for ape in self.apes.all():
            if resumen != "":
                resumen += " - "
            resumen += ape.sigla
        return resumen

    def consultar_nombres_competencias(self) -> str:
        resumen = ""
        for comp in self.competencias.all():
            if resumen != "":
                resumen += " - "
            resumen += comp.sigla
        return resumen

    def consultar_niveles(self) -> None:
        """
        Consulta los niveles asociados a un criterios de la rúbrica.
        Retorna una lista de NivelCriterio
        """
        return self.nivelcriterio_set.all().order_by("numero")

    def consultar_total_puntos(self) -> int:
        return self.nivelcriterio_set.all().aggregate(Max("puntos"))["puntos__max"]


    def clonar_criterio(self, rubrica):
        clon = Criterio()
        clon.nombre_interno = self.nombre_interno
        clon.descripcion = self.descripcion
        clon.numero = self.numero
        clon.save()

        clon.rubrica = rubrica
        for ape in self.apes.all():
            clon.agregar_ape(ape)
        for competencia in self.competencias.all():
            clon.agregar_competencia(competencia)
        clon.save()

        niveles = self.nivelcriterio_set.all()
        for nivel in niveles:
            nivel.clonar_nivel(clon)
        clon.save()



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
        return self.criterio.nombre_interno + ": " + self.nombre + " (" + str(self.numero) + ")"

    def clonar_nivel(self, criterio):
        clon = NivelCriterio()
        clon.nombre = self.nombre
        clon.descripcion = self.descripcion
        clon.puntos = self.puntos
        clon.numero= self.numero
        clon.criterio = criterio
        clon.save()


class ItemCalificacion(models.Model):
    """
    Esta clase sirve para representar un ítem de calificación dentro de un curso o sección.
    Un Item de calificacion corresponde a una rúbrica
    """

    nombre = models.CharField(max_length=120, unique=False)
    peso = models.FloatField(default=100)
    rubrica = models.ForeignKey("rubricas.Rubrica", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre + " (" + str(self.peso) + "%) --> " + str(self.rubrica)


class ItemCalificacionCurso(ItemCalificacion):
    """
    Esta clase sirve para representar un ítem de calificación dentro de un curso.
    """

    curso = models.ForeignKey("rubricas.Curso", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " (" + str(self.peso) + "%) --> " + str(self.rubrica) + " / " + str(self.curso)

    def buscar_rubricas_curso(id_curso):
        print("dummy")
        return RubricaCurso.objects.all()

    def clonar_a_item_curso(self):
        clon = ItemCalificacionCurso()
        clon.save()
        ItemCalificacionCurso.copiar_item(self, clon)
        return clon

    def clonar_a_item_seccion(self):
        clon = ItemCalificacionSeccion()
        clon.save()
        ItemCalificacionCurso.copiar_item(self, clon)
        return clon

    def copiar_item(original, clon):
        clon.nombre = original.nombre
        clon.peso = original.peso
        clon.save()


class ItemCalificacionSeccion(ItemCalificacion):
    """
    Esta clase sirve para representar un ítem de calificación dentro de un curso.
    """

    seccion = models.ForeignKey("rubricas.Seccion", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre + " (" + str(self.peso) + "%) --> " + str(self.rubrica) + " / " + str(self.seccion)
