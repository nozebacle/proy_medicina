from rubricas.models.competencias import GrupoCompetencia, Competencia


def crear_gruposCompetencias(borrar=True):
    print("Creando Grupos de Competencias")
    if borrar:
        GrupoCompetencia.objects.all().delete()

    gc1 = GrupoCompetencia()
    gc1.sigla = "CPP"
    gc1.nombre_corto = "Conocimientos"
    gc1.nombre_largo = "Conoce, investiga, analiza críticamente y aplica los fundamentos de las ciencias básicas y clínicas a la solución de los problemas de la especialidad."
    gc1.save()

    gc2 = GrupoCompetencia()
    gc2.sigla = "HC"
    gc2.nombre_corto = "Habilidades clínicas"
    gc2.nombre_largo = "Reúne la información necesaria, estudia, diagnostica, desarrolla y aplica planes de prevención, tratamiento y rehabilitación necesarios para el cuidado integral de los pacientes de su especialidad. Analiza críticamente este proceso y su evolución identificando problemas o inconsistencias y puede replantear, corregir y mejorar el cuidado del paciente."
    gc2.save()

    gc3 = GrupoCompetencia()
    gc3.sigla = "ABP"
    gc3.nombre_corto = "Aprendizaje en práctica"
    gc3.nombre_largo = "Reconoce la importancia y las limitaciones de la práctica médica estandarizada y basada en la evidencia científica. Identifica problemas o inconsistencias en su práctica médica, busca y analiza críticamente la literatura para dar solución a los problemas planteados."
    gc3.save()

    gc5 = GrupoCompetencia()
    gc5.sigla = "C"
    gc5.nombre_corto = "Comunicacion"
    gc5.nombre_largo = "Destrezas de comunicación y relaciones interpersonales: Se comunica en forma verbal y escrita de manera oportuna, adecuada y efectiva, individual o en grupo, con todo el personal de salud, con el paciente y la familia. Educa, aconseja y guía al paciente y a la familia en la promoción y mantenimiento de la salud."
    gc5.save()


