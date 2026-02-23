from django.db import models
from cadastro_empresa.models import base


#lista de planos
class Plano(base):
    nome = models.CharField('Nome', max_length=100)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Lista de permissoes
class Permissao(base):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome
    
# lista de nivel de criticidade
class NivelCriticidade(base):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome