# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rubricas.decorators import acceso_restringido

import json

import rubricas.utils as utils
from rubricas.constantes import PROFESOR

from rubricas.models.secciones import Programa


@acceso_restringido(tipo_usuario=[PROFESOR])
def listar_programas(request):
    profesor = utils.reconstruir_profesor(request)
    programas = Programa.buscar_por_profesor(1)  # TODO (profesor.id)

    template_name = "rubricas/programas/lista_programas.html"
    context = {"programas": programas}

    return utils.render_page(request, template_name, context)
