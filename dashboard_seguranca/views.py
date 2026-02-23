from django.shortcuts import render
from cadastro_empresa.models import AtivoLogico, AtivoFisico
from analise_vulnerabilidade.models import Vulnerabilidade
from django.db.models import Count

def dashboard_geral(request):
    # Indicadores Rápidos
    total_logicos = AtivoLogico.objects.count()
    total_fisicos = AtivoFisico.objects.count()
    total_vulnerabilidades = Vulnerabilidade.objects.count()
    
    # Vulnerabilidades por Severidade (para um gráfico de pizza, por exemplo)
    severidade_counts = Vulnerabilidade.objects.values('severidade').annotate(total=Count('severidade'))

    # Ativos com mais problemas (Top 5)
    # Aqui usamos o related_name que definimos no model
    ativos_em_risco_logicos = AtivoLogico.objects.annotate(num_vunes=Count('vulnerabilidade')).order_by('-num_vunes')[:5]
    ativos_em_risco_fisicos = AtivoFisico.objects.annotate(num_vunes=Count('vulnerabilidade')).order_by('-num_vunes')[:5]

    context = {
        'total_logicos': total_logicos,
        'total_fisicos': total_fisicos,
        'total_vulnerabilidades': total_vulnerabilidades,
        'severidade_counts': severidade_counts,
        'ativos_em_risco_logicos': ativos_em_risco_logicos,
        'ativos_em_risco_fisicos': ativos_em_risco_fisicos,
    }
    
    return render(request, 'geral.html', context)

