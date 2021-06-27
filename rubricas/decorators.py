# -*- coding: utf-8 -*-
import functools

from rubricas.constantes import PROFESOR
from rubricas.views.autenticacion import login

# def acceso_autenticado(func):
#    """
#       Asegurarse que una función sólo puede ser usada por un
#       usuario autenticado
#    """
#    @functools.wraps(func)
#    def wrapper_exclusivo_usuario(request):
#        tipo_actual = request.session.get('tipo_usuario')
#        # revisar que la sesión no se haya vencido por tiempo
#
#        if tipo_actual is None:
#            mensaje = "Usted no tiene permisos para la operación seleccionada."
#            return login(request, mensaje)
#        return func(request)
#    return wrapper_exclusivo_usuario


def acceso_autenticado():
    """
    Asegurarse que una función sólo puede ser usada por un
    usuario autenticado
    """

    def decorador_autenticado(func):
        @functools.wraps(func)
        def wrapper_exclusivo_usuario(*args, **kwargs):
            request = args[0]
            if "tipo_usuario" in request.session:
                tipo_actual = request.session.get("tipo_usuario")
            else:
                tipo_actual = None
            # revisar que la sesión no se haya vencido por tiempo

            if tipo_actual is None:
                mensaje = "Usted no tiene permisos para la operación seleccionada."
                return login(request, mensaje)
            return func(*args, **kwargs)

        return wrapper_exclusivo_usuario

    return decorador_autenticado


def acceso_restringido(tipo_usuario=PROFESOR, login_url="/"):
    """
    Asegurarse que una función sólo puede ser usada por un
    cierto tipo de usuario.
    """

    def decorador_exclusivo(func):
        @functools.wraps(func)
        def wrapper_exclusivo_usuario(request, *args, **kwargs):
            tipo_actual = request.session.get("tipo_usuario")
            # revisar que la sesión no se haya vencido por tiempo

            # Si hay solo un tipo de usuario, convertirlo en una lista
            if not isinstance(tipo_usuario, list):
                tu = [tipo_usuario]
            else:
                tu = tipo_usuario

            if tipo_actual is None or tipo_actual not in tu:
                mensaje = "Usted no tiene permisos para la operación seleccionada."
                return login(request, mensaje)
            return func(request, *args, **kwargs)

        return wrapper_exclusivo_usuario

    return decorador_exclusivo
