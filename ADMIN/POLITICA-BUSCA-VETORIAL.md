# Política de Busca Vetorial — Ecossistema Takwara

> **Status:** Aprovada em 2026-07-31 (Etapa 3 do Plano de Governança)
> **Aplicação:** `scripts/busca_vector.py` e qualquer indexador semântico local
> **Base:** Plano Administrativo §13 + regras de fronteira do AGENTS.md

## 1. Objetivo

A busca vetorial local indexa repositórios `.md` para recuperação rápida.
Esta política define o que PODE e o que NUNCA PODE ser indexado, para
impedir que dados pessoais, negociações e material bruto entrem no índice.

## 2. Diretórios PROIBIDOS de indexar (deny-list)

Qualquer indexador deve excluir, por padrão, estes caminhos:

```text
**/.git/**
**/site/**
**/_privado/**
**/_quarentena/**
**/_quarentena_old/**
**/TRIAGEM-BRUTA/**
**/TRIAGEM_BRUTA/**
**/_acervo_completo/**
**/ACERVO_RESTRITO/**
**/transcripts/**
**/_chat*.txt
**/WhatsApp Chat - */**
**/Conversa do WhatsApp*.txt
**/*.env
**/.env*
```

## 3. Diretórios PERMITIDOS (allow-list)

```text
docs/**          (árvore pública de documentação)
README.md        (raiz)
AGENTS.md        (raiz)
ADMIN/**         (exceto _privado — ver §2)
PLANOS/**
RELATORIOS/**
TAREFAS/**
```

## 4. Registro por fragmento

Cada fragmento indexado deve carregar metadados:

```yaml
repositorio: <nome>
arquivo: <caminho relativo>
secao: <título da seção>
linhas: <início-fim>
hash: <sha256 do trecho>
visibilidade: publico | interno
data_indexacao: AAAA-MM-DD
```

Fragmentos de `ADMIN/`, `PLANOS/`, `RELATORIOS/` e `TAREFAS/` são
`interno`; fragmentos de `docs/` são `publico`.

## 5. Obrigações

1. `scripts/busca_vector.py` deve aplicar a deny-list completa (hoje só
   filtra `site/`, `.git/` e TRIAGEM — precisa adicionar `_privado/`,
   `_quarentena/`, `_acervo_completo/`, transcrições e `.env`).
2. Novos indexadores (MCP, RAG, embeddings) devem seguir esta política.
3. A política só muda com aprovação de Fabio.
4. Reindexar sempre após atualizar a deny-list.

## 6. Verificação

Após qualquer alteração no indexador, rodar:

```bash
python3 scripts/busca_vector.py
# e conferir no log que NENHUM caminho _privado/_quarentena foi indexado
```
