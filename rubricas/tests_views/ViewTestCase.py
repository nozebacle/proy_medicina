# -*- coding: utf-8 -*-

from django.test import TestCase
from django.urls import reverse

import rubricas.constantes as constantes
from rubricas.models.usuarios import Profesor

class ViewTestCase(TestCase):

    def crear_profesor(self, login, password):
        profe = Profesor()
        profe.login = login
        profe.nombre = login
        profe.alias = login
        profe.tipo = constantes.PROFESOR
        profe.usuario_local = True
        profe.save()
        profe.cambiar_password(password)


    def do_login_profesor(self, client):
        if Profesor.objects.filter(login='profe').count() == 0:
            self.crear_profesor('profe', 'profe')

        response = client.post(reverse("login"), {"usuario": "profe", "password": "profe"})
        self.assertRedirects(response, reverse("home"))
        return response

    def do_other_login(self, client, login, password):
        response = client.post(reverse("login"), {"usuario": login, "password": password})
        self.assertRedirects(response, reverse("home"))
        return response

    def assertResponseCode(self, response, expected_code, operation):
        self.assertEqual(
            response.status_code, expected_code, f"The operation {operation} should generate the code {expected_code}"
        )

    def assertWellFormedHTML(self, response):
        ...
