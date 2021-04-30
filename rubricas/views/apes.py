from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json
import rubricas.utils as utils
from rubricas.models.apes import APE
from rubricas.models.secciones import Programa

def apes(request):
    return apes_home(request)


def apes_home(request, cod_programa):
    # todas_las_apes = APE.objects.all()
    programa = Programa.buscar_por_codigo(cod_programa)
    las_apes = APE.buscar_por_programa(programa)

    template_name = "rubricas/apes/apes_home.html"
    context = {
        'apes' : las_apes
    }
    print(las_apes)

    return utils.render_page(request, template_name, context)
