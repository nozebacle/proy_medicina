# -*- coding: utf-8 -*-
"""
En este módulo se definen clases que son administradas por django:
    Programa
    Curso
    Seccion
"""

from django.db import models
from rubricas.models.competencias import GrupoCompetencia
from rubricas.models.rubricas import RubricaCurso, RubricaSeccion, ItemCalificacionCurso


class Programa(models.Model):
    """
    Esta clase sirve para representar un programa que agrupa Cursos
    """

    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=10, unique=True)
    apes = models.ManyToManyField("rubricas.APE", blank=True)
    competencias = models.ManyToManyField("rubricas.Competencia", blank=True)

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

    def buscar_por_id(id_programa: int):
        """
        Busca el Programa con el id dado y lo retorna
        Si no encuentra uno, retorna None
        """
        try:
            return Programa.objects.get(id=id_programa)
        except:
            return None

    def buscar_por_profesor(id_profesor: int):
        """
        Busca todos los programas en los cuales partipa el profesor
        con el id dado. Si el id no corresponde a un profesor, o el
        profesor no hace parte de ningún curso o sección, retorna una
        lista vacía.
        """
        try:
            return Programa.objects.all()
        except:
            return None

    def agregar_ape(self, APE) -> None:
        """
        Agrega una nueva APE al programa.
        Parámetros:
          APE: el APE que se debe agregar
        """
        self.apes.add(APE)

    def agregar_competencia(self, competencia) -> None:
        """
        Agrega una nueva competencia al programa.
        Parámetros:
          competencia: la competencia que se debe agregar
        """
        self.competencias.add(competencia)

    def consultar_grupos_competencias_programa(self):
        """
        Consulta los grupos de competencia a los que pertenecen las
        competencias asociadas al programa
        """
        return GrupoCompetencia.buscar_por_programa(self)

    def consultar_cursos_programa(self):
        """
        Retorna los cursos que hacen parte del programa
        """
        return self.curso_set.all()

    def consultar_apes(self):
        """Retorna los APEs asociadas al programa"""
        return self.apes.all()

    def consultar_competencias(self):
        """Retorna las competencias asociadas al programa"""
        return self.competencias.all()


class Curso(models.Model):
    """
    Esta clase sirve para representar un curso dentro de un programa
    """
    programa = models.ForeignKey("rubricas.Programa", null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=120, unique=False)
    nombre_interno = models.CharField(max_length=150, unique=False)
    codigo = models.CharField(max_length=20, unique=False, default="DEPT-1234")
    semestre = models.CharField(max_length=20, unique=False)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField(default="")
    apes = models.ManyToManyField("rubricas.APE", blank=True)
    competencias = models.ManyToManyField("rubricas.Competencia", blank=True)
    patologias = models.ManyToManyField("rubricas.Patologia", blank=True)
    procedimientos = models.ManyToManyField("rubricas.Procedimiento", blank=True)

    def __str__(self):
        return self.nombre + "-" + self.semestre

    def buscar_por_codigo_semestre(codigo: str, semestre: str):
        """
        Busca el Curso con el codigo y el semestre dados y lo retorna
        Si no encuentra uno, retorna None
        """
        try:
            return Curso.objects.get(codigo=codigo, semestre=semestre)
        except:
            return None

    def buscar_por_id(id_curso: int):
        """
        Busca el Curso con el id dado y lo retorna
        Si no encuentra uno, retorna None
        """
        try:
            return Curso.objects.get(id=id_curso)
        except:
            return None

    def agregar_ape(self, APE) -> None:
        """
        Agrega una nueva APE al curso.
        Parámetros:
          APE: el APE que se debe agregar
        """
        self.apes.add(APE)

    def agregar_competencia(self, competencia) -> None:
        """
        Agrega una nueva competencia al curso.
        Parámetros:
          competencia: la competencia que se debe agregar
        """
        self.competencias.add(competencia)

    def consultar_rubricas(self):
        """Retorna las rúbricas asociadas al curso"""
        return self.rubricacurso_set.all()

    def consultar_items(self):
        """Retorna los ítems de calificación del curso"""
        return self.itemcalificacioncurso_set.all()

    def consultar_apes(self):
        """Retorna los APEs asociadas al curso"""
        return self.apes.all()

    def consultar_competencias(self):
        """Retorna las competencias asociadas al curso"""
        return self.competencias.all()

    def derivar_seccion(self, numero: int, semestre: str):
        """
        Crea una nueva sección que es un reflejo del curso y está asociada a este curso.
        La nueva sección tiene asciados elementos de tipo RubricaSeccion e ItemCalificacionSeccion
        """
        seccion = Seccion()
        seccion.curso = self
        seccion.numero = numero
        seccion.semestre = semestre
        seccion.save()

        diccionario_clones = {}

        rubricas = self.consultar_rubricas()
        for rubrica in rubricas:
            print("clonando", rubrica.nombre)
            r_seccion = rubrica.clonar_a_rubrica_seccion()
            r_seccion.seccion = seccion
            r_seccion.save()
            diccionario_clones[rubrica.id] = r_seccion.id

        items = self.consultar_items()
        for item in items:
            print("clonando", item.nombre)
            i_seccion = item.clonar_a_item_seccion()
            i_seccion.seccion = seccion
            id_rubrica_seccion = diccionario_clones[item.rubrica.id]
            i_seccion.rubrica = RubricaSeccion.objects.get(id=id_rubrica_seccion)
            i_seccion.save()

        return seccion

class Seccion(models.Model):
    """
    Esta clase sirve para representar secciones de un curso en un semestre particular.
    """

    curso = models.ForeignKey("rubricas.Curso", null=True, on_delete=models.SET_NULL)
    numero = models.IntegerField(default=1)
    identificador_bs = models.CharField(max_length=120, null=True, blank=True)
    semestre = models.CharField(max_length=20, null=False, blank=False)

    def consultar_rubricas(self):
        """Retorna las rúbricas asociadas a la sección"""
        return self.rubricaseccion_set.all()

    def consultar_items(self):
        """Retorna los ítems de calificación de la sección"""
        return self.itemcalificacionseccion_set.all()

    def __str__(self):
        return self.semestre + ": " + str(self.curso.codigo) +  ", Secc. " + str(self.numero)

    def buscar_por_numero(curso: Curso, numero: int):
        """
        Busca la Sección del curso dado, con el número dado y la retorna
        Si no la encuentra, retorna None
        """
        try:
            return Seccion.objects.get(curso=curso, numero=numero)
        except:
            return None

    def consultar_estudiantes(self):
        return self.estudiante_set.all()


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
