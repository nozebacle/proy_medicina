# -*- coding: utf-8 -*-
import sys
from django.contrib.auth.hashers import PBKDF2PasswordHasher

import rubricas.constantes as constantes
from django.db import models


class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    nombre = models.CharField(max_length=120)
    alias = models.CharField(max_length=120, blank=True)
    tipo = models.CharField(max_length=2, choices=constantes.TIPO_USUARIO, default=constantes.ESTUDIANTE)
    ultimo_acceso = models.DateTimeField(auto_now_add=True)
    usuario_local = models.BooleanField(default=False)
    id_brightspace = models.IntegerField(default=0, blank=True, null=False)

    def __str__(self):
        return f"{self.tipo}: {self.login}"

    @property
    def descripcion_tipo_usuario(self):
        descripcion = "Tipo inesperado ... "
        for abr, desc in constantes.TIPO_USUARIO:
            if abr == self.tipo:
                descripcion = desc
        return descripcion

    def cambiar_password(self, nuevo_password):
        hasher = PBKDF2PasswordHasher()
        self.password = hasher.encode(nuevo_password, self.nombre)
        self.save()

    def verificar_password(self, password_forma):
        if self.usuario_local:
            return self.verificar_password_local(password_forma)
        else:
            return self.verificar_password_ldap(password_forma)

    def verificar_password_ldap(self, password):
        import ldap as auth

        login = self.login + "@uniandes.edu.co"
        resultado = False
        try:
            con = auth.initialize("ldap://adua.uniandes.edu.co:389", bytes_mode=False)
            con.simple_bind_s(login, password)
            resultado = True
        except:
            print("Error!", sys.exc_info()[0])
        return resultado

    def verificar_password_local(self, password_forma):
        verificador = PBKDF2PasswordHasher()
        resultado = verificador.verify(password_forma, self.password)
        return resultado

    def usuario_existe(login):
        existe = len(Usuario.objects.filter(login=login)) > 0
        return existe

    @property
    def es_estudiante(self):
        return self.tipo == constantes.ESTUDIANTE

    @property
    def a_estudiante(self):
        if self.es_estudiante:
            return Estudiante.objects.filter(login__exact=self.login).first()
        else:
            return None


class Estudiante(Usuario):
    secciones = models.ManyToManyField("rubricas.Seccion", blank=True)
    preguntas_sin_respuesta = models.BooleanField(default=False)
    solo_nombre = models.CharField(max_length=120)
    solo_apellido = models.CharField(max_length=120)
    codigo = models.CharField(max_length=120, null=True, blank =True)

    def iniciales(self):
        return (self.solo_nombre[0] + self.solo_apellido[0]).upper()


class Profesor(Usuario):
    secciones = models.ManyToManyField("rubricas.Seccion", blank=True)

    def buscar_secciones_profesor(self, semestre=None):
        if semestre is None:
            secciones = self.secciones.all().order_by("-semestre")
        else:
            secciones = self.secciones.filter(semestre=semestre).order_by("numero")
        return secciones

    def buscar_secciones_historicas(self):
        secciones = self.secciones.all().order_by("-semestre")
        return secciones

class Monitor(Usuario):
    secciones = models.ManyToManyField("rubricas.Seccion", blank=True)


class Coordinador(Usuario):
    comentario = models.TextField(null=False, blank=True)


class Administrador(Usuario):
    comentario = models.TextField(null=False, blank=True)


class Externo(Usuario):
    secciones = models.ManyToManyField("rubricas.Seccion", blank=True)
    email = models.CharField(max_length=150, unique=False, null=False, blank=True)
    comentario = models.TextField(null=False, blank=True)


class Registro(models.Model):
    usuario = models.ForeignKey("rubricas.Usuario", null=True, on_delete=models.SET_NULL)
    ip = models.CharField(max_length=15, default="0.0.0.0", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
