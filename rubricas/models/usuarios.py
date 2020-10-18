import os
import random
import sys
from django.conf import settings
from django.db import models
from django.db.models import Count
from django.contrib.auth.hashers import PBKDF2PasswordHasher

class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=2, choices=TIPO_USUARIO, default=ESTUDIANTE)
    ultimo_acceso = models.DateTimeField(auto_now_add=True)
    usuario_local = models.BooleanField(default=False)
    id_brightspace = models.IntegerField(default=0, blank=True, null=False)

    def __str__(self):
        return self.login + " (" + self.tipo + ")"

    @property
    def descripcion_tipo_usuario(self):
        descripcion = "Tipo inesperado ... "
        for abr, desc in TIPO_USUARIO:
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
        return self.tipo == ESTUDIANTE

    @property
    def a_estudiante(self):
        if self.es_estudiante:
            return Estudiante.objects.filter(login__exact=self.login).first()
        else:
            return None

    def buscar_usuarios(terminos_busqueda):
        terminos = terminos_busqueda.lower().split(" ")
        usuarios_con_login = set()
        for termino in terminos:
            usuarios = Usuario.objects.filter(login__icontains=termino)
            usuarios_con_login = usuarios_con_login.union(set(usuarios))

        usuarios_con_nombre = None
        for termino in terminos:
            usuarios = Usuario.objects.filter(nombre__icontains=termino)
            if usuarios_con_nombre is None:
                usuarios_con_nombre = set(usuarios)
            else:
                usuarios_con_nombre = usuarios_con_nombre.intersection(set(usuarios))

        lista_completa = usuarios_con_login.union(usuarios_con_nombre)
        for u in lista_completa:
            if u.es_estudiante:
                print(u.login, u.nombre, u.a_estudiante.seccion)
            else:
                print(u.login, u.nombre, u.usuario_local)
        return list(lista_completa)


