# -*- coding: utf-8 -*-

from rubricas.models.secciones import Programa, Curso, Seccion
from rubricas.models.apes import APE
from rubricas.models.competencias import Competencia

def crear_programa():
    print("Creando programa")
    Programa.objects.all().delete()

    pr = Programa()
    pr.nombre = "Pediatría"
    pr.codigo = "PEDI"
    pr.save()

    # Poniéndole APEs al programa
    pr.apes.add(APE.buscar_por_sigla("APE1"))
    pr.apes.add(APE.buscar_por_sigla("APE2"))
    pr.apes.add(APE.buscar_por_sigla("APE3"))
    pr.apes.add(APE.buscar_por_sigla("APE4"))
    pr.apes.add(APE.buscar_por_sigla("APE5"))
    pr.apes.add(APE.buscar_por_sigla("APE6"))
    pr.apes.add(APE.buscar_por_sigla("APE7"))
    pr.apes.add(APE.buscar_por_sigla("APE8"))
    pr.apes.add(APE.buscar_por_sigla("APE9"))
    pr.apes.add(APE.buscar_por_sigla("APE10"))
    pr.apes.add(APE.buscar_por_sigla("APE11"))
    pr.apes.add(APE.buscar_por_sigla("APE12"))
    pr.save()

    # Poniéndole Competencias al programa
    pr.competencias.add(Competencia.buscar_por_sigla("HC1"))
    pr.competencias.add(Competencia.buscar_por_sigla("HC2"))
    pr.competencias.add(Competencia.buscar_por_sigla("HC3"))
    pr.save()



def crear_cursos():
    print("Creando cursos")
    Curso.objects.all().delete()

    pr = Curso()
    pr.nombre = "Hospitalización 1"
    pr.nombre_interno = "Hospitalización 1 v202020"
    pr.codigo = "PEDI-5101"
    pr.semestre = "2020-20"
    pr.programa = Programa.buscar_por_codigo("PEDI")
    pr.descripcion = "Las rotaciones clínicas permiten que el residente tenga contacto y bajo supervisión atienda pacientes con las patologías frecuentes de un área o subespecialidad específica, aprenda a usar las pruebas, los procedimientos diagnósticos, el tratamiento integral de estas patologías o situaciones clínicas."
    pr.save()

    # Poniéndole APEs al curso
    pr.apes.add(APE.buscar_por_sigla("APE1"))
    pr.apes.add(APE.buscar_por_sigla("APE2"))
    pr.apes.add(APE.buscar_por_sigla("APE3"))
    pr.apes.add(APE.buscar_por_sigla("APE4"))
    pr.apes.add(APE.buscar_por_sigla("APE9"))
    pr.apes.add(APE.buscar_por_sigla("APE11"))
    pr.apes.add(APE.buscar_por_sigla("APE12"))
    pr.save()

    # Poniéndole Competencias al curso
    pr.competencias.add(Competencia.buscar_por_sigla("HC1"))
    pr.competencias.add(Competencia.buscar_por_sigla("HC3"))
    pr.save()

def crear_secciones():
    print("Creando secciones")
    Seccion.objects.all().delete()

    curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20")
    s1 = Seccion()
    s1.curso = curso
    s1.numero = 1
    s1.save()

    s2 = Seccion()
    s2.curso = curso
    s2.numero = 2
    s2.save()










