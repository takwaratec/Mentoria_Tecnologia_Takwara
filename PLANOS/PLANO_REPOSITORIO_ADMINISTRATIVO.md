# Plano de Melhoria — Repositório Administrativo e de Governança

## 1. Objetivo

Transformar o repositório administrativo da Mentoria Tecnologia Takwara em um centro confiável de governança do ecossistema, separando apresentação pública, operação interna, memória do agente e informações confidenciais.

## 2. Escopo

Este plano se aplica ao repositório administrativo ou maestro que contém:

- `README.md`;
- `AGENTS.md` master;
- `FRENTES_DE_TRABALHO.md`;
- `MANUAL_OPERACAO.md`;
- planos de ação;
- scripts de busca e manutenção;
- regras de fronteira entre repositórios;
- registros de sanitização;
- memória operacional do Hermes Agent.

Não inclui fichas científicas, estados da arte ou referências técnicas, que devem permanecer no repositório científico.

## 3. Princípios obrigatórios

1. Um documento deve pertencer a um único repositório canônico.
2. Dados pessoais e negociações não devem ficar em documentos públicos.
3. O agente não pode alterar suas próprias regras sem aprovação.
4. Commit, push e deploy são autorizações distintas.
5. Ações administrativas devem ser auditáveis e reversíveis.
6. Frentes de trabalho devem usar identificadores permanentes.
7. Contagens e estados devem ser gerados automaticamente quando possível.
8. Memória narrativa não substitui registros estruturados.

## 4. Problemas prioritários a corrigir

### 4.1. Divergências entre documentos

Atualmente há inconsistências em:

- número de frentes;
- numeração das frentes;
- quantidade de fichas;
- nomes dos repositórios;
- estados dos projetos;
- datas de atualização;
- regras de automação.

### 4.2. Excesso de informações sensíveis em documentos mestres

Separar dos arquivos públicos:

- negociações;
- posições de parceiros;
- estratégias jurídicas;
- informações financeiras;
- viagens;
- documentos reservados;
- observações pessoais;
- contatos e atribuições sensíveis.

### 4.3. Permissões excessivas do agente

Retirar autorização automática para:

- commit;
- push;
- deploy;
- edição de `AGENTS.md`;
- alteração de documentos de governança;
- transferência entre repositórios;
- exclusão de arquivos;
- publicação de conteúdo de parceiros.

### 4.4. Falta de controle de escopo

Toda tarefa deve declarar:

- repositório;
- frente;
- arquivos permitidos;
- arquivos proibidos;
- nível de risco;
- necessidade de aprovação;
- autorização para commit, push e deploy.

### 4.5. Busca vetorial sem política formal de privacidade

Excluir da indexação:

- diretórios privados;
- quarentena;
- transcrições;
- documentos jurídicos;
- contratos;
- negociações;
- dados pessoais;
- triagem bruta.

## 5. Arquitetura recomendada

```text
/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── governance/
│   ├── policies/
│   │   ├── git-policy.md
│   │   ├── publication-policy.md
│   │   ├── privacy-policy.md
│   │   ├── repository-boundaries.md
│   │   └── agent-permissions.md
│   ├── repositories.yaml
│   ├── fronts.yaml
│   ├── actors-public.yaml
│   └── schemas/
├── operations/
│   ├── MANUAL_OPERACAO.md
│   ├── checklists/
│   ├── runbooks/
│   └── templates/
├── plans/
├── scripts/
├── tests/
├── _private/
│   ├── actors/
│   ├── negotiations/
│   ├── legal/
│   ├── sanitization/
│   └── transcripts/
└── _quarantine/
```

## 6. Registro canônico de repositórios

Criar `governance/repositories.yaml`:

```yaml
repositories:
  - id: REPO-MENTORIA
    name: Mentoria_Tecnologia_Takwara
    owner: takwaratec
    visibility: public
    lifecycle: active
    public_reference: allowed
    front: FR-MENTORIA

  - id: REPO-ACERVO
    name: acervo-soberania-tecnologica
    owner: takwaratec
    visibility: public
    lifecycle: active
    public_reference: allowed
    front: FR-ACERVO

  - id: REPO-TAKWARA-TECH
    name: Takwara-Tech
    owner: Resck
    visibility: restricted-reference
    lifecycle: legacy
    public_reference: prohibited
```

