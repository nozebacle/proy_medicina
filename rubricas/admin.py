from django.contrib import admin


from rubricas.models.usuarios import Usuario, Estudiante, Profesor, Monitor, Coordinador, Administrador, Externo


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("login", "nombre", "alias", "tipo", "usuario_local")
    search_fields = ("login", "nombre", "alias")

    def save_model(self, request, obj, form, change):
        if not obj.password.startswith("pbkdf2_sha256$"):
            obj.cambiar_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Estudiante, UsuarioAdmin)
admin.site.register(Profesor, UsuarioAdmin)
admin.site.register(Monitor, UsuarioAdmin)
admin.site.register(Externo, UsuarioAdmin)
admin.site.register(Coordinador, UsuarioAdmin)
admin.site.register(Administrador, UsuarioAdmin)


from rubricas.models.usuarios import Registro


class RegistroAdmin(admin.ModelAdmin):
    list_display = ("usuario", "timestamp")


admin.site.register(Registro, RegistroAdmin)

from rubricas.models.temas import Patologia


class PatologiaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre", "descripcion")


admin.site.register(Patologia, PatologiaAdmin)

from rubricas.models.temas import SeccionProcedimientos


class SeccionProcedimientosAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")


admin.site.register(SeccionProcedimientos, SeccionProcedimientosAdmin)

from rubricas.models.temas import CapituloProcedimientos


class CapituloProcedimientosAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")


admin.site.register(CapituloProcedimientos, CapituloProcedimientosAdmin)


from rubricas.models.temas import Procedimiento


class ProcedimientoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre", "descripcion")


admin.site.register(Procedimiento, ProcedimientoAdmin)


# APES y Competencias

from rubricas.models.apes import APE


class APEAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nombre_corto")
    search_fields = ("sigla", "nombre_corto", "nombre_largo", "descripcion")


admin.site.register(APE, APEAdmin)


from rubricas.models.competencias import GrupoCompetencia, Competencia


class GrupoCompetenciaAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nombre_corto")
    search_fields = ("sigla", "nombre_corto", "nombre_largo", "descripcion")


admin.site.register(GrupoCompetencia, GrupoCompetenciaAdmin)


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nombre")
    search_fields = ("sigla", "nombre", "descripcion")


admin.site.register(Competencia, CompetenciaAdmin)


# Programas, Cursos y Secciones
from rubricas.models.secciones import Programa, Curso, Seccion


class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


admin.site.register(Programa, ProgramaAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "nombre_interno"
    )
    search_fields = ("codigo", "semestre", "nombre", "nombre_interno")


admin.site.register(Curso, CursoAdmin)


class SeccionAdmin(admin.ModelAdmin):
    list_display = ("curso", "semestre", "numero")


admin.site.register(Seccion, SeccionAdmin)


# Rubrica
from rubricas.models.rubricas import (
    RubricaPrograma,
    RubricaCurso,
    RubricaSeccion,
    Criterio,
    NivelCriterio,
    ItemCalificacionCurso,
    ItemCalificacionSeccion,
)


admin.site.register(RubricaPrograma)
admin.site.register(RubricaCurso)
admin.site.register(RubricaSeccion)


class CriterioAdmin(admin.ModelAdmin):
    list_display = ("nombre_interno", "numero")
    search_fields = ("nombre_interno", "descripcion")


admin.site.register(Criterio, CriterioAdmin)


class NivelCriterioAdmin(admin.ModelAdmin):
    list_display = ("numero", "nombre", "criterio")
    search_fields = ("nombre", "descripcion")


admin.site.register(NivelCriterio, NivelCriterioAdmin)
admin.site.register(ItemCalificacionCurso)
admin.site.register(ItemCalificacionSeccion)


# Resultados
from rubricas.models.resultados import ResultadoRubrica, ResultadoCriterio


class ResultadoRubricaAdmin(admin.ModelAdmin):
    list_display = ("item", "estudiante", "puntos")
    search_fields = ("estudiante", "item")


admin.site.register(ResultadoRubrica, ResultadoRubricaAdmin)


class ResultadoCriterioAdmin(admin.ModelAdmin):
    list_display = ("item", "criterio", "estudiante", "puntos")
    search_fields = ("estudiante", "item", "criterio")


admin.site.register(ResultadoCriterio, ResultadoCriterioAdmin)


# Estadísticas
from rubricas.models.estadisticas import (
    ResumenEstudianteSeccion,
    ResumenAPEEvaluacion,
    ResumenAPESemestre,
    ResumenCompetenciaEvaluacion,
    ResumenCompetenciaSemestre,
)

admin.site.register(ResumenEstudianteSeccion)
admin.site.register(ResumenAPEEvaluacion)
admin.site.register(ResumenAPESemestre)
admin.site.register(ResumenCompetenciaEvaluacion)
admin.site.register(ResumenCompetenciaSemestre)
