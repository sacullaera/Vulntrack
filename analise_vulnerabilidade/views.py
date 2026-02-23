from django.shortcuts import get_object_or_404, render, redirect
from cadastro_empresa.models import AtivoLogico, AtivoFisico
from .services import busca_vulnerabilidades
from .models import Vulnerabilidade

def detalhe_ativo(request, tipo_ativo, ativo_id):
    if tipo_ativo == 'logico':
        ativo = get_object_or_404(AtivoLogico, id=ativo_id)
        vulnerabilidades = Vulnerabilidade.objects.filter(ativo_logico=ativo)
    elif tipo_ativo == 'fisico':
        ativo = get_object_or_404(AtivoFisico, id=ativo_id)
        vulnerabilidades = Vulnerabilidade.objects.filter(ativo_fisico=ativo)
    else:
        return redirect('home')  # Redireciona para a página inicial se o tipo de ativo for inválido
    
    
    return render(request, 'detalhe_ativo.html', {
        'ativo': ativo,
        'tipo': tipo_ativo,
        'vulnerabilidades': vulnerabilidades
    })

def sincronizar_cves(request, tipo_ativo, ativo_id):
    # 1. Busca o ativo correto
    print(f"--- ROTA ACESSADA: Tipo: {tipo_ativo} | ID: {ativo_id} ---")
    if tipo_ativo == 'logico':
        ativo = get_object_or_404(AtivoLogico, id=ativo_id)
    else:
        ativo = get_object_or_404(AtivoFisico, id=ativo_id)
    
    print(f"Ativo encontrado: {ativo.nome}. Chamando API...")
    # 2. Busca os dados na API externa
    lista_cves = busca_vulnerabilidades(ativo.fabricante, ativo.produto, ativo.versao)

    print(f"API retornou {len(lista_cves)} resultados.")
    # 3. CHAMA A FUNÇÃO DE PROCESSAMENTO (O que você queria!)
    
    if len(lista_cves) > 0:
        print("Chamando a função processar_analise agora...")
        processar_analise(ativo, tipo_ativo, lista_cves)
    else:
        print("Aviso: lista_cves veio vazia. Verifique Fabricante/Produto/Versão.")

    # 4. Redireciona de volta para o detalhe
    return redirect('detalhe_ativo', tipo_ativo=tipo_ativo, ativo_id=ativo_id)


def processar_analise(ativo, tipo_ativo, lista_cves):
    print(f"--- Processando {len(lista_cves)} CVEs para o ativo {ativo.nome} ---")
    for item in lista_cves:
        if tipo_ativo == 'logico':
            # Vincula ao campo 'ativo_logico'
            Vulnerabilidade.objects.get_or_create(
                cve_id=item['id'],
                ativo_logico=ativo,  # O objeto AtivoLogico inteiro aqui
                defaults={
                    'descricao': item['descricao'],
                    'severidade': item['severidade']
                }
            )
        else:
            # Vincula ao campo 'ativo_fisico'
            Vulnerabilidade.objects.get_or_create(
                cve_id=item['id'],
                ativo_fisico=ativo,  # O objeto AtivoFisico inteiro aqui
                defaults={
                    'descricao': item['descricao'],
                    'severidade': item['severidade']
                }
            )