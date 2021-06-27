# -*- coding: utf-8 -*-

import rubricas.test_data.data_temas as data_temas
import rubricas.test_data.data_apes as data_apes
import rubricas.test_data.data_competencias as data_competencias
import rubricas.test_data.data_secciones as data_secciones
import rubricas.test_data.data_rubricas as data_rubricas

data_temas.crear_patologias()
data_temas.crear_procedimientos()
data_apes.crear_apes()
data_competencias.crear_competencia()
data_secciones.crear_todo()
data_rubricas.crear_rubricas()
