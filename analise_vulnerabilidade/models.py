from django.db import models
from cadastro_empresa.models import AtivoLogico, AtivoFisico


class Vulnerabilidade(models.Model):
    ativo_logico = models.ForeignKey(AtivoLogico, on_delete=models.CASCADE, null=True, blank=True)
    ativo_fisico = models.ForeignKey(AtivoFisico, on_delete=models.CASCADE, null=True, blank=True)
    
    cve_id = models.CharField(max_length=255)
    descricao = models.TextField()
    severidade = models.CharField(max_length=50)
    data_identificacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.cve_id} - {self.severidade}"
    
