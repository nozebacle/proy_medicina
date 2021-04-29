# -*- coding: utf-8 -*-

from rubricas.models.temas import Patologia
def crear_patologias():
    print("Creando patologias")
    Patologia.objects.all().delete()


    p1 = Patologia()
    p1.codigo = "A00"
    p1.nombre = "COLERA"
    p1.description = p1.nombre
    p1.save()

    p1_1 = Patologia()
    p1_1.codigo = "A000"
    p1_1.nombre = "BIOTIPO CHOLERAE"
    p1_1.description = "COLERA DEBIDO A VIBRIO CHOLERAE O1, BIOTIPO CHOLERAE"
    p1_1.contenedora = p1
    p1_1.save()

    p1_2 = Patologia()
    p1_2.codigo = "A001"
    p1_2.nombre = "BIOTIPO EL TOR"
    p1_2.description = "COLERA DEBIDO A VIBRIO CHOLERAE O1, BIOTIPO EL TOR"
    p1_2.contenedora = p1
    p1_2.save()

    p1_3 = Patologia()
    p1_3.codigo = "A009"
    p1_3.nombre = "COLERA NO ESPECIFICADO"
    p1_3.description = "COLERA NO ESPECIFICADO"
    p1_3.contenedora = p1
    p1_3.save()

    p2 = Patologia()
    p2.codigo = "A01"
    p2.nombre = "FIEBRES TIFOIDEA Y PARATIFOIDEA"
    p2.description = p2.nombre
    p2.save()


from rubricas.models.temas import SeccionProcedimientos, CapituloProcedimientos, Procedimiento
def crear_procedimientos():
    print("Creando procedimientos")
    Procedimiento.objects.all().delete()
    CapituloProcedimientos.objects.all().delete()
    SeccionProcedimientos.objects.all().delete()

    s1 = SeccionProcedimientos()
    s1.codigo = "00"
    s1.nombre = "PROCEDIMIENTOS QUIRÚRGICOS E INTERVENCIONISTAS"
    s1.save()

    c1 = CapituloProcedimientos()
    c1.codigo = "00"
    c1.nombre = "SISTEMA NERVIOSO"
    c1.seccion = s1
    c1.save()

    p01 = Procedimiento()
    p01.codigo = "01"
    p01.nombre = "PROCEDIMIENTOS EN CRÁNEO, CEREBRO Y MENINGES CEREBRALES"
    p01.seccion = s1
    p01.capitulo = c1
    p01.save()

    p010 = Procedimiento()
    p010.codigo = "01.0"
    p010.nombre = "INCISIÓN DE CRÁNEO (PUNCIONES EN CRÁNEO)"
    p010.contenedora = p01
    p010.seccion = p010.contenedora.seccion
    p010.capitulo = p010.contenedora.capitulo
    p010.save()

    p0101 = Procedimiento()
    p0101.codigo = "01.0.1"
    p0101.nombre = "PUNCIONES EN CISTERNA"
    p0101.contenedora = p010
    p0101.seccion = p0101.contenedora.seccion
    p0101.capitulo = p0101.contenedora.capitulo
    p0101.save()

    p01011 = Procedimiento()
    p01011.codigo = "01.0.1.01"
    p01011.nombre = "PUNCIÓN CISTERNAL, VÍA LATERAL"
    p01011.contenedora = p0101
    p01011.seccion = p01011.contenedora.seccion
    p01011.capitulo = p01011.contenedora.capitulo
    p01011.save()

    p01012 = Procedimiento()
    p01012.codigo = "01.0.1.02"
    p01012.nombre = "PUNCIÓN CISTERNAL, VÍA MEDIAL"
    p01012.contenedora = p0101
    p01012.seccion = p01012.contenedora.seccion
    p01012.capitulo = p01012.contenedora.capitulo
    p01012.save()

    p01013 = Procedimiento()
    p01013.codigo = "01.0.1.03"
    p01013.nombre = "PUNCIÓN CISTERNAL"
    p01013.contenedora = p0101
    p01013.seccion = p01013.contenedora.seccion
    p01013.capitulo = p01013.contenedora.capitulo
    p01013.save()

    p0109 = Procedimiento()
    p0109.codigo = "01.0.9"
    p0109.nombre = "PUNCIÓN CRANEAL"
    p0109.contenedora = p010
    p0109.seccion = p0109.contenedora.seccion
    p0109.capitulo = p0109.contenedora.capitulo
    p0109.save()

    p01091 = Procedimiento()
    p01091.codigo = "01.0.9.01"
    p01091.nombre = "PUNCIÓN SUBDURAL"
    p01091.contenedora = p0109
    p01091.seccion = p01091.contenedora.seccion
    p01091.capitulo = p01091.contenedora.capitulo
    p01091.save()

    p01092 = Procedimiento()
    p01092.codigo = "01.0.9.02"
    p01092.nombre = "OTRA PUNCIÓN CRANEAL "
    p01092.contenedora = p0109
    p01092.seccion = p01092.contenedora.seccion
    p01092.capitulo = p01092.contenedora.capitulo
    p01092.save()