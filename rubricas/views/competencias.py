from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rubricas.decorators import acceso_restringido

import rubricas.utils as utils
from rubricas.constantes import PROFESOR

from rubricas.models.competencias import GrupoCompetencia, Competencia
from rubricas.models.secciones import Programa, Curso


def competencias(request):
    return competencias_home(request)


def competencias_home(request):
    template_name = "rubricas/competencias/competencias_home.html"
    context = {}

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=[PROFESOR])
def competencia_programa(request, id_competencia, id_programa):
    comp = get_object_or_404(Competencia, id=id_competencia)
    rubricas_programa = comp.buscar_rubricas_competencia_programa(id_programa)

    programa = get_object_or_404(Programa, id=id_programa)
    cursos = programa.consultar_cursos_programa()

    rubricas_cursos = {}
    for curso in cursos:
        rubricas = comp.buscar_rubricas_competencia_curso(curso.id)
        rubricas_cursos[curso] = rubricas

    template_name = "rubricas/competencias/detalle_competencia.html"
    context = {"competencia": comp, "rubricas_programa": rubricas_programa, "rubricas_cursos": rubricas_cursos}

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=[PROFESOR])
def competencia_curso(request, id_competencia, id_curso):
    comp = get_object_or_404(Competencia, id=id_competencia)
    curso = get_object_or_404(Curso, id=id_curso)
    rubricas = comp.buscar_rubricas_competencia_curso(curso.id)
    rubricas_cursos = {curso: rubricas}

    template_name = "rubricas/competencias/detalle_competencia.html"
    context = {"competencia": comp, "rubricas_cursos": rubricas_cursos}

    return utils.render_page(request, template_name, context)
