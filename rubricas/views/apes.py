from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse

import json
import rubricas.utils as utils


def apes(request):
    return apes_home(request)


def apes_home(request):
    template_name = "rubricas/apes/apes_home.html"
    context = {
    }

    return utils.render_page(request, template_name, context)
