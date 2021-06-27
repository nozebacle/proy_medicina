# -*- coding: utf-8 -*-
from rubricas.tests_views.ViewTestCase import ViewTestCase
from django.test import Client
from django.urls import reverse
from django.db import connection
from django.test.utils import CaptureQueriesContext

import rubricas.test_data.data_secciones as data_secciones

from rubricas.models.secciones import Programa


class Test_View_Programas(ViewTestCase):
    def setUp(self):
        data_secciones.crear_programa()

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_listar_programas(self):
        """El llamado a listar_programas muestra la información correcta"""
        c = Client()
        response = self.do_login_profesor(c)

        response = c.get(reverse("programas"))
        self.assertResponseCode(response, 200, "listar_programas")
        self.assertTemplateUsed(response, "rubricas/programas/lista_programas.html")
        self.assertWellFormedHTML(response)

        pr = Programa.buscar_por_codigo("PEDI")

        # Revisar que aparezca el programa
        self.assertContains(response, pr.codigo)
        self.assertContains(response, pr.nombre)

        # Revisar que aparezcan los códigos de los cursos
        cursos = pr.consultar_cursos_programa()
        for curso in cursos:
            self.assertContains(response, curso.codigo)

        # Revisar que aparezcan las siglas de los APEs del programa
        apes = pr.apes.all()
        for ape in apes:
            self.assertContains(response, ape.sigla)

        # Revisar que aparezcan las siglas de las Comepentencias del programa
        comps = pr.competencias.all()
        for comp in comps:
            self.assertContains(response, comp.sigla)
