from django.test import TestCase

# Create your tests here.

from rubricas.unit_tests.temas import crear_patologias, crear_procedimientos
crear_patologias()
crear_procedimientos()

from rubricas.unit_tests.apes import crear_apes
crear_apes()

from rubricas.unit_tests.competencias import crear_competencia
crear_competencia()

from rubricas.unit_tests.secciones import crear_programa, crear_cursos, crear_secciones
crear_programa()
crear_cursos()
crear_secciones()


from rubricas.unit_tests.rubricas import crear_rubricas
crear_rubricas()
