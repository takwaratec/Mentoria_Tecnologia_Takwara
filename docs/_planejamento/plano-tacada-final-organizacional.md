# Plano de Trabalho — Última Tacada Organizacional

> **Objetivo:** Matriz enxuta e funcional para todas as frentes.
> **Regra de ouro:** Raiz do repositório só com AGENTS.md, README.md, mkdocs.yml. Todo o resto vai para diretórios.

---

## 📊 DIAGNÓSTICO ATUAL

### Mentoria_Tecnologia_Takwara — 28 itens na raiz (muitos soltos)

| Grupo | Itens | Ação |
|-------|-------|------|
| ✅ **Corretos** | AGENTS.md, README.md, mkdocs.yml, FRENTES_DE_TRABALHO.md, MANUAL_OPERACAO.md | Manter |
| 📁 **Pastas corretas** | docs/, PLANOS/, scripts/, overrides/, _privado/ | Manter |
| ❌ **Scripts soltos** | `_check_pdf_libs.py`, `_extract_*.py`, `extract_intros.py`, `parse_chat.py`, `generate_rx.py` | Mover para `scripts/` |
| ❌ **Docs soltos** | `levantamento-fichas-pendentes.md`, `mapa-acervo-personagens.md` | Mover para `docs/` |
| ❌ **Outros** | `_shara_extracted.txt`, `requirements.txt`, `vercel.json` | Mover para `scripts/` ou raiz |
| ❌ **Duplicata** | `01_TRIAGEM_BRUTA/` + `TRIAGEM_BRUTA/` | Unificar |
| ❌ **Temp** | `consolidacao-academico-cientifico/` | Remover (já consolidado) |

### Acervo Científico — Quase limpo (5 itens na raiz)
✅ Só precisa de verificação de AGENTS.md

### Fábrica Modelo — Limpo (3 itens na raiz)
✅ Precisa de AGENTS.md na raiz (está em docs/)

### Vaga Lúmen — 20 itens na raiz (muitos soltos)
❌ 15 arquivos .md soltos → Mover para `docs/`
❌ `regulamento-finep-mais-inovacao.md` → Mover para `EDITAIS/`

---

## 📋 PLANO EM 5 FASES

### FASE 1 — Limpeza da Mentoria (raiz)

| Ação | arquivos | Destino |
|------|----------|---------|
| Mover scripts Python | `_check_pdf_libs.py`, `_extract_full.py`, `_extract_pdf.py`, `_extract_results.py`, `_extract_shara.py`, `extract_intros.py`, `parse_chat.py`, `generate_rx.py` | `scripts/` |
| Mover docs soltos | `levantamento-fichas-pendentes.md`, `mapa-acervo-personagens.md` | `docs/_planejamento/` |
| Mover outros | `_shara_extracted.txt` → `TRIAGEM_BRUTA/`, `requirements.txt` → `scripts/` | |
| Unificar triagem | `01_TRIAGEM_BRUTA/` fundir em `TRIAGEM_BRUTA/` | Manter só `TRIAGEM_BRUTA/` |
| Remover temp | `consolidacao-academico-cientifico/` | Remover (já consolidado) |

### FASE 2 — AGENTS.md de cada repositório

Cada AGENTS.md deve ter:
1. **Escopo** — do que trata este repositório
2. **Estrutura** — pastas e o que contêm
3. **Fronteiras** — o que NÃO deve ser colocado aqui
4. **Instruções para agentes** — coordenadas explícitas para quem chegar
5. **Links para documentos externos** — com caminhos corretos

**Repos que precisam de AGENTS.md:**
- ✅ Mentoria — já tem, precisa revisar links
- ✅ Acervo — já tem, precisa revisar
- ✅ Fábrica Modelo — está em `docs/`, mover para raiz
- ⚠️ Vaga Lúmen — já tem na raiz, precisa revisar
- ❌ Eco Prancha — criar
- ❌ Plataforma Juventude Solidária — criar
- ❌ UnB Desafios Amazônia — criar

### FASE 3 — Varredura e correção de links

**Links quebrados identificados no diagnóstico:**

