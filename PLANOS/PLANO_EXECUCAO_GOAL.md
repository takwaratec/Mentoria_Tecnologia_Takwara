# Plano de Execução em Etapas — Goal de Governança 2026

> **Status:** ⏳ Para avaliação do Fabio (não aprovado, não commitado)
> **Data:** 2026-07-31
> **Escopo:** Mentoria_Tecnologia_Takwara (administrativo) + acervo-soberania-tecnologica (científico)
> **Base:** PLANOS/#PLANO_REPOSITORIO_ADMINISTRATIVO.md + _privado/inventarios/#PLANO_REPOSITORIO_CIENTIFICO.md
> **Autor:** Hermes Agent (elaborado a partir dos planos e do estado real dos repositórios)

---

## 0. Como usar o Goal (Hermes)

| Comando | Efeito |
|---------|--------|
| `/goal <texto>` | Define um objetivo permanente; o Hermes trabalha nele entre turnos até concluir |
| `/goal status` | Mostra progresso do goal ativo |
| `/goal pause` / `/goal resume` | Pausar / retomar o goal |
| `/goal clear` | Encerrar o goal |
| `/cron` | Gerencia tarefas agendadas (recorrentes) |

**Goal sugerido para digitar no CLI:**

```
/goal Executar plano de governança 2026 em 5 etapas: 1) sanitizar
      Mentoria, 2) integridade do acervo, 3) registros canônicos,
      4) automação controlada, 5) publicação segura — sempre com
      commit/push/deploy sob aprovação explícita do Fabio.
```

---

## ETAPA 1 — SANITIZAÇÃO MENTORIA (urgente)

| # | Ação | Estado |
|---|------|--------|
| 1.1 | Renomear `PLANOS/#PLANO_REPOSITORIO_ADMINISTRATIVO.md` sem "#" (caractere problemático) | ⏳ |
| 1.2 | Eleger estrutura canônica (ADMIN/ na raiz OU governance/) e eliminar triplicação com `docs/04_ADMINISTRACAO_E_ESTRATEGIA/` | ⏳ |
| 1.3 | Revisar e commitar conjunto pendente (mkdocs.yml com gaveta admin, docs/04_ADMINISTRACAO_E_ESTRATEGIA/, RELATORIOS/auditorias/, deleções Reclamacao_Vivo) | ⏳ |
| 1.4 | Decidir destino de `TRIAGEM_BRUTA/` e das 2 fichas acadêmicas ainda em `docs/analises/` | ⏳ |
| 1.5 | Registrar sanitização formal em `_privado/sanitization/` (decisão, plano, inventário antes/depois, relatório) | ⏳ |

**Critério de conclusão:** working tree limpo, dados sensíveis fora do site, decisões registradas.

---

## ETAPA 2 — INTEGRIDADE DO ACERVO

| # | Ação | Estado |
|---|------|--------|
| 2.1 | Aprovar gavetas lógicas (9 públicas + 4 quarentena + 4 privadas) e aplicar no mkdocs.yml OU em GOVERNANCA_DOCUMENTAL.md | ⏳ |
| 2.2 | Corrigir os 11 links do nav que apontam para arquivos inexistentes | ⏳ |
| 2.3 | Criar index.md nos 12 subdiretórios de `docs/analyses/` | ⏳ |
| 2.4 | Adotar schema de ficha alinhado à nomenclatura REAL do acervo (BAM_01, PER_10, SCI_...) em vez de `ficha-AAAA-NNNNNN` | ⏳ |
| 2.5 | Implementar máquina de estados documentais no front matter (recebido → publicado + excepcionais) | ⏳ |

**Critério de conclusão:** nav sem quebras, fichas com front matter padronizado e estados válidos.

---

## ETAPA 3 — GOVERNANÇA (registros canônicos)

| # | Ação | Estado |
|---|------|--------|
| 3.1 | Criar `governance/repositories.yaml` (a partir de ADMIN/REPOSITORIOS.yaml, com IDs permanentes REPO-*) | ⏳ |
| 3.2 | Criar `governance/fronts.yaml` com IDs permanentes (FR-MENTORIA, FR-ACERVO, FR-FABRICA-MODELO...) | ⏳ |
| 3.3 | Política de busca vetorial com deny-list (_privado, _quarentena, TRIAGEM_BRUTA, transcrições) | ⏳ |
| 3.4 | Criar CHANGELOG.md e eliminar contagens manuais (gerar automaticamente) | ⏳ |

**Critério de conclusão:** um único registro por repositório/frente, sem divergências entre documentos.

---

## ETAPA 4 — AUTOMAÇÃO CONTROLADA

| # | Ação | Estado |
|---|------|--------|
| 4.1 | Scripts validadores (frontmatter, links, duplicatas, conteúdo privado na árvore pública) | ⏳ |
| 4.2 | GitHub Actions com `mkdocs build --strict` + validadores | ⏳ |
| 4.3 | Reativar cron jobs (hoje com erro 403 de provider opencode-go/deepseek-v4-flash) | ⏳ |
| 4.4 | Agendar Biblioteca Livre (4 obras ✅ já inventariadas em LIVROS_REPRODUTIVEIS_SITE_INTERATIVO.md) | ⏳ |

**Critério de conclusão:** builds e validações automáticas passando; cron jobs entregando.

---

## ETAPA 5 — PUBLICAÇÃO SEGURA

| # | Ação | Estado |
|---|------|--------|
| 5.1 | Deploy final do Mentoria (após Etapa 1 concluída) | ⏳ |
| 5.2 | Push + deploy do Ludmila (push já feito em 31/07 — deploy pendente) | ⏳ |
| 5.3 | Verificação pós-deploy (curl HTTP 200 + ausência de conteúdo privado no HTML) | ⏳ |

**Critério de conclusão:** sites ativos e verificados, sem dados pessoais publicados.

---

## Divergências a resolver antes de aplicar (dos planos originais)

1. **AGENTS.md**: plano administrativo propõe mover para `governance/`, mas o Hermes só auto-carrega AGENTS.md da RAIZ. → Manter na raiz.
2. **Estrutura administrativa**: ADMIN/ (raiz) × governance/ (plano) × docs/04_ADMINISTRACAO_E_ESTRATEGIA/ (cópias p/ site). → Eleger UM canônico.
3. **Nomenclatura de fichas**: `ficha-AAAA-NNNNNN` (plano) × códigos reais BAM_01/PER_10/SCI_... → Alinhar schema à nomenclatura real.
4. **Diretório privado**: `private/` (plano) × `_privado/` (já em uso). → Padronizar `_privado/`.
5. **Arquivos com "#"**: nomes começando com `#` causam problemas em shell/git. → Renomear.

---

## Protocolo permanente (já vigente)

- Commit, push e deploy são autorizações INDEPENDENTES — uma não autoriza a seguinte.
- Nenhum documento é alterado sem permissão explícita do Fabio.
- Nenhum commit é feito sem revisão prévia + build local.
- Dados pessoais, negociações e transcrições brutas ficam fora de `docs/` público.
- Backup antes de qualquer sobrescrita.
