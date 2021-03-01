from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json

import rubricas.utils as utils
#from rubricas.models.usuarios import Usuario
#from rubricas.constantes import PROFESOR, ESTUDIANTE, ADMINISTRADOR, MONITOR, COORDINADOR, SEMESTRE_ACTUAL


#def home(request):
def cursos(request):
    return cursos_estudiante(request)


def cursos_estudiante(request):
    template_name = "rubricas/cursos/cursos_estudiante.html"
    context = {
    }

    return utils.render_page(request, template_name, context)