def crear_competencia(borrar=True):

    if borrar:
        Competencia.objects.all().delete()

    print("Creando competencias")
    crear_gruposCompetencias(borrar)

    descripcion = "Conoce las ciencias  básicas y clínicas necesarias para la especialidad."
    crear_competencia_detalles("CPP", "CPP1", descripcion)

    descripcion = "Conoce la fisiopatología de las enfermedades y situaciones médicas esenciales de la especialidad"
    crear_competencia_detalles("CPP", "CPP2", descripcion)

    descripcion = "Demuestra conocimientos suficientes para diagnosticar y tratar las patologías y situaciones médicas frecuentes "
    crear_competencia_detalles("CPP", "CPP3", descripcion)

    descripcion = "Conoces  las bases fisiológicas, las indicaciones, contraindicaciones e interpreta los resultados de  las pruebas de laboratorio, imágenes y otros métodos diagnósticos asociados a las patologías y situaciones médicas frecuentes"
    crear_competencia_detalles("CPP", "CPP4", descripcion)

    descripcion = (
        "Aproximación analítica e investigativa a la solución de problemas clínicos y la adquisición de conocimiento."
    )
    crear_competencia_detalles("CPP", "CPP5", descripcion)

    descripcion = "Conoce el Sistema General de Seguridad Social de Salud, la Política de Atención Integral en Salud, el Modelo Integral de Atención MIAS y las RIAS "
    crear_competencia_detalles("CPP", "CPP6", descripcion)

    descripcion = "Reúne la información necesaria de manera organizada, identificando y profundizando en datos clínicos relevantes. valora la salud, la dinámica familiar el contexto social."
    crear_competencia_detalles("HC", "HC1", descripcion)

    descripcion = "Realiza un examen organizado, completo y minucioso, identificando los signos clínicos relevante, teniendo en cuenta la situación y necesidades del paciente."
    crear_competencia_detalles("HC", "HC2", descripcion)

    descripcion = "Sintetiza, analiza la información y establece diagnósticos diferenciales y planes de estudio y tratamiento apropiados."
    crear_competencia_detalles("HC", "HC3", descripcion)

    descripcion = "Analiza,  interpreta y usa adecuadamente las pruebas diagnósticas para estudio y seguimiento, evalua riesgo y beneficio. Conoce y aplica los conceptos de probabilidad pre test y las características operativas de las pruebas."
    crear_competencia_detalles("HC", "HC4", descripcion)

    descripcion = "Desarrolla y aplica planes para la prevención, promoción, mantenimiento de la salud, tratamiento y rehabilitación necesarios para el cuidado integral de los pacientes con patologías de su especialidad. Tiene encuenta e incluye el contexto social, la familia y comunidad."
    crear_competencia_detalles("HC", "HC5", descripcion)

    descripcion = "Hace correctamente los procedimientos invasivos o quirúrgicos de la especialidad y da el cuidado pos procedimiento adecuado."
    crear_competencia_detalles("HC", "HC6", descripcion)

    descripcion = "Identifica, maneja, estabiliza pacientes con situaciones médicas de urgencia."
    crear_competencia_detalles("HC", "HC7", descripcion)

    descripcion = "Reconoce sus actividades como las de un especialista en formación, conoce los límites de sus competencias y solicita ayuda cuando es necesario."
    crear_competencia_detalles("HC", "HC8", descripcion)

    descripcion = "Puede manejar los pacientes y situaciones clínicas comunes con mínima supervisión."
    crear_competencia_detalles("HC", "HC9", descripcion)

    descripcion = "Reflexiona y compara su práctica médica con las recomendaciones y referentes nacionales o internacionales; reconoce sus fortalezas, deficiencias y límites para la práctica de la especialidad."
    crear_competencia_detalles("ABP", "ABP1", descripcion)

    descripcion = "Identifica problemas o inconsistencias en su práctica médica, busca y analiza críticamente la literatura para dar solución a los problemas planteados.  "
    crear_competencia_detalles("ABP", "ABP2", descripcion)

    descripcion = "Identifica, integra a la práctica y comunica a los pacientes los conceptos de MBE, incluido riesgo, beneficio y alternativas para los tratamientos."
    crear_competencia_detalles("ABP", "ABP3", descripcion)

    descripcion = "En práctica, identifica diferencias, barreras y puntos de mejoramiento relacionados con el personal de salud,  el sistema de salud, el paciente y su familia. "
    crear_competencia_detalles("ABP", "ABP4", descripcion)

    descripcion = "Participa en el diseño e implementación de planes de mejoramiento para la atención médica."
    crear_competencia_detalles("ABP", "ABP5", descripcion)

    descripcion = "Participa activamente y asume responsabilidades para contribuir en la educación y desarrollo de atriviades académicas de pregrado y postgrado."
    crear_competencia_detalles("ABP", "ABP6", descripcion)

    descripcion = "Se comunica adecuada y oportunamente, con el paciente, la familia."
    crear_competencia_detalles("C", "C1", descripcion)

    descripcion = "Involucra y orienta adecuadamente al paciente y a su familia o cuidadores en las decisiones y planes de cuidado"
    crear_competencia_detalles("C", "C2", descripcion)

    descripcion = "Educa y confirma la comprensión del paciente y su familia sobre la enfermedad, proceso de diagnóstico, tratamiento, rehabilitación, precauciones y prevención"
    crear_competencia_detalles("C", "C3", descripcion)

    descripcion = "Percibe y es conciente de las emociones y de la respuesta humana a las emociones, las entiende y le ayudan a establecer y manejar las relaciones  interpersonales."
    crear_competencia_detalles("C", "C4", descripcion)

    descripcion = "Atiende y cuida de todos los pacientes sin discriminación de ningún tipo."
    crear_competencia_detalles("C", "C5", descripcion)

    descripcion = "Se comunica adecuada y oportunamente con todo el personal involucrado en el cuidado del paciente."
    crear_competencia_detalles("C", "C6", descripcion)

    descripcion = "La historia y los informes escritos son compole¡tos, fieles y adecuados."
    crear_competencia_detalles("C", "C7", descripcion)

    descripcion = (
        "Trabaja efectivamente como  miembro o líder de un grupo de cuidado de la salud u otro grupo profesional. "
    )
    crear_competencia_detalles("C", "C8", descripcion)


def crear_competencia_detalles(sigla_grupo, sigla, descripcion):
    c1 = Competencia()
    c1.sigla = sigla
    c1.nombre = descripcion[: min(120, len(descripcion))]
    c1.descripcion = descripcion
    c1.grupo = GrupoCompetencia.buscar_por_sigla(sigla_grupo)
    c1.save()
