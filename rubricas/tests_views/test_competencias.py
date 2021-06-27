# -*- coding: utf-8 -*-
from rubricas.tests_views.ViewTestCase import ViewTestCase
from django.test import Client
from django.urls import reverse
from django.db import connection
from django.test.utils import CaptureQueriesContext

import rubricas.test_data.data_competencias as data_competencias
import rubricas.test_data.data_secciones as data_secciones
import rubricas.test_data.data_rubricas as data_rubricas

from rubricas.models.competencias import Competencia
from rubricas.models.secciones import Programa
from rubricas.models.secciones import Curso


class Test_View_Programas(ViewTestCase):
    def setUp(self):
        data_competencias.crear_competencia()
        data_secciones.crear_todo()
        data_rubricas.crear_rubricas()

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_competencia_programa_detalle_correcto(self):
        """El llamado a competencia_programa muestra la información correcta de la competencia"""
        c = Client()
        response = self.do_login_profesor(c)

        comp = Competencia.buscar_por_sigla("HC1")
        id_comp = comp.id
        id_programa = Programa.buscar_por_codigo("PEDI").id

        response = c.get(reverse("competencia_programa", args=[id_comp, id_programa]))
        self.assertResponseCode(response, 200, "competencia_programa")
        self.assertTemplateUsed(response, "rubricas/competencias/detalle_competencia.html")
        self.assertWellFormedHTML(response)

        # Revisar que aparezca la información de la competencia
        self.assertContains(response, comp.sigla)
        self.assertContains(response, comp.nombre)
        self.assertContains(response, comp.descripcion)

        # Revisar que aparezca la información del grupo al que peternece la competencia
        self.assertContains(response, comp.grupo.sigla)
        self.assertContains(response, comp.grupo.nombre_corto)

        # Revisar que aparezcan los nombres de las rúbricas de programa
        # relacionadas con esta competencia
        rubricas = comp.buscar_rubricas_competencia_programa(id_programa)
        for rub in rubricas:
            self.assertContains(response, rub.nombre)

        # Revisar que aparezcan los nombres de las rúbricas de curso
        # relacionadas con esta competencia
        rubricas = comp.buscar_rubricas_competencia_cursos_programa(id_programa)
        for rub in rubricas:
            self.assertContains(response, rub.nombre)

    def test_competencia_programa_con_competencia_incorrecto(self):
        """El llamado a competencia_programa genera un error cuando la competencia no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        id_comp = 9999
        id_programa = Programa.buscar_por_codigo("PEDI").id

        response = c.get(reverse("competencia_programa", args=[id_comp, id_programa]))
        self.assertResponseCode(response, 404, "competencia_programa: competencia inexistente")

    def test_competencia_programa_con_programa_incorrecto(self):
        """El llamado a competencia_programa genera un error cuando el programa no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        comp = Competencia.buscar_por_sigla("HC1")
        id_comp = comp.id
        id_programa = 9999

        response = c.get(reverse("competencia_programa", args=[id_comp, id_programa]))
        self.assertResponseCode(response, 404, "competencia_programa: programa inexistente")

    def test_competencia_programa_con_competencia_y_programa_incorrecto(self):
        """El llamado a competencia_programa genera un error cuando ni la competencia ni el programa existen"""
        c = Client()
        response = self.do_login_profesor(c)

        id_comp = 9999
        id_programa = 9999

        response = c.get(reverse("competencia_programa", args=[id_comp, id_programa]))
        self.assertResponseCode(response, 404, "competencia_programa: competencia y programa inexistentes")

    def test_competencia_curso_detalle_correcto(self):
        """El llamado a competencia_curso muestra la información correcta de la competencia"""
        c = Client()
        response = self.do_login_profesor(c)

        comp = Competencia.buscar_por_sigla("HC1")
        id_comp = comp.id
        id_curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20").id

        response = c.get(reverse("competencia_curso", args=[id_comp, id_curso]))
        self.assertResponseCode(response, 200, "competencia_curso")
        self.assertTemplateUsed(response, "rubricas/competencias/detalle_competencia.html")
        self.assertWellFormedHTML(response)

        # Revisar que aparezca la información de la competencia
        self.assertContains(response, comp.sigla)
        self.assertContains(response, comp.nombre)
        self.assertContains(response, comp.descripcion)

        # Revisar que aparezca la información del grupo al que peternece la competencia
        self.assertContains(response, comp.grupo.sigla)
        self.assertContains(response, comp.grupo.nombre_corto)

        # Revisar que aparezcan los nombres de las rúbricas de curso
        # relacionadas con esta competencia
        rubricas = comp.buscar_rubricas_competencia_curso(id_curso)
        for rub in rubricas:
            self.assertContains(response, rub.nombre)

    def test_competencia_curso_con_competencia_incorrecto(self):
        """El llamado a competencia_curso genera un error cuando la competencia no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        id_comp = 9999
        id_curso = Curso.buscar_por_codigo_semestre("PEDI-5101", "2020-20").id

        response = c.get(reverse("competencia_curso", args=[id_comp, id_curso]))
        self.assertResponseCode(response, 404, "competencia_curso: competencia inexistente")

    def test_competencia_curso_con_programa_incorrecto(self):
        """El llamado a competencia_curso genera un error cuando el programa no existe"""
        c = Client()
        response = self.do_login_profesor(c)

        comp = Competencia.buscar_por_sigla("HC1")
        id_comp = comp.id
        id_curso = 9999

        response = c.get(reverse("competencia_curso", args=[id_comp, id_curso]))
        self.assertResponseCode(response, 404, "competencia_curso: programa inexistente")

    def test_competencia_curso_con_competencia_y_programa_incorrecto(self):
        """El llamado a competencia_curso genera un error cuando ni la competencia ni el programa existen"""
        c = Client()
        response = self.do_login_profesor(c)

        id_comp = 9999
        id_curso = 9999

        response = c.get(reverse("competencia_curso", args=[id_comp, id_curso]))
        self.assertResponseCode(response, 404, "competencia_curso: competencia y programa inexistentes")
