from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json

import rubricas.utils as utils

def competencias(request):
    return competencias_home(request)


def competencias_home(request):
    template_name = "rubricas/competencias/competencias_home.html"
    context = {
    }

    return utils.render_page(request, template_name, context)
