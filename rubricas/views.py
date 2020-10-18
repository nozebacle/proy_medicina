from django.shortcuts import render, redirect, reverse, HttpResponse
import datetime
#import dashboard.utils as utils
#from dashboard.models.usuarios import Usuario, Registro
from rubricas.forms import AuthForm


def login(request, mensaje=None):
    forma = AuthForm(request.POST or None)
    if forma.is_valid():
        # request.session.flush()
        usuario = forma.cleaned_data["usuario"]
        password_forma = forma.cleaned_data["password"]

        if usuario.endswith("@uniandes.edu.co"):
            usuario = usuario.split("@uniandes.edu.co")[0]

        try:
            obj_usuario = Usuario.objects.get(login=usuario)
            resultado = obj_usuario.verificar_password(password_forma)
            if resultado:
                request.session["usuario"] = usuario
                request.session["tipo_usuario"] = obj_usuario.tipo
                request.session["id_usuario"] = obj_usuario.id
                obj_usuario.ultimo_acceso = datetime.datetime.now()
                obj_usuario.save()

                ip_cliente = utils.buscar_ip(request)
                reg = Registro()
                reg.usuario = obj_usuario
                reg.ip = ip_cliente
                reg.save()

                return redirect(reverse("home"))
            else:
                mensaje = "Password incorrecto."
        except Usuario.DoesNotExist:
            print("No encontré el usuario")
            mensaje = "Nombre de usuario incorrecto."

    template_name = "dashboard/login.html"
    context = {"mensaje": mensaje}
    return render(request, template_name, context)


def logout(request):
    try:
        request.session["usuario"] = "none"
        request.session["tipo_usuario"] = "none"
        request.session["id_usuario"] = "none"

        del request.session["usuario"]
        del request.session["tipo_usuario"]
        del request.session["id_usuario"]
        request.session.flush()
    except KeyError:
        print("Problemas haciendo logout")
        pass

    return redirect("login")
