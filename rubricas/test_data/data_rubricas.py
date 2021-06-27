# -*- coding: utf-8 -*-

import random

from rubricas.models.temas import Patologia, Procedimiento
from rubricas.models.secciones import Programa, Curso, Seccion
from rubricas.models.rubricas import (
    RubricaCurso,
    RubricaSeccion,
    Criterio,
    NivelCriterio,
    ItemCalificacionCurso,
    ItemCalificacionSeccion,
)
from rubricas.models.apes import APE
from rubricas.models.competencias import Competencia


def crear_rubricas(borrar=True):
    print("Creando rúbricas")

    if borrar:
        RubricaSeccion.objects.all().delete()

    r = RubricaSeccion()
    r.nombre = "Rúbrica de Enfermería Piso"
    r.nombre_interno = r.nombre
    r.descripcion = "Desempeño del residente en rotación según el/la jefe de enfermería del piso"
    r.comentarios = "Rúbrica de prueba"
    r.debe_tener_procedimientos = True
    r.debe_tener_patologias = True
    r.save()

    r.programa = Programa.buscar_por_codigo("PEDI")
    curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20")
    r.seccion = Seccion.buscar_por_numero(curso, "1")

    r.patologias.add(Patologia.buscar_por_codigo("A001"))
    r.patologias.add(Patologia.buscar_por_codigo("A009"))

    r.procedimientos.add(Procedimiento.buscar_por_codigo("01.0"))
    r.procedimientos.add(Procedimiento.buscar_por_codigo("01.0.9"))

    r.save()

    icc = ItemCalificacionCurso()
    icc.nombre = r.nombre + " - Semana 1"
    icc.peso = 10
    icc.rubrica = r
    icc.curso = curso
    icc.save()

    icc = ItemCalificacionCurso()
    icc.nombre = r.nombre + " - Semana 2"
    icc.peso = 10
    icc.rubrica = r
    icc.curso = curso
    icc.save()

    icc = ItemCalificacionCurso()
    icc.nombre = r.nombre + " - Semana 3"
    icc.peso = 10
    icc.rubrica = r
    icc.curso = curso
    icc.save()

    ics = ItemCalificacionSeccion()
    ics.nombre = r.nombre + " - Semana 1"
    ics.peso = 10
    ics.rubrica = r
    ics.seccion = Seccion.buscar_por_numero(curso, "1")
    ics.save()

    ics = ItemCalificacionSeccion()
    ics.nombre = r.nombre + " - Semana 2"
    ics.peso = 10
    ics.rubrica = r
    ics.seccion = Seccion.buscar_por_numero(curso, "1")
    ics.save()

    ics = ItemCalificacionSeccion()
    ics.nombre = r.nombre + " - Semana 3"
    ics.peso = 10
    ics.rubrica = r
    ics.seccion = Seccion.buscar_por_numero(curso, "1")
    ics.save()

    print("Creando criterios")
    Criterio.objects.all().delete()

    cr1 = Criterio()
    cr1.nombre_interno = "Historia clínica"
    cr1.descripcion = "Hace una historia clínica completa y detallada del paciente pediátrico. Identifica y prioriza los diagnósticos diferenciales, conoce y usa adecuadamente las pruebas diagnosticas indicadas."
    cr1.rubrica = r
    cr1.numero = 1
    cr1.save()

    cr1.apes.add(APE.buscar_por_sigla("APE1"))
    cr1.apes.add(APE.buscar_por_sigla("APE2"))
    cr1.apes.add(APE.buscar_por_sigla("APE3"))
    cr1.competencias.add(Competencia.buscar_por_sigla("HC1"))
    cr1.competencias.add(Competencia.buscar_por_sigla("HC3"))
    cr1.save()

    n1 = NivelCriterio()
    n1.nombre = "No está preparado"
    n1.descripcion = "Información es insuficiente o exhaustiva. A veces omite datos relevantes o se desvía del problema principal. El examen físico es incompleto u omite detalles relevantes para el problema principal. "
    n1.puntos = 0
    n1.numero = 1
    n1.criterio = cr1
    n1.save()

    n2 = NivelCriterio()
    n2.nombre = "Aceptable"
    n2.descripcion = "La información es completa, cronológica y estructurada, describe el estado del paciente y los hallazgos principales. Conoce e interpreta las pruebas diagnosticas esenciales. Tiene en cuenta riesgos, beneficios y las preferencias del paciente."
    n2.puntos = 0
    n2.numero = 2
    n2.criterio = cr1
    n2.save()

    n3 = NivelCriterio()
    n3.nombre = "Lo hace bien"
    n3.descripcion = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    n3.puntos = 8
    n3.numero = 3
    n3.criterio = cr1
    n3.save()

    n4 = NivelCriterio()
    n4.nombre = "Ejemplar"
    n4.descripcion = "La información es completa, cronológica y estructurada, describe el estado del paciente y los hallazgos principales, hace un plan de estudio razonado, coherente. Conoce, prioriza e interpreta las pruebas diagnosticas, las usa para el diagnostico, gravedad y seguimiento. Tiene en cuenta riesgos, beneficios y las preferencias del paciente."
    n4.puntos = 10
    n4.numero = 4
    n4.criterio = cr1
    n4.save()

    cr2 = Criterio()
    cr2.nombre_interno = "Registro valores"
    cr2.descripcion = "Toma valores antropométricos, analiza percentil; valora el estado nutricional, la alimentación, salud bucal los hábitos y practica, hace evaluación ocular, auditiva, identificación sexual."
    cr2.rubrica = r
    cr2.numero = 2
    cr2.save()

    cr2.apes.add(APE.buscar_por_sigla("APE1"))
    cr2.apes.add(APE.buscar_por_sigla("APE2"))
    cr2.apes.add(APE.buscar_por_sigla("APE3"))
    cr2.apes.add(APE.buscar_por_sigla("APE4"))
    cr2.apes.add(APE.buscar_por_sigla("APE7"))
    cr2.competencias.add(Competencia.buscar_por_sigla("HC1"))
    cr2.competencias.add(Competencia.buscar_por_sigla("HC2"))
    cr2.save()

    n1 = NivelCriterio()
    n1.nombre = "No está preparado"
    n1.descripcion = "Falla en la evaluación de valores antropométricos y percentil. No tiene en cuenta o es incompleta la valoración del estado nutricional, la alimentación, salud bucal, ocular, auditiva, identificación sexual."
    n1.puntos = 0
    n1.numero = 1
    n1.criterio = cr2
    n1.save()

    n2 = NivelCriterio()
    n2.nombre = "Aceptable"
    n2.descripcion = "Tiene en cuenta valores antropométricos, analiza percentil; hace una valoración aceptable del estado nutricional, la alimentación, salud boca, ocular, auditiva, identificación sexual."
    n2.puntos = 0
    n2.numero = 2
    n2.criterio = cr2
    n2.save()

    n3 = NivelCriterio()
    n3.nombre = "Lo hace bien"
    n3.descripcion = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    n3.puntos = 8
    n3.numero = 3
    n3.criterio = cr2
    n3.save()

    n4 = NivelCriterio()
    n4.nombre = "Ejemplar"
    n4.descripcion = "Toma valores antropométricos, analiza percentil; valora el estado de salud: nutricional, la alimentación, salud bucal los hábitos y practica, hace evaluación ocular (movimiento, fijación, etc.), auditiva, identificación sexual."
    n4.puntos = 10
    n4.numero = 4
    n4.criterio = cr2
    n4.save()


