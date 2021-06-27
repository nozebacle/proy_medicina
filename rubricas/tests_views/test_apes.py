# -*- coding: utf-8 -*-
from rubricas.tests_views.ViewTestCase import ViewTestCase
from django.test import Client
from django.urls import reverse
from django.db import connection
from django.test.utils import CaptureQueriesContext

import rubricas.test_data.data_apes as data_apes
import rubricas.test_data.data_secciones as data_secciones
import rubricas.test_data.data_rubricas as data_rubricas

from rubricas.models.apes import APE
from rubricas.models.secciones import Programa
from rubricas.models.secciones import Curso


class Test_View_Programas(ViewTestCase):
    def setUp(self):
        data_apes.crear_apes()
        data_secciones.crear_todo()
        data_rubricas.crear_rubricas()

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_ape_programa_detalle_correcto(self):
        """El llamado a ape_programa muestra la información correcta del ape"""
        c = Client()
        response = self.do_login_profesor(c)

        ape = APE.buscar_por_sigla("APE1")
        id_ape = ape.id
        id_programa = Programa.buscar_por_codigo("PEDI").id

        response = c.get(reverse("ape_programa", args=[id_ape, id_programa]))
        self.assertResponseCode(response, 200, "ape_programa")
        self.assertTemplateUsed(response, "rubricas/apes/detalle_ape.html")
        self.assertWellFormedHTML(response)

        # Revisar que aparezca la información del ape
        self.assertContains(response, ape.sigla)
        self.assertContains(response, ape.nombre_largo)
        self.assertContains(response, ape.descripcion)

        # Revisar que aparezcan los nombres de las rúbricas de programa
        # relacionadas con este APE
        rubricas = ape.buscar_rubricas_ape_programa(id_programa)
        for rub in rubricas:
            self.assertContains(response, rub.nombre)

        # Revisar que aparezcan los nombres de las rúbricas de curso
        # relacionadas con este APE
        rubricas = ape.buscar_rubricas_ape_cursos_programa(id_programa)
        for rub in rubricas:
            self.assertContains(response, rub.nombre)

    def test_ape_programa_con_ape_incorrecto(self):
        """El llamado a ape_programa genera un error cuando el ape no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        id_ape = 9999
        id_programa = Programa.buscar_por_codigo("PEDI").id

        response = c.get(reverse("ape_programa", args=[id_ape, id_programa]))
        self.assertResponseCode(response, 404, "ape_programa: ape inexistente")

    def test_ape_programa_con_programa_incorrecto(self):
        """El llamado a ape_programa genera un error cuando el programa no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        ape = APE.buscar_por_sigla("APE1")
        id_ape = ape.id
        id_programa = 9999

        response = c.get(reverse("ape_programa", args=[id_ape, id_programa]))
        self.assertResponseCode(response, 404, "ape_programa: programa inexistente")

    def test_ape_programa_con_ape_y_programa_incorrecto(self):
        """El llamado a ape_programa genera un error cuando ni el ape ni el programa existen"""
        c = Client()
        response = self.do_login_profesor(c)

        id_ape = 9999
        id_programa = 9999

        response = c.get(reverse("ape_programa", args=[id_ape, id_programa]))
        self.assertResponseCode(response, 404, "ape_programa: ape y programa inexistentes")

    def test_ape_curso_detalle_correcto(self):
        """El llamado a ape_curso muestra la información correcta del ape"""
        c = Client()
        response = self.do_login_profesor(c)

        ape = APE.buscar_por_sigla("APE1")
        id_ape = ape.id
        id_curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20").id

        response = c.get(reverse("ape_curso", args=[id_ape, id_curso]))
        self.assertResponseCode(response, 200, "ape_curso")
        self.assertTemplateUsed(response, "rubricas/apes/detalle_ape.html")
        self.assertWellFormedHTML(response)

        # Revisar que aparezca la información del ape
        self.assertContains(response, ape.sigla)
        self.assertContains(response, ape.nombre_largo)
        self.assertContains(response, ape.descripcion)

        # Revisar que aparezcan los nombres de las rúbricas de curso
        # relacionadas con este APE
        rubricas = ape.buscar_rubricas_ape_curso(id_curso)
        for rub in rubricas:
            self.assertContains(response, rub.nombre)

    def test_ape_curso_con_ape_incorrecto(self):
        """El llamado a ape_curso genera un error cuando el ape no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        id_ape = 9999
        id_curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20").id

        response = c.get(reverse("ape_curso", args=[id_ape, id_curso]))
        self.assertResponseCode(response, 404, "ape_curso: ape inexistente")

    def test_ape_curso_con_curso_incorrecto(self):
        """El llamado a ape_curso genera un error cuando el programa no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        ape = APE.buscar_por_sigla("APE1")
        id_ape = ape.id
        id_curso = 9999

        response = c.get(reverse("ape_curso", args=[id_ape, id_curso]))
        self.assertResponseCode(response, 404, "ape_curso: curso inexistente")

    def test_ape_curso_con_ape_y_curso_incorrecto(self):
        """El llamado a ape_programa genera un error cuando ni el ape ni el curso existen"""
        c = Client()
        response = self.do_login_profesor(c)

        id_ape = 9999
        id_curso = 9999

        response = c.get(reverse("ape_curso", args=[id_ape, id_curso]))
        self.assertResponseCode(response, 404, "ape_curso: ape y curso inexistentes")
