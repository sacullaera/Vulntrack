from django.contrib import admin
from .models import NivelCriticidade, Plano, Permissao

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome',)

@admin.register(Permissao)
class PermissaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome',)

@admin.register(NivelCriticidade)
class NivelCriticidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome',)