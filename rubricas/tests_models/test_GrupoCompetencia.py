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
class Test_GrupoCompetencia(TestCase):
    def setUp(self):
        GrupoCompetencia.objects.create(nombre_corto="gc nc", nombre_largo="gc nl", sigla="gc", descripcion="desc")

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra la sigla y el nombre del grupo de comeptencias"
        grupo = GrupoCompetencia.objects.get(sigla="gc")
        self.assertTrue("gc" in str(grupo))
        self.assertTrue("gc nc" in str(grupo))

    def test_buscar_por_sigla(self):
        """Si se busca un grupo de competencias por sigla, se encuentra"""
        gc1 = GrupoCompetencia.objects.get(sigla="gc")
        gc2 = GrupoCompetencia.buscar_por_sigla("gc")
        self.assertIsNotNone(gc1, "El grupo encontrado con GET no debería ser None")
        self.assertIsNotNone(gc2, "El grupo encontrado con buscar_por_sigla no debería ser None")
        self.assertEqual(gc1.sigla, gc2.sigla, "Las siglas no son las mismas")
        self.assertEqual(gc1.id, gc2.id, "Los objetos no tienen los mismos ids")

    def test_buscar_por_sigla_inexistente(self):
        """Si se busca un grupo de competencias usando una sigla que no existe, retorna None"""
        cc = GrupoCompetencia.buscar_por_sigla("XX")
        self.assertIsNone(cc, "El grupo retornado debería ser None")

    def test_buscar_por_programa(self):
        """buscar_por_programa encuentra los grupos de competencias correctos"""
        grupo1 = GrupoCompetencia.objects.get(sigla="gc")
        cp1 = Competencia.objects.create(grupo=grupo1, nombre="n1", sigla="cp1", descripcion="d1")
        cp2 = Competencia.objects.create(grupo=grupo1, nombre="n2", sigla="cp2", descripcion="d2")
        cp3 = Competencia.objects.create(grupo=grupo1, nombre="n3", sigla="cp3", descripcion="d3")

        grupo2 = GrupoCompetencia.objects.get(sigla="gc")
        cp4 = Competencia.objects.create(grupo=grupo2, nombre="n4", sigla="cp4", descripcion="d4")

        pr1 = Programa.objects.create(nombre="Programa1", codigo="PRO1")
        pr1.agregar_competencia(cp1)
        pr1.agregar_competencia(cp2)

        grupos_1 = Competencia.buscar_por_programa(pr1)
        self.assertIsNotNone(grupos_1)
        self.assertIn(grupo1, grupos_1)
        self.assertNotIn(grupo2, grupos_1)

        pr2 = Programa.objects.create(nombre="Programa2", codigo="PRO2")
        pr2.agregar_competencia(cp4)

        grupos_2 = Competencia.buscar_por_programa(pr1)
        self.assertIsNotNone(grupos_2)
        self.assertNotIn(grupo1, grupos_2)
        self.assertIn(grupo2, grupos_2)

        pr3 = Programa.objects.create(nombre="Programa3", codigo="PRO3")
        pr3.agregar_competencia(cp1)
        pr3.agregar_competencia(cp4)

        grupos_3 = Competencia.buscar_por_programa(pr1)
        self.assertIsNotNone(grupos_3)
        self.assertIn(grupo1, grupos_3)
        self.assertIn(grupo2, grupos_3)

    def test_buscar_por_programa_sin_competencias(self):
        """buscar_por_programa retorna una lista vacía si el programa no tiene competencias"""
        pr = Programa.objects.create(nombre="Pediatria", codigo="PEDI")
        grupos = GrupoCompetencia.buscar_por_programa(pr)
        self.assertIsNotNone(grupos)
        self.assertEquals(0, len(grupos))
