from django.urls import path

import rubricas.views.autenticacion as auth
import rubricas.views.homes as homes

import rubricas.views.programas as programas
import rubricas.views.apes as apes
import rubricas.views.competencias as competencias
import rubricas.views.rubricas as rubs
import rubricas.views.cursos as cursos
import rubricas.views.secciones as secciones

urlpatterns = [
    path("", auth.login, name="initial"),
    path("login/", auth.login, name="login"),
    path("logout/", auth.logout, name="logout"),
    path("home", homes.home, name="home"),
    path("cursos", cursos.cursos, name="cursos"),
    path("cursos/especifico", cursos.curso_especifico, name="especifico"),
    path("cursos/rubrica_g", cursos.rubrica_g, name="rubrica_g"),
    path("cursos/rubrica_c", cursos.rubrica_c, name="rubrica_c"),
    path("apes/<str:cod_programa>", apes.apes_home, name="apes"),
    path("competencias", competencias.competencias, name="competencias"),
    path("programas", programas.listar_programas, name="programas"),
    path("apes/programa/<int:id_ape>/<int:id_programa>", apes.ape_programa, name="ape_programa"),
    path("apes/curso/<int:id_ape>/<int:id_curso>", apes.ape_curso, name="ape_curso"),
    path(
        "competencias/programa/<int:id_competencia>/<int:id_programa>",
        competencias.competencia_programa,
        name="competencia_programa",
    ),
    path(
        "competencias/curso/<int:id_competencia>/<int:id_curso>",
        competencias.competencia_curso,
        name="competencia_curso",
    ),
    path("rubrica_curso/<int:id_rubrica>/<int:id_curso>", rubs.rubrica_curso, name="rubrica_curso"),
    path("evaluar", rubs.evaluar, name="evaluar_estudiante"),
    path("curso/<int:id_curso>", cursos.curso, name="curso"),
    path("secciones", secciones.listar_secciones, name="secciones"),
    path("historico", secciones.listar_secciones_historicas, name="historico_secciones"),
    path("seccion/<int:id_seccion>", secciones.seccion, name="seccion"),
    path("estudiante_seccion/<int:id_estudiante>/<int:id_seccion>", secciones.estudiante_seccion, name="estudiante_seccion"),
]
