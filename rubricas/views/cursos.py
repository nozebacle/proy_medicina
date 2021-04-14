from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json
import rubricas.utils as utils


def cursos(request):
    return cursos_estudiante(request)

def cursos_estudiante(request):
    template_name = "rubricas/cursos/cursos_estudiante.html"
    context = {
    }
    return utils.render_page(request, template_name, context)

def curso_especifico(request):
    template_name = "rubricas/cursos/especifico.html"
    context = {
    }
    return utils.render_page(request, template_name, context)

def rubrica_g(request):
    template_name = "rubricas/cursos/rubrica_g.html"
    context = {
    }
    return utils.render_page(request, template_name, context)

def rubrica_c(request):
    template_name = "rubricas/cursos/rubrica_c.html"
    context = {
    }
    return utils.render_page(request, template_name, context)
