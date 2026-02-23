from django import forms
from .models import AtivoLogico, Empresa, Funcionario, AtivoFisico

class EmpresaModelForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_fantasia', 'cnpj', 'segmento', 'plano']


class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'empresa', 'funcao', 'permissoes', 'avatar']

class AtivoLogicoModelForm(forms.ModelForm):
    class Meta:
        model = AtivoLogico
        fields = ['nome', 'empresa', 'descricao', 'nivel_criticidade', 'fabricante', 'produto', 'versao', 'cpe', 'numero_serie', 'responsavel', 'data_aquisicao', 'data_encerramento_suporte']

class AtivoFisicoModelForm(forms.ModelForm):
    class Meta:
        model = AtivoFisico
        fields = ['nome', 'empresa', 'descricao', 'nivel_criticidade', 'fabricante', 'produto', 'versao', 'numero_serie', 'responsavel', 'data_aquisicao', 'data_encerramento_garantia', 'data_ult_manutencao', 'foto_ativo']