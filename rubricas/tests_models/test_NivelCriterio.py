# -*- coding: utf-8 -*-

from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext

from rubricas.models.rubricas import Rubrica
from rubricas.models.rubricas import Criterio
from rubricas.models.rubricas import NivelCriterio

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_NivelCriterio(TestCase):
    ncr1_id = 0

    def setUp(self):
        nombre = "LaRubrica_1"
        interno = "Interno_1"
        descripcion = "desc_1"
        comentarios = "comms_1"
        r1 = Rubrica.objects.create(
            nombre=nombre, nombre_interno=interno, descripcion=descripcion, comentarios=comentarios
        )

        cr1 = Criterio.objects.create(nombre_interno="interno", descripcion="desc", rubrica=r1, numero=1)

        ncr1 = NivelCriterio.objects.create(nombre="nivel", criterio=cr1, descripcion="desc", puntos=5, numero=20)

        self.ncr1_id = ncr1.id

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra el nombre interno del criterio y el de la rúbrica"
        nc = NivelCriterio.objects.get(id=self.ncr1_id)
        self.assertTrue("interno" in str(nc))
        self.assertTrue("nivel" in str(nc))
        self.assertTrue("20" in str(nc))
