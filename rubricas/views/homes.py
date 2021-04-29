from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json

import rubricas.utils as utils
#from rubricas.models.usuarios import Usuario
#from rubricas.constantes import PROFESOR, ESTUDIANTE, ADMINISTRADOR, MONITOR, COORDINADOR, SEMESTRE_ACTUAL


def home(request):
    return home_estudiante(request)


def home_estudiante(request):
    template_name = "rubricas/homes/home_estudiante.html"
    context = {
    }

    return utils.render_page(request, template_name, context)
