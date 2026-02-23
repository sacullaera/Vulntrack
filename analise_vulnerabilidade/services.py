import requests
import time
from cadastro_empresa.models import AtivoLogico, AtivoFisico
from .models import Vulnerabilidade

def busca_vulnerabilidades(fabricante, produto, versao):
    query = f"{fabricante} {produto} {versao}"
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {'keywordSearch': query}

    try:
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            vulnerabilidades = []
            
            # Navegando no JSON complexo do NIST
            for item in dados.get('vulnerabilities', []):
                cve = item.get('cve', {})
                vulnerabilidades.append({
                    'id': cve.get('id'),
                    'descricao': cve.get('descriptions', [{}])[0].get('value'),
                    'severidade': cve.get('metrics', {}).get('cvssMetricV31', [{}])[0].get('cvssData', {}).get('baseSeverity', 'N/A')
                })
            return vulnerabilidades
        else:
            print(f"Erro na API: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"Falha na conexão: {e}")
        return []