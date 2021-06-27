# -*- coding: utf-8 -*-

from unittest import TestCase
import pprint

from django.db import connection
from django.test.utils import CaptureQueriesContext

from rubricas.models.rubricas import Rubrica
from rubricas.models.rubricas import ItemCalificacion
from rubricas.models.rubricas import ItemCalificacionSeccion
from rubricas.models.secciones import Programa, Curso, Seccion

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class Test_ItemCalificacionCurso(TestCase):
    r1_id = 0
    ic1_id = 0
    curso_id = 0
    seccion_id = 0

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

        pr = Programa.objects.create(nombre="PROGRAMA", codigo="PRO1")
        curso = Curso.objects.create(
            nombre="nombre_curso",
            nombre_interno="interno_curso",
            codigo="codigo_curso",
            semestre="200010",
            programa=pr,
            descripcion="desc_curso",
        )
        curso_id = curso.id

        seccion = Seccion.objects.create(curso=curso, numero=14)
        seccion_id = curso.id

        ic1 = ItemCalificacionSeccion.objects.create(nombre="item1", peso=25, rubrica=r1, seccion=seccion)
        self.ic1_id = ic1.id

    def tearDown(self):
        print("Number of queries: ", len(connection.queries))
        # pprint.pprint(connection.queries)

    def test_str(self):
        "El método str muestra el nombre del ítem de calificación, el peso, el nombre de la rúbrica y el número de la seccion"
        ic1 = ItemCalificacionSeccion.objects.get(id=self.ic1_id)
        self.assertTrue("item1" in str(ic1))
        self.assertTrue("25" in str(ic1))
        self.assertTrue("LaRubrica_1" in str(ic1))
        self.assertTrue("14" in str(ic1))
