# -*- coding: utf-8 -*-

from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext

from rubricas.models.secciones import Programa
from rubricas.models.competencias import GrupoCompetencia
from rubricas.models.competencias import Competencia

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_Competencia(TestCase):
    def setUp(self):
        nombre = "nombre"
        sigla = "cp"
        descripcion = "descripcion"
        gr = self.crearGrupoCompetencia()
        Competencia.objects.create(grupo=gr, nombre=nombre, sigla=sigla, descripcion=descripcion)

    def crearGrupoCompetencia(self, nombre="gc"):
        return GrupoCompetencia.objects.create(nombre_corto=nombre, nombre_largo="nl", sigla=nombre, descripcion="desc")

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra la sigla y el nombre de la competencia"
        competencia = Competencia.objects.get(sigla="cp")
        self.assertTrue("cp" in str(competencia))
        self.assertTrue("nombre" in str(competencia))

    def test_buscar_por_sigla(self):
        """Si se busca una competencia por sigla, se encuentra"""
        cp1 = Competencia.objects.get(sigla="cp")
        cp2 = Competencia.buscar_por_sigla("cp")
        self.assertIsNotNone(cp1, "La competencia encontrada con GET no debería ser None")
        self.assertIsNotNone(cp2, "La competencia encontrada con buscar_por_sigla no debería ser None")
        self.assertEqual(cp1.sigla, cp1.sigla, "Las siglas no son las mismas")
        self.assertEqual(cp2.id, cp2.id, "Los objetos no tienen los mismos ids")

    def test_buscar_por_sigla_inexistente(self):
        """Si se busca un APE usando una sigla que no existe, retorna None"""
        cc = Competencia.buscar_por_sigla("CC")
        self.assertIsNone(cc, "La competencia retornada debería ser None")

    def test_buscar_por_programa(self):
        """buscar_por_programa encuentra las competencias correctas"""
        gr = self.crearGrupoCompetencia("gg")
        cp1 = Competencia.objects.create(grupo=gr, nombre="n1", sigla="cp1", descripcion="d1")
        cp2 = Competencia.objects.create(grupo=gr, nombre="n2", sigla="cp2", descripcion="d2")
        cp3 = Competencia.objects.create(grupo=gr, nombre="n3", sigla="cp3", descripcion="d3")

        pr = Programa.objects.create(nombre="Pediatria", codigo="PEDI")
        pr.agregar_competencia(cp1)
        pr.agregar_competencia(cp2)

        competencias = Competencia.buscar_por_programa(pr)
        self.assertIsNotNone(competencias)
        self.assertIn(cp1, competencias)
        self.assertIn(cp2, competencias)
        self.assertNotIn(cp3, competencias)

    def test_buscar_por_programa_sin_competencias(self):
        """buscar_por_programa retorna una lista vacía si el programa no tiene competencias"""
        pr = Programa.objects.create(nombre="Pediatria", codigo="PEDI")
        competencias = Competencia.buscar_por_programa(pr)
        self.assertIsNotNone(competencias)
        self.assertEquals(0, len(competencias))
