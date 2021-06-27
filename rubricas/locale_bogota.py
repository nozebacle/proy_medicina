# -*- coding: utf-8 -*-

import pytz
import locale

try:
    locale.setlocale(locale.LC_TIME, "es_ES")
    print("Usando: es_ES")
except:
    print("No encontré el locale: es_ES")

try:
    locale.setlocale(locale.LC_TIME, "es_ES.utf8")
    print("Usando: es_ES.utf8")
except:
    print("No encontré el locale2: es_ES.utf8")

bogota = pytz.timezone("America/Bogota")
local_timezone = bogota
