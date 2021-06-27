from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json

import rubricas.utils as utils
import rubricas.views.secciones as secciones


def home(request):
    return home_profesor(request)


def home_estudiante(request):
    template_name = "rubricas/homes/home_estudiante.html"
    context = {}

    return utils.render_page(request, template_name, context)


def home_profesor(request):
    return secciones.listar_secciones(request)
