# -*- coding: utf-8 -*-

from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext

from rubricas.models.rubricas import Rubrica
from rubricas.models.rubricas import Criterio

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_Criterio(TestCase):
    cr1_id = 0

    def setUp(self):
        nombre = "LaRubrica_1"
        interno = "Interno_1"
        descripcion = "desc_1"
        comentarios = "comms_1"
        r1 = Rubrica.objects.create(
            nombre=nombre, nombre_interno=interno, descripcion=descripcion, comentarios=comentarios
        )

        cr1 = Criterio.objects.create(nombre_interno="interno", descripcion="desc", rubrica=r1, numero=1)
        self.cr1_id = cr1.id

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra el nombre interno del criterio y el de la rúbrica"
        c = Criterio.objects.get(id=self.cr1_id)
        self.assertTrue("interno" in str(c))
        self.assertTrue("LaRubrica_1" in str(c))
