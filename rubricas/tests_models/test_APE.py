# -*- coding: utf-8 -*-

# from django.test import TestCase
from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext


from rubricas.models.apes import APE
from rubricas.models.secciones import Programa

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_APE(TestCase):
    def setUp(self):
        largo = "nombre largo"
        corto = "nombre corto"
        sigla = "APX1"
        APE.objects.create(sigla=sigla, nombre_corto=corto, nombre_largo=largo, descripcion=largo)

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra la sigla y el nombre corto del ape"
        ape1 = APE.objects.get(sigla="APX1")
        self.assertTrue("APX1" in str(ape1))
        self.assertTrue("nombre corto" in str(ape1))

    def test_buscar_por_sigla(self):
        """Si se busca un APE por sigla, se encuentra"""
        ape1 = APE.objects.get(sigla="APX1")
        ape2 = APE.buscar_por_sigla("APX1")
        self.assertIsNotNone(ape1, "El APE encontrado con GET no debería ser None")
        self.assertIsNotNone(ape1, "El APE encontrado con buscar_por_sigla no debería ser None")
        self.assertEqual(ape1.sigla, ape2.sigla, "Las siglas no son las mismas")
        self.assertEqual(ape1.id, ape2.id, "Los objetos no tienen los mismos ids")

    def test_buscar_por_sigla_inexistente(self):
        """Si se busca un APE usando una sigla que no existe, retorna None"""
        ape = APE.buscar_por_sigla("AAA")
        self.assertIsNone(ape, "El APE retornado debería ser None")

    def test_buscar_por_programa(self):
        """buscar_por_programa encuentra los apes correctos"""
        ap2 = APE.objects.create(sigla="AP2", nombre_corto="nc2", nombre_largo="nl2", descripcion="d2")
        ap3 = APE.objects.create(sigla="AP3", nombre_corto="nc3", nombre_largo="nl3", descripcion="d3")
        ap4 = APE.objects.create(sigla="AP4", nombre_corto="nc4", nombre_largo="nl4", descripcion="d4")

        pr = Programa.objects.create(nombre="Pediatria", codigo="PEDI")
        pr.agregar_ape(ap2)
        pr.agregar_ape(ap3)

        apes = APE.buscar_por_programa(pr)
        self.assertIn(ap2, apes)
        self.assertIn(ap3, apes)
        self.assertNotIn(ap4, apes)
