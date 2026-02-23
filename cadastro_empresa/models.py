from django.db import models
from stdimage.models import StdImageField
from smart_selects.db_fields import ChainedForeignKey

#Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

#Cadastro base
class base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


#Cadastro de empresa
class Empresa(base):
    nome_fantasia = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18)
    segmento = models.CharField('Segmento', max_length=100)
    plano = models.ForeignKey('core.Plano', verbose_name='Plano', on_delete=models.CASCADE)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome_fantasia

# Signal (gatilho) para gerar o slug automaticamente antes de salvar a empresa
def empresa_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome_fantasia) 
signals.pre_save.connect(empresa_pre_save, sender=Empresa)


# Cadastro de funcionário
class Funcionario(base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)
    funcao = models.CharField('Função', max_length=100)
    permissoes = models.ForeignKey('core.Permissao', verbose_name='Permissões', on_delete=models.CASCADE)
    avatar = StdImageField('Avatar', upload_to='avatar_funcionario', variations={'thumb': (100, 100)}, blank=True, null=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
# Signal (gatilho) para gerar o slug automaticamente antes de salvar o funcionário
def funcionario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
signals.pre_save.connect(funcionario_pre_save, sender=Funcionario)


# Cadastro de ativos logicos
class AtivoLogico(base):
    nome = models.CharField('Nome', max_length=100)
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=True, null=True)
    nivel_criticidade = models.ForeignKey('core.NivelCriticidade', verbose_name='Nível de criticidade', default=1, on_delete=models.CASCADE)
    fabricante = models.CharField('Nome do fabricante', max_length=100)
    produto = models.CharField('Produto', max_length=100, default='Não informado')
    versao = models.CharField('Versão', max_length=100)
    numero_serie = models.CharField('Número de série', max_length=100, blank=True, null=True)
    responsavel = ChainedForeignKey(Funcionario, verbose_name='Responsável', chained_field='empresa', chained_model_field='empresa', show_all=False, auto_choose=True, on_delete=models.CASCADE)
    cpe = models.CharField('CPE (Reconmendado)', max_length=100, blank=True, null=True)
    data_aquisicao = models.DateField('Data de aquisição')
    data_encerramento_suporte = models.DateField('Data de encerramento do suporte', blank=True, null=True)
    data_ult_cve = models.DateField('Data da última CVE', blank=True, null=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
# Signal (gatilho) para gerar o slug automaticamente antes de salvar o ativo lógico
def ativo_logico_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
signals.pre_save.connect(ativo_logico_pre_save, sender=AtivoLogico)


# Cadastro de ativos físicos
class AtivoFisico(base):
    nome = models.CharField('Nome', max_length=100)
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=True, null=True)
    nivel_criticidade = models.ForeignKey('core.NivelCriticidade', verbose_name='Nível de criticidade', default=1, on_delete=models.CASCADE)
    fabricante = models.CharField('Nome do fabricante', max_length=100)
    produto = models.CharField('Produto', max_length=100, default='Não informado')
    versao = models.CharField('Versão', max_length=100, blank=True, null=True)
    numero_serie = models.CharField('Número de série', max_length=100, blank=True, null=True)
    responsavel = ChainedForeignKey(Funcionario, verbose_name='Responsável', chained_field='empresa', chained_model_field='empresa', show_all=False, auto_choose=True, on_delete=models.CASCADE)
    data_aquisicao = models.DateField('Data de aquisição')
    data_encerramento_garantia = models.DateField('Data de encerramento do suporte')
    data_ult_manutencao = models.DateField('Data da última manutenção', blank=True, null=True)
    foto_ativo = StdImageField('Foto do ativo', upload_to='foto_ativo', variations={'thumb': (200, 200)}, blank=True, null=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome