# -*- coding: utf-8 -*-

from rubricas.models.secciones import Programa, Curso, Seccion
from rubricas.models.apes import APE
from rubricas.models.competencias import Competencia


def crear_todo(borrar=True):
    crear_programa(borrar)
    crear_cursos(borrar)
    crear_secciones(borrar)
    crear_estructura_muestra(borrar)


def crear_programa(borrar=True):
    print("Creando programa")

    if borrar:
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


def crear_cursos(borrar=True):
    print("Creando cursos")

    if borrar:
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


def crear_secciones(borrar=True):
    print("Creando secciones")

    if borrar:
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


def crear_estructura_muestra(borrar=True):
    print("Creando programa muestra (DEMO)")

    if borrar:
        viejo = Programa.buscar_por_codigo("DEMO")
        if viejo is not None:
            cursos = viejo.consultar_cursos_programa()
            for curso in cursos:
                curso.delete()
            viejo.delete()

    pr = Programa()
    pr.nombre = "Programa muestra"
    pr.codigo = "DEMO"
    pr.save()

    # Poniéndole APEs al programa
    pr.apes.add(APE.buscar_por_sigla("APE1"))
    pr.apes.add(APE.buscar_por_sigla("APE2"))
    pr.apes.add(APE.buscar_por_sigla("APE3"))
    pr.apes.add(APE.buscar_por_sigla("APE4"))
    pr.save()

    # Poniéndole Competencias al programa
    pr.competencias.add(Competencia.buscar_por_sigla("CPP1"))
    pr.competencias.add(Competencia.buscar_por_sigla("CPP1"))
    pr.competencias.add(Competencia.buscar_por_sigla("CPP4"))
    pr.competencias.add(Competencia.buscar_por_sigla("HC1"))
    pr.competencias.add(Competencia.buscar_por_sigla("HC2"))
    pr.competencias.add(Competencia.buscar_por_sigla("HC3"))
    pr.competencias.add(Competencia.buscar_por_sigla("ABP1"))
    pr.competencias.add(Competencia.buscar_por_sigla("ABP2"))
    pr.competencias.add(Competencia.buscar_por_sigla("ABP3"))
    pr.competencias.add(Competencia.buscar_por_sigla("ABP4"))
    pr.competencias.add(Competencia.buscar_por_sigla("ABP5"))
    pr.competencias.add(Competencia.buscar_por_sigla("ABP6"))
    pr.competencias.add(Competencia.buscar_por_sigla("C1"))
    pr.competencias.add(Competencia.buscar_por_sigla("C2"))
    pr.competencias.add(Competencia.buscar_por_sigla("C4"))
    pr.competencias.add(Competencia.buscar_por_sigla("C6"))
    pr.competencias.add(Competencia.buscar_por_sigla("C7"))

    pr.save()

    print("Creando cursos para DEMO")

    c1 = crear_curso_programa(
        "DEMO-0001", "Curso Muestra I", "2020-20", "DEMO", pr.consultar_apes(), pr.consultar_competencias()
    )
    c2 = crear_curso_programa(
        "DEMO-0002", "Curso Muestra II", "2020-20", "DEMO", pr.consultar_apes(), pr.consultar_competencias()
    )
    c3 = crear_curso_programa(
        "DEMO-0003", "Curso Muestra III", "2020-20", "DEMO", pr.consultar_apes(), pr.consultar_competencias()
    )
    c4 = crear_curso_programa(
        "DEMO-0004", "Curso Muestra IV", "2020-20", "DEMO", pr.consultar_apes(), pr.consultar_competencias()
    )


def crear_curso_programa(codigo, nombre, semestre, codigo_programa="DEMO", apes=[], competencias=[]):
    c = Curso()
    c.nombre = nombre
    c.nombre_interno = f"{nombre} v{semestre}"
    c.codigo = codigo
    c.semestre = semestre
    c.programa = Programa.buscar_por_codigo(codigo_programa)
    c.descripcion = f"El curso >{c.nombre}< para el programa, para el semestre {c.semestre}"
    c.save()

    for ape in apes:
        c.agregar_ape(ape)

    for comp in competencias:
        c.agregar_competencia(comp)

    c.save()

    return c
