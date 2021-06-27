# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rubricas.decorators import acceso_restringido

import rubricas.utils as utils
from rubricas.constantes import PROFESOR

from rubricas.models.usuarios import Estudiante
from rubricas.models.secciones import Seccion
from rubricas.models.resultados import ResultadoRubrica
from rubricas.models.estadisticas import ResumenEstudianteSeccion



@acceso_restringido(tipo_usuario=[PROFESOR])
def listar_secciones(request):
    # profesor = utils.reconstruir_profesor(request)

    template_name = "rubricas/secciones/lista_secciones.html"
    context = {"titulo" : "Secciones actuales", "descripciones": "Listado de secciones del semestre actual"}

    return utils.render_page(request, template_name, context)

@acceso_restringido(tipo_usuario=[PROFESOR])
def listar_secciones_historicas(request):
    profesor = utils.reconstruir_profesor(request)
    historicas = profesor.buscar_secciones_historicas()
    template_name = "rubricas/secciones/lista_secciones.html"
    context = {"historicas" : historicas, "titulo" : "Historial de secciones",  "descripciones": "Listado histórico de secciones"}

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=[PROFESOR])
def seccion(request, id_seccion):
    seccion = get_object_or_404(Seccion, id=id_seccion)
    rubricas = seccion.consultar_rubricas()
    items = seccion.consultar_items()

    estudiantes = seccion.consultar_estudiantes()
    for estudiante in estudiantes:
        estudiante.resumen = ResumenEstudianteSeccion.buscar_resumen(estudiante, seccion)
        estudiante.ultimo_resultado = estudiante.resumen.ultimo_resultado

    template_name = "rubricas/secciones/detalle_seccion.html"
    context = {"seccion": seccion, "rubricas": rubricas, "items": items, "estudiantes": estudiantes }

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=[PROFESOR])
def estudiante_seccion(request, id_estudiante, id_seccion):
    seccion = get_object_or_404(Seccion, id=id_seccion)
    estudiante = get_object_or_404(Estudiante, id=id_estudiante)
    estudiante.resumen = ResumenEstudianteSeccion.buscar_resumen(estudiante, seccion)

    resultados = []
    items = seccion.consultar_items()
    for item in items:
        resultado = ResultadoRubrica.buscar_resultado_estudiante_item(estudiante, item)
        resultados.append((item, resultado))

    template_name = "rubricas/estudiantes/detalle_estudiante.html"
    context = {"seccion": seccion, "items": items, "estudiante": estudiante, "resultados": resultados }

    return utils.render_page(request, template_name, context)