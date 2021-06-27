# -*- coding: utf-8 -*-

from rubricas.models.apes import APE


def crear_apes(borrar=True):
    print("Creando apes")
    if borrar:
        APE.objects.all().delete()

    ape = APE()
    ape.sigla = "APE1"
    ape.nombre_corto = "Historia clínica"
    ape.nombre_largo = "Hace una historia clínica completa y detallada del paciente pediátrico, tiene en cuenta el crecimiento, desarrollo y comportamiento del paciente de acuerdo con los grupos de edad."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE2"
    ape.nombre_corto = "Valoración clínica"
    ape.nombre_largo = "Valora adecuadamente el crecimiento y desarrollo (físico, motriz, cognitivo, nutricional y socioemocional), la salud oral, visual, mental, sexual y reproductiva), la dinámica familiar, el contexto social y las redes de apoyo."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE3"
    ape.nombre_corto = "Diagnósticos"
    ape.nombre_largo = "Identifica y prioriza los diagnósticos diferenciales, conoce y usa adecuadamente las pruebas diagnósticas indicadas."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE4"
    ape.nombre_corto = "Manejo integral"
    ape.nombre_largo = "Establece un Plan de manejo integral y seguimiento, trabaja en equipo, hace el tratamiento de las enfermedades y problemas clínicos frecuentes en ámbito ambulatorio, urgencias, hospitalización."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE5"
    ape.nombre_corto = "Dinámicas familiares"
    ape.nombre_largo = "Identifica y trabaja para mejorar factores de riesgo o alteraciones de la dinámica y estructura familiar o social, que repercutan en el estado de salud."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE6"
    ape.nombre_corto = "Comunicación"
    ape.nombre_largo = "Se comunica adecuadamente y educa sobre las recomendaciones para la promoción y mantenimiento de la salud del paciente, familia y comunidad."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE7"
    ape.nombre_corto = "Procedimientos pedriatría"
    ape.nombre_largo = "Puede hacer los procedimientos básicos de un pediatra general."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE8"
    ape.nombre_corto = "Documentación"
    ape.nombre_largo = "Documenta de manera adecuada, eficiente y razonada la atención del paciente en la historia clínica. Demuestra capacidad de síntesis y razonamiento clínico, se comunica y elabora informes para garantizar la calidad, seguridad, continuidad de la atención."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE9"
    ape.nombre_corto = "Práctica clínica"
    ape.nombre_largo = "Realiza una práctica clínica crítica y reflexiva, identificando problemas o inconsistencias que soluciona con base en la evidencia científica."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE10"
    ape.nombre_corto = "Trabajo en equipo"
    ape.nombre_largo = "Trabaja en equipo y realiza una práctica interdisciplinaria, coordina con los involucrados para garantizar la calidad, seguridad, continuidad en la atención en la institución y en el sistema de salud. Realiza interconsultas, referencia y contrareferencia. "
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE11"
    ape.nombre_corto = "Tratamiento enfermedades y problemas"
    ape.nombre_largo = "Identifica, puede Iniciar el estudio y tratamiento de las enfermedades y problemas clínicos complejos frecuentes, conoce sus limitaciones, sabe remitirlos."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE12"
    ape.nombre_corto = "Urgencias"
    ape.nombre_largo = "Identifica los pacientes que requieren atención de urgencia y hace el manejo adecuado."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE13"
    ape.nombre_corto = "Neonatos"
    ape.nombre_largo = "Puede recibir, evaluar, estabilizar y dar los cuidados iniciales a un recién nacido, incluida la educación a la madre."
    ape.descripcion = ape.nombre_largo
    ape.save()

    ape = APE()
    ape.sigla = "APE14"
    ape.nombre_corto = "Reanimación"
    ape.nombre_largo = "Puede dar soporte vital avanzado y realizar reanimación de pacientes pediátricos."
    ape.descripcion = ape.nombre_largo
    ape.save()
