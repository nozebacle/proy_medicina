from django.contrib import admin

# Register your models here.
# Patologías y Procedimientos

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
    list_display = ("codigo", "semestre", "nombre",)
    search_fields = ("codigo", "semestre", "nombre", "nombre_interno")

admin.site.register(Curso, CursoAdmin)


class SeccionAdmin(admin.ModelAdmin):
    list_display = ("curso", "numero")

admin.site.register(Seccion, SeccionAdmin)


# Rubrica
from rubricas.models.rubricas import RubricaPrograma, RubricaCurso, RubricaSeccion, Criterio, NivelCriterio, ItemCalificacionCurso, ItemCalificacionSeccion


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

admin.site.register(ItemCalificacionCurso )
admin.site.register(ItemCalificacionSeccion )
