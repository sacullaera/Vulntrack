**VULNTRACK - Plataforma de gerenciamento de vulnerabilidades**

Vulntrack é uma plataforma desenvolvida para empresas de pequeno/médio porte, com o cadastro dos ativos, ela automaticamente busca as *Common Vulnerabilities and Exposures* (CVEs) publicadas pelo *National Institute of Standards ant Technology* (NIST) via API oficial, caso haja alguma vulnerabilidade comunicada, a plataforma armazena e alerta o cliente para que ela seja tratada o mais breve possível.

Pré-requisitos:

| Nome                 | Versão |
| -------------------- | ------ |
| Python               | 3.14.0 |
| Django               | 6.0.2  |
| SQLite               | 3.46.1 |
| Django-bootstap5     | 26.1   |
| Django-STDimage      | 6.0.2  |
| Django-smart-selects | 1.7.2  |
| Django-q2            | 1.9.0  |
**ARQUITETURA**



**API (NIST)**
A plataforma utiliza a API oficial do NIST.
pelo endpoint: "https://services.nvd.nist.gov/rest/json/cves/2.0"

Ela envia pera o endpoint um JSON com três campos
"Fabricante", "produto", "versão"
(eles são fornecidos pelo cliente quando se cadastra um ativo)

a API retorna três campos:
"id", "description", "metrics"

estes campos são salvos na s variáveis:
is, descrição, severidade

essas variáveis estão dentro de um laço lastreado pelo identificador do ativo, com essas informações o processo chegar a tabela "vulnerabilidade" no banco de dados, se o id da CVE e o id do ativo já existirem na mesma linha, o processo não faz nada, caso contrário a CVE é adicionada ao bando de dados.


**Dicionário de dados:**

*obs.: as tabelas não possuem o campo 'id', pois o próprio Django cria ao gerar uma tabela.*

Tabela "base"
Usada por outras tabelas por possuir campos comuns a todas as outras tabelas de cadastro.

| campo      | tipo     | descrisão                                                                        |
| ---------- | -------- | -------------------------------------------------------------------------------- |
| criado     | data     | ao adicionar uma nova entrada na tabela, esse campo se preenche automaticamente. |
| modificado | data     | Ao modificar uma entrada na tabela, esse campo é preenchido aotomaticamente.     |
| ativo      | booleano | Se verdadeiro, a entrada é vista pelo sistema.                                   |



Tabela "empresa"
Usada para armazenar os dados das empresas que fazem o gerenciamento de vulnerabilidades.

| campo         | tipo       | descrição                                                               |
| ------------- | ---------- | ----------------------------------------------------------------------- |
| nome_fantasia | varchar    | Nome fantasia da empresa                                                |
| cnpj          | varchar    | Cadastro nacional de pessoa juridica                                    |
| segmento      | varchar    | Área de atuação da empresa                                              |
| plano         | foreingkey | seleciona um dos planos fornecidos pela Vulntrack                       |
| slug          | sting      | nome da empresa em lowercase e sem espaços para ser usado em endpoints. |

Tabela "funcionário"
Usada para cadastro dos funcionários responsáveis pelos ativos nas empresas cadastradas.

| campo      | tipo       | descrição                                                                   |
| ---------- | ---------- | --------------------------------------------------------------------------- |
| nome       | varchar    | nome do funcionário.                                                        |
| email      | email      | email para identificação e contato com o responsável.                       |
| empresa    | foreingkey | seleciona a empresa que o funcionário pertence.                             |
| funcao     | varchar    | Função que o funcionário ocupa na empresa.                                  |
| permissoes | foreingkey | seleciona as permissões que o funcionário pode executar na plataforma.      |
| avatar     | image      | foto do funcionario da empresa.                                             |
| slug       | string     | nome do funcionário em lowercase e sem espaços para ser usado em endpoints. |

Tabela "ativoLogico"
Armazena os ativos lógicos das empresas cadastradas.

| campo                     | tipo       | descrição                                                                                    |
| ------------------------- | ---------- | -------------------------------------------------------------------------------------------- |
| nome                      | varchar    | nome do ativo lógico                                                                         |
| empresa                   | foreingKey | seleciona a empresa cadastrada ao qual o ativo pertence.                                     |
| descricao                 | varchar    | uma breve descrição informando qual  utilidade do ativo na empresa                           |
| nivel_criticidade         | foreingKey | seleciona o nível crítico da função do ativo na empresa.                                     |
| fabricante                | varchar    | quem fabricou o ativo.                                                                       |
| versao                    | varchar    | a versão em que se encontra o ativo                                                          |
| numero_serie              | varchar    | número de identificação do ativo pela fabricante.                                            |
| responsavel               | foreingKey | Seleciona o funcionário responsável pelo ativo                                               |
| cpe                       | varchar    | _Customer Premises Equipment_ (CPE) número de identificação para o equipamento em específico |
| data_aquisicao            | data       | Data que o ativo foi adquirido pela empresa.                                                 |
| data_encerramento_suporte | data       | data de encerramento do suporte, caso o ativo seja código proprietário.                      |
| data_ult_cve              | data       | data da ultima CVE registrada.                                                               |
| slug                      | sting      | nome do ativo em lowercase e sem espaços para ser usado em endpoints.                        |


Tabela "ativoFisico"

| campo                      | tipo       | descrição                                                             |
| -------------------------- | ---------- | --------------------------------------------------------------------- |
| nome                       | varchar    | nome do ativo físico                                                  |
| empresa                    | foreingKey | seleciona a empresa cadastrada ao qual o ativo pertence.              |
| descricao                  | varchar    | uma breve descrição informando qual  utilidade do ativo na empresa    |
| nivel_criticidade          | foreingKey | seleciona o nível crítico da função do ativo na empresa.              |
| fabricante                 | varchar    | quem fabricou o ativo.                                                |
| versao                     | varchar    | a versão em que se encontra o ativo                                   |
| numero_serie               | varchar    | número de identificação do ativo pela fabricante.                     |
| responsavel                | foreingKey | Seleciona o funcionário responsável pelo ativo                        |
| data_aquisicao             | data       | Data que o ativo foi adquirido pela empresa.                          |
| data_encerramento_garantia | data       | data de encerramento da garantia do ativo.                            |
| data_ult_manutencao        | data       | data em que o ativo teve sua ultima manutenção                        |
| foto_ativo                 | image      | foto do ativo de empresa.                                             |
| slug                       | sting      | nome do ativo em lowercase e sem espaços para ser usado em endpoints. |
