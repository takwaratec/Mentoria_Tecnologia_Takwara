# CHANGELOG — Mentoria Tecnologia Takwara (Maestro)

> Registro cronológico de mudanças administrativas relevantes do
> repositório-mestre. Detalhes técnicos nos commits; este arquivo resume
> marcos e decisões de governança.

## 2026-07-31 — Sanitização + Governança (Etapas 1–3 do Plano)

### Commit 626b96d — Sanitização do repositório
- **D1:** TRIAGEM_BRUTA sem binários (10 áudios + 7 PDFs movidos para
  backup local em `~/Documents/_backup_sanitizacao_2026-07-31/`); 263 .md
  mantidos como acervo documental de auditoria.
- **D2:** `_privado/` adicionado ao `.gitignore` (paridade com o acervo).
- **D3:** Estrutura canônica definida: `ADMIN/`, `RELATORIOS/`, `TAREFAS/`,
  `PLANOS/` na raiz; `docs/04_ADMINISTRACAO_E_STRATEGIA/` como espelho de
  publicação.
- **D4:** Fichas acadêmicas `SOC_PER_005` e `SOC_SIN_001` removidas
  (fonte canônica = acervo, `_quarentena/_sem_doi/`).
- **D5:** `PLANOS/#PLANO_REPOSITORIO_ADMINISTRATIVO.md` renomeado sem "#";
  "Sanitizacao-Hermes 31-7" movido para `_privado/sanitizacao/`; `.swp`
  removido; deleção `Reclamacao_Vivo` commitada; gaveta "Administração e
  Estratégia" adicionada ao nav (15 arquivos).
- Registro formal: `_privado/sanitizacao/DECISAO-SANITIZACAO-2026-07-31.md`.

### Push
- `0725c96..626b96d main -> main` (alinhado).

### Etapa 3 — Registros canônicos (em andamento)
- `ADMIN/FRENTES.yaml` criado com IDs permanentes `FR-*` (12 frentes).
- `ADMIN/REPOSITORIOS.yaml` ganhou IDs permanentes `REPO-*` (15 repos).
- `ADMIN/POLITICA-BUSCA-VETORIAL.md` criada (deny-list completa).
- Este `CHANGELOG.md` criado.

## 2026-07-31 — Acervo (Etapa 2 do Plano)

### Commit 651166a — Integridade do acervo
- Gavetas lógicas aprovadas registradas em `GOVERNANCA_DOCUMENTAL.md`
  (9 públicas + 4 quarentena + 4 privadas).
- Máquina de estados formalizada + tabela de equivalência dos 8 valores
  em uso.
- Ficha `SCI_014_POLYMERS_ALKALI_TREATMENT.md` renomeada para
  `kamaruddin-et-al-2022-tratamento-alcalino-capim-limao.md` (padrão
  autor-ano) com redirect.
- Deploy automático via GitHub Actions (success).

## 2026-07-31 — Ludmila / ATHIS-DF

### Commit fbb9a1c — Histórico, visita 08/08, oportunidades, app REURB
- Decupagem pessoal 2021-2025 removida do nav E do build (exclude_docs).
- Push + deploy manual (gh-deploy) — página sensível saiu do ar (404).

### Commit e315de0 — CI/CD
- GitHub Actions criado (`mkdocs gh-deploy` no push) — deploy automático
  a partir de agora. Run inicial: success.

---

## Histórico anterior (resumo)

- `0725c96` — estrutura ADMIN/RELATORIOS/TAREFAS, Raio-X, TEC_04, carta privada isolada.
- `d364004` — FRENTES_DE_TRABALHO pós-reunião ECOSALA 07/07.
- `25bc473` — P13: migração MQTF (30 SCI + 31 FICHA + 6 LAB).
