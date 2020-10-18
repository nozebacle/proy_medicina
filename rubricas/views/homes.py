from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json
import rubricas.utils as utils
from rubricas.models.usuarios import Usuario
from rubricas.constantes import PROFESOR, ESTUDIANTE, ADMINISTRADOR, MONITOR, COORDINADOR, SEMESTRE_ACTUAL


@acceso_autenticado()
def home(request):
    usuario = get_object_or_404(Usuario, pk=request.session["id_usuario"])
    tipo = usuario.tipo
    if tipo == ESTUDIANTE:
        return home_estudiante(request)
    elif tipo == PROFESOR:
        return home_profesor(request)
    elif tipo == ADMINISTRADOR:
        return home_admin(request)
    elif tipo == MONITOR:
        return home_monitor(request)
    elif tipo == COORDINADOR:
        return home_coordinador(request)


@acceso_restringido(tipo_usuario=ESTUDIANTE)
def home_estudiante(request):
    estudiante = utils.reconstruir_estudiante(request)

   
    template_name = "dashboard/homes/home_estudiante.html"
    context = {
    }

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=PROFESOR)
def home_profesor(request):
    profesor = utils.reconstruir_profesor(request)

    template_name = "dashboard/homes/home_profesor.html"
    context = {
    }

    return utils.render_page(request, template_name, context)
    

def home_monitor(request):
    template_name = "dashboard/homes/home_monitor.html"
    context = {}
    return utils.render_page(request, template_name, context)


def home_admin(request):
    template_name = "dashboard/homes/home_admin.html"
    context = {}
    return utils.render_page(request, template_name, context)


def home_coord(request):
    template_name = "dashboard/homes/home_coord.html"
    context = {}
    return utils.render_page(request, template_name, context)
