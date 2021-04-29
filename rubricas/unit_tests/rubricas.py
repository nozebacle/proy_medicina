# -*- coding: utf-8 -*-

from rubricas.models.temas import Patologia, Procedimiento
from rubricas.models.secciones import Programa, Curso, Seccion
from rubricas.models.rubricas import Rubrica, Criterio, NivelCriterio, ItemCalificacionCurso, ItemCalificacionSeccion
from rubricas.models.apes import APE
from rubricas.models.competencias import Competencia

def crear_rubricas():
    print("Creando rúbricas")
    Rubrica.objects.all().delete()

    r = Rubrica()
    r.nombre = "Rúbrica de Enfermería Piso"
    r.nombre_interno = r.nombre
    r.descripcion = "Desempeño del residente en rotación según el/la jefe de enfermería del piso"
    r.comentarios = "Rúbrica de prueba"
    r.debe_tener_procedimientos = True
    r.debe_tener_patologias = True
    r.save()

    r.programa = Programa.buscar_por_codigo("PEDI")
    curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20")
    r.secciones.add(Seccion.buscar_por_numero(curso, "1"))

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
    n1.nombre="No está preparado"
    n1.descripcion = "Información es insuficiente o exhaustiva. A veces omite datos relevantes o se desvía del problema principal. El examen físico es incompleto u omite detalles relevantes para el problema principal. "
    n1.puntos = 0
    n1.numero = 1
    n1.criterio = cr1
    n1.save()

    n2 = NivelCriterio()
    n2.nombre="Aceptable"
    n2.descripcion = "La información es completa, cronológica y estructurada, describe el estado del paciente y los hallazgos principales. Conoce e interpreta las pruebas diagnosticas esenciales. Tiene en cuenta riesgos, beneficios y las preferencias del paciente."
    n2.puntos = 0
    n2.numero = 2
    n2.criterio = cr1
    n2.save()

    n3 = NivelCriterio()
    n3.nombre="Lo hace bien"
    n3.descripcion = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    n3.puntos = 8
    n3.numero = 3
    n3.criterio = cr1
    n3.save()


    n4 = NivelCriterio()
    n4.nombre="Ejemplar"
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
    n1.nombre="No está preparado"
    n1.descripcion = "Falla en la evaluación de valores antropométricos y percentil. No tiene en cuenta o es incompleta la valoración del estado nutricional, la alimentación, salud bucal, ocular, auditiva, identificación sexual."
    n1.puntos = 0
    n1.numero = 1
    n1.criterio = cr2
    n1.save()

    n2 = NivelCriterio()
    n2.nombre="Aceptable"
    n2.descripcion = "Tiene en cuenta valores antropométricos, analiza percentil; hace una valoración aceptable del estado nutricional, la alimentación, salud boca, ocular, auditiva, identificación sexual."
    n2.puntos = 0
    n2.numero = 2
    n2.criterio = cr2
    n2.save()

    n3 = NivelCriterio()
    n3.nombre="Lo hace bien"
    n3.descripcion = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    n3.puntos = 8
    n3.numero = 3
    n3.criterio = cr2
    n3.save()


    n4 = NivelCriterio()
    n4.nombre="Ejemplar"
    n4.descripcion = "Toma valores antropométricos, analiza percentil; valora el estado de salud: nutricional, la alimentación, salud bucal los hábitos y practica, hace evaluación ocular (movimiento, fijación, etc.), auditiva, identificación sexual."
    n4.puntos = 10
    n4.numero = 4
    n4.criterio = cr2
    n4.save()



