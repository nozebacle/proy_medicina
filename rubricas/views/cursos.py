# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rubricas.decorators import acceso_restringido

import rubricas.utils as utils
from rubricas.constantes import PROFESOR

from rubricas.models.secciones import Programa, Curso
from rubricas.models.rubricas import RubricaCurso


@acceso_restringido(tipo_usuario=[PROFESOR])
def curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    rubricas = curso.consultar_rubricas()
    items = curso.consultar_items()

    template_name = "rubricas/cursos/detalle_curso.html"
    context = {"curso": curso, "rubricas": rubricas, "items": items}

    return utils.render_page(request, template_name, context)


def cursos(request):
    return cursos_estudiante(request)


def cursos_estudiante(request):
    template_name = "rubricas/cursos/cursos_estudiante.html"
    context = {}
    return utils.render_page(request, template_name, context)


def curso_especifico(request):
    template_name = "rubricas/cursos/especifico.html"
    context = {}
    return utils.render_page(request, template_name, context)


def rubrica_g(request):
    template_name = "rubricas/cursos/rubrica_g.html"
    context = {}
    return utils.render_page(request, template_name, context)


def rubrica_c(request):
    template_name = "rubricas/cursos/rubrica_c.html"
    context = {}
    return utils.render_page(request, template_name, context)
