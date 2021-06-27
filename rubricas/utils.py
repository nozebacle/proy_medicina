import datetime
import rubricas.locale_bogota as local

from django.shortcuts import render

from rubricas.models.usuarios import Usuario, Estudiante, Profesor, Monitor, Externo, Coordinador
from rubricas.constantes import PROFESOR, ESTUDIANTE, MONITOR, ADMINISTRADOR, COORDINADOR, EXTERNO, SEMESTRE_ACTUAL


def render_page(request, template_name, context):
    usuario = reconstruir_usuario(request)
    # pendientes = Notificacion.buscar_notificaciones_pendientes_usuario(usuario.id)

    context["id_usuario"] = usuario.id
    context["menu"] = seleccionar_menu(usuario.tipo)
    if usuario.tipo == PROFESOR:
        profesor = reconstruir_profesor(request)
        context["secciones"] = profesor.buscar_secciones_profesor(SEMESTRE_ACTUAL)

    return render(request, template_name, context)


def seleccionar_menu(tipo_usuario: str) -> str:
    """
    Esta función selecciona el menú que se le debe mostrar a un usuario,
    según su tipo (PROFESOR, ESTUDIANTE, MONITOR, ADMINISTRADOR)
    Parámetros:
        tipo_usuario: El tipo del usuario que requiere un menú
    Retorno:
        (str): El nombre de la plantilla con el menú para el usuario
    """
    menu = "none"
    if tipo_usuario == PROFESOR:
        menu = "navbar_profesor"
    elif tipo_usuario == ESTUDIANTE:
        menu = "navbar_estudiante"
    elif tipo_usuario == MONITOR:
        menu = "navbar_monitor"
    elif tipo_usuario == ADMINISTRADOR:
        menu = "navbar_admin"
    elif tipo_usuario == EXTERNO:
        menu = "navbar_externo"
    elif tipo_usuario == COORDINADOR:
        menu = "navbar_coordinador"

    return "rubricas/menus/" + menu + ".html"


def reconstruir_usuario(request):
    if "usuario" not in request.session:
        return None

    login = request.session["usuario"]
    result = Usuario.objects.filter(login__exact=login)
    if result:
        usuario = result.first()
        return usuario
    return None


def reconstruir_estudiante(request):
    if "usuario" not in request.session:
        return None

    login = request.session["usuario"]
    result = Estudiante.objects.filter(login__exact=login)
    if result:
        usuario = result.first()
        return usuario
    return None


def reconstruir_profesor(request):
    if "usuario" not in request.session:
        return None

    login = request.session["usuario"]

    result = Profesor.objects.filter(login__exact=login)
    if result:
        usuario = result.first()
        return usuario
    return None


def reconstruir_monitor(request):
    if "usuario" not in request.session:
        return None

    login = request.session["usuario"]
    result = Monitor.objects.filter(login__exact=login)
    if result:
        usuario = result.first()
        return usuario
    return None



def hora_servidor():
    now = datetime.datetime.now()
    hora_servidor = local.bogota.localize(now)
    return hora_servidor


def buscar_ip(request):
    from ipware import get_client_ip

    try:
        client_ip, _ = get_client_ip(request)
        if client_ip is not None:
            return client_ip
        else:
            return None
    except:
        print("No conseguí la ip ...")
        return "--"
