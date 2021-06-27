# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rubricas.decorators import acceso_restringido

import rubricas.utils as utils
from rubricas.constantes import PROFESOR

from rubricas.models.usuarios import Estudiante
from rubricas.models.secciones import Curso
from rubricas.models.rubricas import Rubrica, RubricaCurso, RubricaSeccion, ItemCalificacionSeccion


@acceso_restringido(tipo_usuario=[PROFESOR])
def rubrica_curso(request, id_rubrica, id_curso):
    rubrica = get_object_or_404(Rubrica, id=id_rubrica)
    curso = get_object_or_404(Curso, id=id_curso)

    print(rubrica)

    template_name = "rubricas/rubricas/detalle_rubrica.html"
    context = {"rubrica": rubrica, "curso": curso}

    return utils.render_page(request, template_name, context)

@acceso_restringido(tipo_usuario=[PROFESOR])
def rubrica_curso(request, id_rubrica, id_curso):
    rubrica = get_object_or_404(Rubrica, id=id_rubrica)
    curso = get_object_or_404(Curso, id=id_curso)

    print(rubrica)

    template_name = "rubricas/rubricas/detalle_rubrica.html"
    context = {"rubrica": rubrica, "curso": curso}

    return utils.render_page(request, template_name, context)

@acceso_restringido(tipo_usuario=[PROFESOR])
def evaluar(request):
    #rubrica = get_object_or_404(Rubrica, id=id_rubrica)
    #curso = get_object_or_404(Curso, id=id_curso)

    item = ItemCalificacionSeccion.objects.last()
    rubrica = item.rubrica
    estudiante = Estudiante.objects.last()

    template_name = "rubricas/rubricas/forma_rubrica.html"
    context = {"item": item, "rubrica": rubrica, "estudiante": estudiante}

    return utils.render_page(request, template_name, context)