Os demais documentos devem ser gerados ou validados com base nesse registro.

## 7. Registro canônico de frentes

Criar `governance/fronts.yaml` com identificadores permanentes:

```yaml
fronts:
  - id: FR-MENTORIA
    name: Mentoria
    repository: REPO-MENTORIA
    status: active

  - id: FR-ACERVO
    name: Acervo Cientifico
    repository: REPO-ACERVO
    status: active

  - id: FR-FABRICA-MODELO
    name: Fabrica Modelo
    repository: REPO-FABRICA-MODELO
    status: awaiting-definition
```

A posição na lista pode mudar sem alterar o identificador.

## 8. Separação entre documentos públicos e privados

### Público

- missão do ecossistema;
- mapa resumido dos repositórios;
- regras gerais de governança;
- documentação de uso;
- políticas editoriais;
- links aprovados.

### Privado

- contatos;
- negociações;
- estratégias jurídicas;
- informações financeiras;
- atas não sanitizadas;
- transcrições;
- conflitos;
- documentos pessoais;
- avaliações internas de parceiros.

### Quarentena

- materiais ainda não classificados;
- duplicatas;
- arquivos com possível dado pessoal;
- documentos candidatos à exclusão;
- conteúdos com origem ou autorização incerta.

## 9. Matriz de permissões do Hermes

| Operação | Automática | Aprovação necessária |
|---|---:|---:|
| Ler arquivos | Sim | Não |
| Pesquisar localmente | Sim | Não |
| Criar relatório | Sim | Não |
| Criar arquivo temporário | Sim | Não |
| Criar branch local | Sim | Não |
| Editar dentro do escopo autorizado | Sim | Conforme risco |
| Alterar `AGENTS.md` | Não | Sim |
| Alterar `FRENTES_DE_TRABALHO.md` | Não | Sim |
| Commit | Não | Sim |
| Push | Não | Sim |
| Deploy | Não | Sim |
| Mover entre repositórios | Não | Sim |
| Excluir arquivos | Não | Sim |
| Reescrever histórico Git | Não | Aprovação especial |
| Publicar dados de parceiros | Não | Sim |
| Indexar diretório privado | Proibido | Não aplicável |

## 10. Workflow administrativo seguro

### Etapa 1 — Identificação

```yaml
repository:
front:
task_type:
visibility:
risk_level:
```

### Etapa 2 — Pré-verificação

- confirmar repositório;
- confirmar branch;
- confirmar remoto;
- consultar regras centrais e locais;
- verificar estado do Git;
- verificar escopo autorizado;
- avaliar privacidade;
- avaliar fronteiras.

### Etapa 3 — Plano

```yaml
files_to_read: []
files_to_change: []
files_to_create: []
prohibited_paths: []
risks: []
tests: []
requires_approval: true
```

### Etapa 4 — Execução local

- criar branch por tarefa;
- aplicar alterações;
- não fazer commit;
- preservar originais;
- registrar decisões.

### Etapa 5 — Validação

- validar YAML;
- verificar links;
- verificar build;
- procurar segredos;
- procurar dados pessoais;
- verificar fronteiras;
- executar `git diff --check`;
- apresentar diff.

### Etapa 6 — Aprovações independentes

1. aprovar alterações;
2. aprovar commit;
3. aprovar push;
4. aprovar deploy.

Uma aprovação não autoriza automaticamente as seguintes.

## 11. Política de Git

Workflow recomendado:

```bash
git status --short
git branch --show-current
git remote -v
git pull --ff-only
git switch -c hermes/<tarefa>

python scripts/validate_governance.py
python scripts/check_private_content.py
python scripts/check_repository_boundaries.py
mkdocs build --strict

git diff --check
git diff --stat
git diff
```

Commit, push e deploy somente após autorização.

## 12. Política de sanitização

Criar registros formais:

