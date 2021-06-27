from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rubricas.decorators import acceso_restringido

import rubricas.utils as utils
from rubricas.constantes import PROFESOR

from rubricas.models.apes import APE
from rubricas.models.secciones import Programa, Curso


def apes(request):
    return apes_home(request)


def apes_home(request, cod_programa):
    # todas_las_apes = APE.objects.all()
    programa = Programa.buscar_por_codigo(cod_programa)
    las_apes = APE.buscar_por_programa(programa)

    template_name = "rubricas/apes/apes_home.html"
    context = {"apes": las_apes}
    print(las_apes)

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=[PROFESOR])
def ape_programa(request, id_ape, id_programa):
    ape = get_object_or_404(APE, id=id_ape)
    rubricas_programa = ape.buscar_rubricas_ape_programa(id_programa)

    programa = get_object_or_404(Programa, id=id_programa)
    cursos = programa.consultar_cursos_programa()

    rubricas_cursos = {}
    for curso in cursos:
        rubricas = ape.buscar_rubricas_ape_curso(curso.id)
        rubricas_cursos[curso] = rubricas

    template_name = "rubricas/apes/detalle_ape.html"
    context = {"ape": ape, "rubricas_programa": rubricas_programa, "rubricas_cursos": rubricas_cursos}

    return utils.render_page(request, template_name, context)


@acceso_restringido(tipo_usuario=[PROFESOR])
def ape_curso(request, id_ape, id_curso):
    ape = get_object_or_404(APE, id=id_ape)
    curso = get_object_or_404(Curso, id=id_curso)
    rubricas = ape.buscar_rubricas_ape_curso(curso.id)
    rubricas_cursos = {curso: rubricas}

    template_name = "rubricas/apes/detalle_ape.html"
    context = {"ape": ape, "rubricas_cursos": rubricas_cursos}

    return utils.render_page(request, template_name, context)
