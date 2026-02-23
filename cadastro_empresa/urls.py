from django.urls import path
from .views import cadastro_ativo_fisico, cadastro_ativo_logico, cadastro_empresa, cadastro_funcionario 

urlpatterns = [
    path('empresa/', cadastro_empresa, name='cadastro_empresa'),
    path('funcionario/', cadastro_funcionario, name='cadastro_funcionario'),
    path('ativo-logico/', cadastro_ativo_logico, name='cadastro_ativo_logico'),
    path('ativo-fisico/', cadastro_ativo_fisico, name='cadastro_ativo_fisico'),
]