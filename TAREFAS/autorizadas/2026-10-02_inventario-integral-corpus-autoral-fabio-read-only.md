# TAREFA AUTORIZADA — INVENTÁRIO INTEGRAL DO CORPUS AUTORAL DE FABIO TAKWARA

STATUS: AUTORIZADA
AUTORIZADO_POR: Fabio Takwara
DATA: 2026-10-02
EXECUTOR: Hermes
MODE: READ_ONLY
MUTATION: PROHIBITED

## Contexto
Esta tarefa amplia a recuperação genealógica anterior. O objetivo não é localizar apenas três artigos de 2021, mas produzir um mapa integral do corpus autoral relevante à Pré-Constituição da Regência v2 e à missão editorial de produzir artigos autorais rastreáveis para as gavetas/estados da arte.

## Objetivo
Inventariar, sem alterar nenhum arquivo, toda publicação ou rascunho autoral de Fabio Takwara localizável nos repositórios e arquivos locais acessíveis, incluindo:
- artigos Medium e respectivas cópias/espelhos;
- publicações Zenodo e artefatos com DOI;
- Cadernos 1–7, Anexo 1 e Anais;
- cartilhas, manuais, memoriais, ensaios e artigos metodológicos;
- artigos já publicados, candidatos, prontos para depósito e rascunhos;
- artigos associados às gavetas/estados da arte;
- material com declaração de uso/assistência de inteligência artificial;
- artigo de Habitação de Interesse Social informado por Fabio como revisado e pronto para Zenodo;
- documentos autorais históricos relevantes encontrados em repositórios legados.

## Âncoras remotas já confirmadas
Repo: takwaratec/acervo-soberania-tecnologica
- docs/analyses/bambu-estrutural/00-inventario-corpus-autoral.md
- docs/analyses/tecnologia-takwara/index.md
- docs/como-navegar-no-acervo.md
- docs/analyses/fundamentos/index.md
- publicacoes-zenodo/
- docs/frentes-documentais/
- docs/analyses/*/estado-da-arte.md

O inventário público confirma Cadernos 1–7 + Anexo 1 + Anais e distingue Cartilhas autorais de fichas científicas/estados da arte. O índice Tecnologia Takwara registra, entre outros, Bioeconomia Comunitária do Bambu e Fitorremediação e Mercados de Carbono.

## Escopo local
Inspecionar os repositórios já conhecidos da recuperação anterior e, quando necessário, outros diretórios Git sob /Users/fabiotakwara/Documents/GitHub/ que contenham material autoral. Incluir TakwaraTec-Acervo-Web, acervo-soberania-tecnologica, Takwara-Tech/Resck quando disponível localmente, Mulheres-Tecem-Amazonia e demais repositórios em que buscas por autoria/título/DOI indiquem material relevante.

## Registro por item
Para cada obra/versão material:
- AUTHORIAL_WORK_ID provisório;
- título;
- data/ano;
- tipo documental;
- tema/gaveta relacionada;
- estado: HISTORICO | RASCUNHO | EM_REVISAO | REVISADO | PRONTO_PARA_DEPOSITO | PUBLICADO;
- caminho absoluto/local e repo/ref quando aplicável;
- URL pública/original quando houver;
- DOI e versão do DOI quando houver;
- idioma e relação com traduções;
- relação ORIGINAL | COPIA_VERSIONADA | DERIVADO | TRADUCAO | ESPELHO | DEPOSITO;
- declaração de IA: PRESENTE | AUSENTE | NAO_VERIFICADA, com locator;
- relação com estado-da-arte/gaveta;
- fonte/evidência citada ou camada documental que o sustenta;
- divergências de metadados/DOI/título/versão;
- SHA256 local quando houver arquivo material;
- observações de privacidade/custódia.

## Produtos
1. Relatório integral legível em Markdown.
2. Manifesto tabular CSV ou TSV com uma linha por obra/versão material.
3. Matriz GAVETA/ESTADO_DA_ARTE -> ARTIGO_AUTORAL, classificando:
   EXISTENTE_PUBLICADO | EXISTENTE_PRONTO | EXISTENTE_RASCUNHO | AUSENTE | NAO_DETERMINADO.
4. Lista específica de obras PRONTAS_PARA_DEPOSITO, sem publicar nada.
5. Lista de divergências e duplicatas sem escolher canonicidade.
6. Receipt curto.

## Regras epistemológicas
- Não contar cópia/tradução/espelho como nova obra autoral.
- Não inferir DOI, publicação, revisão ou prontidão.
- DOI depositado != homologação documental.
- Artigo autoral != ficha científica != estado da arte.
- Declaração de IA deve ser constatada no texto/metadado; ausência de busca não prova ausência.
- Não promover rascunho a publicado.
- Não publicar nem reservar DOI.
- Não mover, renomear, editar, deduplicar ou limpar.
- Não expor conteúdo privado no receipt; usar locators.

## Questões obrigatórias
A. Quantas OBRAS AUTORAIS ÚNICAS foram encontradas?
B. Quantas possuem DOI?
C. Quantas estão publicadas?
D. Quantas estão prontas para depósito mas não publicadas?
E. Quantas estão em revisão/rascunho?
F. Quantos artigos Medium únicos existem e quais têm cópia versionada?
G. Quais gavetas/estados da arte já têm artigo autoral correspondente?
H. Quais ainda não têm?
I. Onde está e qual é o estado documental do artigo de Habitação de Interesse Social informado como revisado/pronto para Zenodo?
J. Quais obras têm declaração explícita de assistência/uso de IA?
K. Quais divergências impedem uma genealogia canônica segura?

## Saída
RESULT=PASS | PARTIAL | STOP
UNIQUE_AUTHORIAL_WORKS=<n>
WITH_DOI=<n>
PUBLISHED=<n>
READY_FOR_DEPOSIT=<n>
DRAFT_OR_REVIEW=<n>
MEDIUM_UNIQUE=<n>
GAVETAS_WITH_AUTHORIAL_ARTICLE=<n>
GAVETAS_WITHOUT_AUTHORIAL_ARTICLE=<n>
HIS_ARTICLE_STATUS=<state>
REPORT_PATH=<absolute path>
MANIFEST_PATH=<absolute path>
MATRIX_PATH=<absolute path>
STOPS=<...>
NEXT=RETURN_RECEIPT_TO_MAESTRO_FOR_PRE_CONSTITUTION_GENEALOGY_RECONCILIATION
