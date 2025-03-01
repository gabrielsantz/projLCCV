from django.contrib import admin
from .models import Colaboradores, Financiador, AreasTecnologicas, Projetos




@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('id_colaborador', 'nome', 'cpf', 'dt_nascimento')
    search_fields = ('nome', 'cpf')
    list_filter = ('dt_nascimento',)

@admin.register(Financiador)
class FinanciadorAdmin(admin.ModelAdmin):
    list_display = ('id_financiador', 'financiador')
    search_fields = ('financiador',)

@admin.register(AreasTecnologicas)
class AreasTecnologicasAdmin(admin.ModelAdmin):
    list_display = ('id_area_tecnologica', 'area_tecnologica')
    search_fields = ('area_tecnologica',)

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('id_projeto', 'projeto', 'id_financiador', 'id_area_tecnologica', 'coordenador', 'ativo', 'inicio_vigencia', 'fim_vigencia', 'valor')
    search_fields = ('projeto', 'coordenador')
    list_filter = ('id_financiador', 'id_area_tecnologica', 'inicio_vigencia')
    filter_horizontal = ('equipe',)