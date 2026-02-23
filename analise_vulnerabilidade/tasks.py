from cadastro_empresa.models import AtivoLogico, AtivoFisico
from .views import busca_vulnerabilidades, processar_analise
import time

def tarefa_sincronizacao_global():
    """Esta função será chamada automaticamente pelo agendador."""
    
    # Sincroniza Ativos Lógicos
    for ativo in AtivoLogico.objects.all():
        lista = busca_vulnerabilidades(ativo.fabricante, ativo.produto, ativo.versao)
        processar_analise(ativo, 'logico', lista)
        time.sleep(5) # Delay para evitar bloqueio na API do NIST

    # Sincroniza Ativos Físicos
    for ativo in AtivoFisico.objects.all():
        lista = busca_vulnerabilidades(ativo.fabricante, ativo.produto, ativo.versao)
        processar_analise(ativo, 'fisico', lista)
        time.sleep(5) # Delay para evitar bloqueio na API do NIST