def crear_rubricas_curso_muestra(borrar=True):
    print("Creando rúbricas para los cursos del programa muestra (DEMO)")

    programa = Programa.buscar_por_codigo("DEMO")
    cursos = programa.consultar_cursos_programa()

    if borrar:
        for curso in cursos:
            rubricas = curso.consultar_rubricas()
            for rubrica in rubricas:
                criterios = rubrica.criterio_set.all()
                for criterio in criterios:
                    niveles = criterio.nivelcriterio_set.all()
                    for nivel in niveles:
                        nivel.delete()
                    criterio.delete()
                rubrica.delete()

    niveles = ["No está preparado", "Aceptable", "Lo hace bien", "Ejemplar"]
    for curso in cursos:
        print(f"Creando rubricas para {curso.codigo}")
        apes = list(curso.consultar_apes())
        competencias = list(curso.consultar_competencias())
        num_rubricas = random.randint(3, 7)
        porcentajes_items = generar_porcentajes_items(num_rubricas, 5)

        for nr in range(num_rubricas):
            letra = chr(ord("A") + nr)
            rubrica = crear_rubrica_muestra(
                f"R. Evaluación Tipo-{letra} ({curso.codigo})", curso, True, True, 5, niveles, apes, competencias
            )
            pesos = porcentajes_items[nr]
            for numero in range(len(pesos)):
                peso = pesos[numero]
                crear_item_calificacion(rubrica, curso, f"Evaluación {letra}", peso, numero + 1)


