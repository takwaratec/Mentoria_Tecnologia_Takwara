# Inventário Administrativo dos Ativos GitHub — 2026

> Conta principal: `takwaratec`
> Primeira auditoria: 22/07/2026
> Estado: inventário inicial; será aprofundado repositório por repositório.

## 1. Regra de autoridade

- `acervo-soberania-tecnologica` é a única referência científica do ecossistema.
- Os demais repositórios públicos documentam projetos, formação, divulgação, interfaces ou legado.
- Um repositório público de projeto não valida cientificamente as tecnologias que menciona.
- Fontes científicas devem apontar para a publicação primária ou para uma versão depositada e estável.
- Somente `Mulheres-Tecem-Amazonia` (MQTF) será privado nesta rodada.

## 2. Ativos da conta TakwaraTec

| Repositório | Classe administrativa | Visibilidade em 22/07 | Destino |
|---|---|---:|---|
| `acervo-soberania-tecnologica` | Referência científica | Público | Manter público; concluir curadoria e publicação |
| `Mentoria_Tecnologia_Takwara` | Coordenação e método | Público | Manter público; fonte das regras administrativas |
| `Mentoria_Comunidades_RaioX` | Coordenação e método | Público | Manter público; auditar conteúdo e fronteira |
| `ECOSALA` | Projeto | Público | Manter público após saneamento |
| `fundo-vaga-lumen-2026` | Projeto | Público | Manter público após saneamento |
| `fabrica-modelo` | Projeto | Público | Manter público após saneamento |
| `eco-prancha` | Projeto | Público | Manter público após saneamento |
| `plataforma-juventude-solidaria-2026` | Projeto | Público | Manter público após saneamento |
| `unb-desafios-amazonia-2026` | Projeto | Público | Manter público após saneamento |
| `ludmila-athis-df` | Projeto | Público | Manter público após saneamento |
| `Personagens-Bambu` | Divulgação e formação | Público | Manter público; auditar alegações |
| `takwara-mentoria-vercel` | Interface | Público | Manter público; auditar publicação e dados |
| `projetos` | Legado/agregação | Público | Definir função; depois manter ou arquivar |
| `docmd-test-takwara` | Teste | Público | Definir necessidade; depois arquivar ou restringir publicação |
| `Mulheres-Tecem-Amazonia` | Projeto futuro MQTF | **Privado desde 22/07/2026** | Manter privado; preparação para 2027 |

## 3. Salvaguarda do MQTF

### Cópias identificadas

| Cópia | Estado | Função definida |
|---|---|---|
| `/Users/fabiotakwara/Documents/GitHub/Mulheres-Tecem-Amazonia_Clone` | Limpa, `main` em `b5ee92da`, alinhada ao último estado remoto conhecido | Cópia canônica do histórico Git |
| `/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia` | `main` em `602b6dc4`, 732 alterações rastreadas e 339 não rastreadas | Fonte do trabalho local ainda não integrado |

### Pacote de preservação

Local: `/Users/fabiotakwara/Documents/GitHub/_salvaguardas_mqtf/2026-07-22/`

| Arquivo | Conteúdo | SHA-256 |
|---|---|---|
| `mqtf-historico-remoto.bundle` | Histórico completo alinhado ao remoto, incluindo `main` e `gh-pages` | `cf94dd65bb55ff8fff64a6ddd7d05dc8b2374e055f1dd2dab4dc84674074d5a9` |
| `mqtf-historico-base-local.bundle` | Histórico completo da base usada pela pasta UnB | `2884a5bdd3af83b9b3127ef034bfd273b8733f211d0b6a7cd9284dd34736cfb3` |
| `mqtf-alteracoes-rastreadas.patch` | Patch binário das 732 alterações rastreadas | `0f91f1569c4d2a5cbfdf05859ad09bb482005eef86761003078f432fc5a35a0a` |
| `mqtf-arquivos-nao-rastreados.tar.gz` | Pacote dos 339 arquivos não rastreados | `4fc6a44cd6676d91621ad42da6cc503ae8cefe0e30606fc1bc33eb9930dd46ad` |

