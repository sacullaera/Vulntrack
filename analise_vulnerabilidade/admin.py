from django.contrib import admin

from analise_vulnerabilidade.models import Vulnerabilidade

@admin.register(Vulnerabilidade)
class VulnerabilidadeAdmin(admin.ModelAdmin):
    # REMOVA 'ativo' da lista abaixo e adicione os novos campos
    list_display = ('cve_id', 'get_ativo', 'severidade', 'data_identificacao')
    list_filter = ('severidade',)
    search_fields = ('cve_id', 'descricao')

    # Criamos um método para mostrar qual ativo está vinculado, já que agora são dois campos
    def get_ativo(self, obj):
        if obj.ativo_logico:
            return f"Lógico: {obj.ativo_logico.nome}"
        if obj.ativo_fisico:
            return f"Físico: {obj.ativo_fisico.nome}"
        return "Nenhum ativo"
    
    get_ativo.short_description = 'Ativo Vinculado' # Nome da coluna no Admin