def crear_item_calificacion(rubrica, curso, nombre, peso, numero):
    icc = ItemCalificacionCurso()
    icc.nombre = f"{nombre} - Semana {numero}"
    icc.peso = peso
    icc.rubrica = rubrica
    icc.curso = curso
    icc.save()


def crear_rubrica_muestra(
    nombre, curso, con_patologias, con_procedimientos, num_criterios, niveles, apes, competencias
):
    r = RubricaCurso()
    r.nombre = nombre
    r.nombre_interno = nombre
    r.descripcion = f"Rubrica para medir el desempeño del residente en la evaluación {nombre}"
    r.comentarios = "Esta es una rúbrica de prueba, generada automáticamente para las pruebas"
    r.debe_tener_patologias = con_patologias
    r.debe_tener_procedimientos = con_procedimientos
    r.save()

    r.agregar_curso(curso)
    r.save()

    # r.patologias.add(Patologia.buscar_por_codigo("A001"))
    # r.patologias.add(Patologia.buscar_por_codigo("A009"))
    # r.procedimientos.add(Procedimiento.buscar_por_codigo("01.0"))
    # r.procedimientos.add(Procedimiento.buscar_por_codigo("01.0.9"))

    apes_rubrica = set()
    comps_rubrica = set()

    for num in range(1, num_criterios + 1):
        cr = Criterio()
        cr.nombre_interno = f"Criterio {num} de {nombre} en {curso.codigo}"
        cr.descripcion = f"Descripción detallada del criterio {num} que explica de qué se trata el criterio y qué se está intentando evaluar."
        cr.rubrica = r
        cr.numero = num
        cr.save()

        selected_apes = random.sample(apes, random.randint(0, len(apes)))
        for ape in selected_apes:
            cr.agregar_ape(ape)
            apes_rubrica.add(ape)

        selected_comps = random.sample(competencias, random.randint(0, len(competencias)))
        for comp in selected_comps:
            cr.agregar_competencia(comp)
            comps_rubrica.add(comp)

        cr.save()

        puntos_por_nivel = random.randint(1, 5)

        for n in range(len(niveles)):
            nivel = NivelCriterio()
            nivel.nombre = niveles[n]
            nivel.descripcion = f"El estudiante que se encuentra en este nivel (el nivel {n}) se comportó de una cierta forma que lo ubica en la categoría '{niveles[n]}' para este criterio particular."
            nivel.puntos = puntos_por_nivel * n
            nivel.numero = n
            nivel.criterio = cr
            nivel.save()

    for ape in apes_rubrica:
        r.agregar_ape(ape)

    for comp in comps_rubrica:
        r.agregar_competencia(comp)

    r.save()
    return r


def generar_porcentajes_items(grupos: int, maximo_por_grupo: int = 1) -> list:
    rangos_grupos = []
    acumulado = 0
    for i in range(grupos - 1):
        siguiente = random.randint(acumulado + 1, 18 - grupos + i)
        rangos_grupos.append(siguiente * 5)
        acumulado = siguiente
    rangos_grupos.append(100)

    porcentajes_items = []
    base = 0
    for i in range(len(rangos_grupos)):
        grupo = []
        porcentajes_items.append(grupo)

        siguiente = rangos_grupos[i]
        porcentaje_grupo = siguiente - base
        num_items = random.randint(1, maximo_por_grupo)

        if num_items > 1:
            porc_item = porcentaje_grupo // num_items
            total = 0
            for _ in range(num_items):
                grupo.append(porc_item)
                total += porc_item

            if total < porcentaje_grupo:
                grupo[-1] += porcentaje_grupo - total

        else:
            grupo.append(porcentaje_grupo)

        base = siguiente

    total = 0
    for grupo in porcentajes_items:
        for item in grupo:
            total += item

    return porcentajes_items
