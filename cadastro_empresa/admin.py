from django.contrib import admin
from .models import Empresa, Funcionario, AtivoFisico, AtivoLogico


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'cnpj', 'segmento', 'plano', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome_fantasia', 'cnpj')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'funcao', 'permissoes', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome', 'email')

@admin.register(AtivoLogico)
class AtivoLogicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'nivel_criticidade', 'responsavel', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome',)

@admin.register(AtivoFisico)
class AtivoFisicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'nivel_criticidade', 'responsavel', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome',)   