Os dois bundles foram verificados pelo Git e registram históricos completos. O pacote dos não rastreados foi conferido com 339 entradas.

### Decisão de reconciliação

O clone alinhado ao remoto será usado como base canônica. O trabalho existente na pasta UnB será avaliado e integrado de maneira seletiva sobre essa base, sem `reset`, `pull`, descarte ou sobrescrita. A privatização do repositório remoto não depende da conclusão dessa integração, pois a salvaguarda já foi realizada.

## 4. Pendências imediatas

- [x] Fabio revogou os tokens clássicos anteriores; autenticação SSH exclusiva configurada e testada em 22/07/2026.
- [x] Tornar `takwaratec/Mulheres-Tecem-Amazonia` privado — concluído por Fabio em 22/07/2026.
- [x] Conferir o efeito da mudança sobre o GitHub Pages — repositório e página pública retornam HTTP 404.
- [ ] Definir e conferir os colaboradores que manterão acesso.
- [x] Higienizar as URLs remotas locais — 16 remotos TakwaraTec convertidos para o alias SSH `github-takwaratec`; nenhuma credencial incorporada remanescente.
- [ ] Iniciar a auditoria de conteúdo dos 14 repositórios que permanecerão públicos.

## 5. Campos da próxima auditoria

Para cada repositório serão acrescentados: responsável, participantes, finalidade, estado, Pages/Vercel, licença, dados sensíveis encontrados, risco de propriedade intelectual, última revisão e próxima ação.

## 6. Fotografia operacional local — 22/07/2026

| Repositório local relevante | Alterações locais | Superfície detectada | Observação |
|---|---:|---|---|
| `acervo-soberania-tecnologica` | 1.148 | MkDocs | Prioridade máxima; não publicar antes de inventariar e revisar o diff |
| `ECOSALA` | 33 | MkDocs | Preservar mudanças e separar arquivos gerados antes do saneamento |
| `fabrica-modelo` | 7 | MkDocs | Auditar edital, negociação, propriedade intelectual e publicação |
| `ludmila-athis-df` | 2 | MkDocs | Auditar perfis, consentimento e materiais brutos |
| `unb-desafios-amazonia-2026` | 1 | MkDocs | Auditar fronteira entre projeto e trajetória pessoal |
| `takwara-mentoria-vercel` | 6 | Vercel/código | Auditar conteúdo publicado e variáveis locais |
| `docmd-test-takwara` | 2 | Sem site detectado | Decidir função ou arquivamento |
| `fundo-vaga-lumen-2026` | 0 | Sem site detectado | Árvore limpa; auditar conteúdo público |
| `eco-prancha` | 0 | Sem site detectado | Árvore limpa; auditar conteúdo público |
| `plataforma-juventude-solidaria-2026` | 0 | MkDocs | Árvore limpa; auditar conteúdo e publicação |
| `Personagens-Bambu` | 0 | MkDocs | Árvore limpa; auditar alegações e público |
| `Mentoria_Comunidades_RaioX` | 0 | MkDocs | Árvore limpa; auditar fronteira metodológica |

Também foram encontrados ativos históricos locais não representados na lista inicial da conta TakwaraTec: `BD-BAMBU`, `Takwara-Tech`, `UnB/Mulheres_Bioeconomia_Amazonia` e `Install-Git-Desktop`. Eles serão classificados como ativos, históricos, auxiliares ou descartáveis sem exclusão automática.

### Alerta de autenticação

O alerta foi resolvido em 22/07/2026. A cópia histórica do MQTF e os demais remotos da conta TakwaraTec usam agora o alias SSH dedicado `github-takwaratec`. A conta histórica Resck não foi alterada.