```text
_private/sanitization/
├── DECISAO-SANITIZACAO-AAAA-MM-DD.md
├── PLANO-SANITIZACAO-AAAA-MM-DD.yaml
├── INVENTARIO-ANTES.csv
├── INVENTARIO-DEPOIS.csv
└── RELATORIO-EXECUCAO.md
```

A política deve definir:

- origem dos arquivos;
- destino;
- tratamento de dados pessoais;
- tratamento de duplicatas;
- arquivos para quarentena;
- itens candidatos à exclusão;
- necessidade de limpeza do histórico Git;
- condição para novo deploy.

## 13. Política da busca vetorial

```yaml
vector_index:
  allowed:
    - docs/public/**
    - README.md
  denied:
    - "**/_private/**"
    - "**/_quarantine/**"
    - "**/TRIAGEM_BRUTA/**"
    - "**/transcripts/**"
    - "**/ACERVO_RESTRITO/**"
    - "**/*.env"
```

Cada fragmento deve registrar:

- repositório;
- arquivo;
- seção;
- linhas;
- hash;
- visibilidade;
- data de indexação.

## 14. Documentos existentes: destino recomendado

### `README.md`

Manter apenas:

- propósito;
- arquitetura;
- documentos de governança;
- links estáveis;
- data da última sincronização.

Remover status cotidiano e números mantidos manualmente.

### `AGENTS.md`

Manter:

- princípios;
- hierarquia de instruções;
- proibições;
- permissões;
- workflow seguro.

Mover dados pessoais, estados de parceiros e negociações para `_private/`.

### `FRENTES_DE_TRABALHO.md`

Converter gradualmente em visão gerada a partir de `fronts.yaml`.

Manter no documento público apenas status resumidos e autorizados.

### `MANUAL_OPERACAO.md`

Atualizar para retirar:

- commit automático;
- push automático;
- deploy automático;
- autoedição do `AGENTS.md`;
- promessas de ações externas sem confirmação.

### Arquivo de sanitização

Transformar em:

- decisão;
- plano;
- inventário;
- relatório de execução.

Não manter conversa bruta como documento permanente de governança.

## 15. Scripts recomendados

```text
scripts/
├── validate_governance.py
├── generate_readme_status.py
├── generate_fronts_report.py
├── scan_personal_data.py
├── scan_secrets.py
├── check_repository_boundaries.py
├── check_private_content.py
└── build_vector_index.py
```

## 16. Plano de implementação

### Fase 1 — Sanitização e privacidade

- classificar o repositório;
- remover dados sensíveis de documentos públicos;
- formalizar sanitização;
- excluir diretórios privados do build e da indexação;
- verificar histórico Git;
- suspender deploy até auditoria.

### Fase 2 — Segurança operacional

- retirar commit automático;
- retirar autoedição do `AGENTS.md`;
- separar commit, push e deploy;
- criar branch por tarefa;
- exigir diff;
- adicionar scanner de dados pessoais e segredos.

### Fase 3 — Coerência documental

- criar `repositories.yaml`;
- criar `fronts.yaml`;
- adotar identificadores permanentes;
- eliminar contagens manuais;
- sincronizar nomes e estados;
- criar changelog.

### Fase 4 — Automação controlada

- gerar mapas e relatórios automaticamente;
- validar fronteiras;
- integrar testes ao GitHub Actions;
- atualizar busca vetorial com política de privacidade;
- gerar painéis sem expor dados internos.

## 17. Critérios de aceitação

O repositório administrativo estará pronto para operação supervisionada quando:

- o agente não puder alterar suas próprias regras;
- commit, push e deploy exigirem aprovações independentes;
- existir registro canônico de repositórios;
- existir registro canônico de frentes;
- os documentos não divergirem em nomes e estados;
- dados pessoais estiverem separados;
- quarentena estiver fora do build e da indexação;
- toda alteração apresentar diff;
- fronteiras forem verificadas por script;
- o README não funcionar como painel operacional manual.

## 18. Resultado esperado

Um repositório administrativo capaz de:

- coordenar múltiplas frentes;
- preservar fronteiras institucionais;
- proteger informações internas;
- orientar agentes com segurança;
- registrar decisões;
- evitar publicação acidental;
- manter estados e mapas consistentes;
- permitir automação sem perda de controle humano.
