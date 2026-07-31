# TAREFAS/README.md

> Acompanhamento de tarefas operacionais do ecossistema.
> Complementa o FRENTES_DE_TRABALHO.md (visão estratégica) e a ferramenta `todo` do Hermes (sessão atual).

## Estrutura

```
TAREFAS/
├── pendentes/     ← Tarefas identificadas, aguardando priorização
├── autorizadas/   ← Tarefas autorizadas por Fabio, prontas para execução
├── executadas/    ← Tarefas concluídas, com referência ao commit ou relatório
└── bloqueadas/    ← Tarefas que dependem de fator externo
```

## Fluxo

1. Hermes identifica tarefa → registra em `pendentes/`
2. Fabio prioriza e autoriza → move para `autorizadas/`
3. Hermes executa → move para `executadas/` com referência
4. Se depende de externo → move para `bloqueadas/` com motivo

## Relação com outros instrumentos

| Instrumento | Escopo | Atualização |
|-------------|--------|-------------|
| `FRENTES_DE_TRABALHO.md` | Visão estratégica, status, prioridades | Por sessão |
| `todo` (ferramenta Hermes) | Tarefas da sessão atual | Volátil |
| `TAREFAS/` | Histórico e pendências permanentes | Persistente |

## Regras

- NÃO duplicar tarefas que já estão no `FRENTES_DE_TRABALHO.md` como pendências.
- NÃO versionar tarefas sem autorização.
- NÃO armazenar senhas, tokens ou dados pessoais nos arquivos de tarefa.
- Preferir arquivos .md por tarefa ou lote nomeados como `YYYY-MM-DD_descricao.md`.

---

*Estrutura criada em 30/07/2026. Nenhuma tarefa versionada ainda.*