| Arquivo | Link antigo | Novo caminho |
|---------|-------------|--------------|
| `AGENTS.md` (Mentoria) | `docs/PU_Vegetal_Ficha_Tecnica_Consolidada.md` | `https://github.com/takwaratec/Analises-e-escrita-cientifica/.../pu-vegetal-ficha-tecnica-consolidada.md` |
| `AGENTS.md` (Mentoria) | `docs/carta-intencoes-pesquisador-colaborador-generica.md` | `docs/carta-intencoes-pesquisador-colaborador-generica.md` (mantido) |
| `FRENTES_DE_TRABALHO.md` | Referências a `PLANOS/PAUTA_REUNIAO_FABRICA_MODELO.md` | `fabrica-modelo/docs/pauta-reuniao-fabrica-modelo.md` |
| `MENSAGEM_ANDRE_CONFIRMACAO_3006.md` | Link para pauta no GitHub | Link atualizado |
| `ORGANIZACAO_REUNIAO_3006.md` | `extracao_dados_fichas_cientificas.md` | Link para o acervo |
| `docs/AGENTS.md` (fabrica) | `PLANOS/PAUTA_REUNIAO_FABRICA_MODELO.md` | `docs/pauta-reuniao-fabrica-modelo.md` |

**Metodologia:** grep em todos os .md de todos os repos → identificar todo link que referencie arquivo movido → corrigir com patch.

### FASE 4 — Ajustes finais por repositório

**Mentoria:**
- ✅ Verificar `docs/` — metadados, links, consistência
- ✅ AGENTS.md master atualizado com links corrigidos
- ✅ FRENTES_DE_TRABALHO.md revisado

**Fábrica Modelo:**
- ✅ AGENTS.md da raiz (mover de docs/)
- ✅ Carta de Intenções (já criadas)
- ✅ Proposal Teaser (já criado)
- ✅ Formulário Espelho (já criado)

**Acervo:**
- ✅ AGENTS.md revisado
- ✅ Links para fichas no próprio repo

**Vaga Lúmen:**
- ❌ Mover docs soltos da raiz para `docs/`
- ❌ AGENTS.md revisado
- ❌ Criar pasta `TRIAGEM/` se necessário

**Demais repositórios** (eco-prancha, plataforma-juventude, unb-desafios):
- ❌ Criar AGENTS.md com instruções para agentes
- ❌ Organizar raiz

### FASE 5 — Commit e push generalizado

| Repositório | O que commitar |
|-------------|---------------|
| Mentoria | Limpeza raiz, AGENTS.md revisado, FRENTES_DE_TRABALHO.md, links corrigidos |
| Acervo | AGENTS.md revisado |
| Fábrica Modelo | AGENTS.md na raiz, links corrigidos |
| Vaga Lúmen | Organização raiz, AGENTS.md |
| Demais | AGENTS.md, organização |

---

## ⏱️ ESTIMATIVA DE ESFORÇO

| Fase | arquivos | Tempo estimado |
|------|----------|----------------|
| F1 — Limpeza Mentoria | ~15 movimentações | 5 min |
| F2 — AGENTS.md | ~6 arquivos (revisar/criar) | 15 min |
| F3 — Varredura links | ~10 correções em 4 repos | 10 min |
| F4 — Ajustes finais | 5 repos | 10 min |
| F5 — Commits | 5-6 repos | 5 min |
| **Total** | | **~45 min** |

---

## ✅ AGUARDANDO SUA APROVAÇÃO

Antes de executar, confirme:

1. **Posso unificar** `01_TRIAGEM_BRUTA/` → `TRIAGEM_BRUTA/` na Mentoria?
2. **Posso remover** `consolidacao-academico-cientifico/` (já consolidado)?
3. **Sobre a Vaga Lúmen**: quer que eu organize a raiz também (mover .md soltos para docs/)?
4. **Demais repositórios** (eco-prancha, plataforma-juventude, unb-desafios): quer AGENTS.md com instruções para agentes?

Se preferir, autorize tudo de uma vez com: **"Pode executar o plano completo"**
