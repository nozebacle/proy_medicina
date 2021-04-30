# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Programa
    Curso
    Seccion
"""

from django.db import models


class Programa(models.Model):
    """
    Esta clase sirve para representar un programa que agrupa Cursos
    """
    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=10, unique=True)
    apes = models.ManyToManyField("rubricas.APE")
    competencias = models.ManyToManyField("rubricas.Competencia")

    def __str__(self):
        return self.nombre

    def buscar_por_codigo(codigo: str):
        """
        Busca el Programa con el codigo dado y lo retorna
        Si no encuentra uno, retorna None
        """
        try:
            return Programa.objects.get(codigo=codigo)
        except:
            return None

class Curso(models.Model):
    """
    Esta clase sirve para representar un curso dentro de un programa
    """
    programa = models.ForeignKey("rubricas.Programa", null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=120, unique=False)
    nombre_interno = models.CharField(max_length=150, unique=False)
    codigo = models.CharField(max_length=20, unique=False, default="DEPT-1234")
    semestre = models.CharField(max_length=20, unique=False)
    descripcion = models.TextField(default="")
    apes = models.ManyToManyField("rubricas.APE")
    competencias = models.ManyToManyField("rubricas.Competencia")
    patologias = models.ManyToManyField("rubricas.Patologia")
    procedimientos = models.ManyToManyField("rubricas.Procedimiento")

    def __str__(self):
        return self.nombre + "-" +  self.semestre

    def buscar_por_codigo_semestre(codigo: str, semestre: str):
        """
        Busca el Curso con el codigo y el semestre dados y lo retorna
        Si no encuentra uno, retorna None
        """
        try:
            return Curso.objects.get(codigo=codigo, semestre=semestre)
        except:
            return None


class Seccion(models.Model):
    """
    Esta clase sirve para representar secciones de un curso en un semestre particular.
    """
    curso = models.ForeignKey("rubricas.Curso", null=True, on_delete=models.SET_NULL)
    numero = models.IntegerField(default=1)
    identificador_bs = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.curso) + ", Secc. " + str(self.numero)

    def buscar_por_numero(curso: Curso, numero: int):
        """
        Busca la Sección del curso dado, con el número dado y la retorna
        Si no la encuentra, retorna None
        """
        try:
            return Seccion.objects.get(curso=curso, numero=numero)
        except:
            return None

#     def crear_seccion(numero_seccion: int, nombre_semestre: str, curso: Curso, identificador_bs = "0"):
#         """
#         Crea una nueva sección con los parámetros dados
#         Parámetros:
#             numero_seccion: el número de la nueva sección
#             nombre_semestre: el nombre del semestre en el que se va a crear la sección
#             curso: el curso al que va a pertenecer la sección
#         Return:
#             (Seccion) : La nueva sección que fue creada
#         """
#         nueva_seccion = Seccion()
#         nueva_seccion.numero = numero_seccion
#         nueva_seccion.nombre_semestre = nombre_semestre
#         nueva_seccion.curso_seccion = curso
#         nueva_seccion.identificador_bs = identificador_bs
#         nueva_seccion.save()
#         return nueva_seccion

#     def buscar_seccion(curso: Curso, semestre: str, num_seccion: str):
#         """ Busca una sección dado el curso, semestre y número de la sección
#         Parámetros:
#             curso (Curso): El curso del que debe hacer parte la sección
#             semestre (str): El nombre del semestre en que se busca la sección
#             num_seccion (id): El número de la sección (no el identificador)
#         Retorno:
#             (Seccion): La sección que cumple con los criterios o None
#         """
#         secciones = (
#             Seccion.objects.filter(curso_seccion=curso).filter(nombre_semestre=semestre).filter(numero=num_seccion)
#         )
#         if len(secciones) > 0:
#             return secciones[0]
#         return None

#     def __str__(self):
#         if self.curso_seccion is None:
#             cod = "***"
#         else:
#             cod = self.curso_seccion.codigo_curso
#         return cod + " - " + self.nombre_semestre + ": " + str(self.numero)

#     @property
#     def cantidad_estudiantes(self) -> int:
#         """
#         Esta propiedad calcula la cantidad de estudiantes en la sección
#         Retorno:
#             (int): Cantidad de estudiantes
#         """
#         numero = self.estudiante_set.count()
#         return numero

#     def secciones():
#         """
#         Retorna todas las secciones del sistema
#         """
#         return Seccion.objects.all()

#     def secciones_semestre(semestre: str):
#         """ Busca todas las secciones de un semestre particular
#         Parámetros:
#             semestre (str): El nombre del semestre para el que se van a buscar las secciones
#         """
#         return Seccion.objects.filter(nombre_semestre=semestre)

#     @property
#     def profesores(self):
#         """
#         Esta propiedad calcula el conjunto de los profesores de la sección
#         """
#         return self.profesor_set.all()
