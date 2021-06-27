# -*- coding: utf-8 -*-

from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext

from rubricas.models.rubricas import Rubrica
from rubricas.models.rubricas import ItemCalificacion

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_ItemCalificacion(TestCase):
    r1_id = 0
    ic1_id = 0

    def setUp(self):
        nombre = "LaRubrica_1"
        interno = "Interno_1"
        descripcion = "desc_1"
        comentarios = "comms_1"

        r1 = Rubrica.objects.create(
            nombre=nombre,
            nombre_interno=interno,
            descripcion=descripcion,
            comentarios=comentarios,
            debe_tener_procedimientos=False,
            debe_tener_patologias=False,
        )
        self.r1_id = r1.id

        ic1 = ItemCalificacion.objects.create(nombre="item1", peso=25, rubrica=r1)
        self.ic1_id = ic1.id

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra el nombre del ítem de calificación, el peso y el nombre de la rúbrica"
        ic1 = ItemCalificacion.objects.get(id=self.ic1_id)
        self.assertTrue("item1" in str(ic1))
        self.assertTrue("25" in str(ic1))
        self.assertTrue("LaRubrica_1" in str(ic1))
