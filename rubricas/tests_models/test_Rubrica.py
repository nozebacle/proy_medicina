# -*- coding: utf-8 -*-

from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext

from rubricas.models.rubricas import Rubrica

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_Rubrica(TestCase):
    r1_id = 0

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

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra el nombre de la rubrica"
        r = Rubrica.objects.get(id=self.r1_id)
        self.assertTrue("LaRubrica_1" in str(r))
