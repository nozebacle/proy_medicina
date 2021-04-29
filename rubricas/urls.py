from django.urls import path

import rubricas.views.homes as homes
import rubricas.views.cursos as cursos
import rubricas.views.apes as apes
import rubricas.views.competencias as competencias

urlpatterns = [
    path("home/", homes.home, name="home"),
    path("cursos/", cursos.cursos, name="cursos"),
    path("cursos/especifico/", cursos.curso_especifico, name="especifico"),
    path("cursos/rubrica_g/", cursos.rubrica_g, name="rubrica_g"),
    path("cursos/rubrica_c/", cursos.rubrica_c, name="rubrica_c"),
    path("apes/", apes.apes, name="apes"),
    path("competencias/", competencias.competencias, name="competencias"),
    ]
