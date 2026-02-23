from django.urls import path
from .views import detalhe_ativo, sincronizar_cves

#app_name = 'analise_vulnerabilidade'

urlpatterns = [
    path('detalhe/<str:tipo_ativo>/<int:ativo_id>/', detalhe_ativo, name='detalhe_ativo'),
    path('sincronizar/<str:tipo_ativo>/<int:ativo_id>/', sincronizar_cves, name='sincronizar_cves'),
]
