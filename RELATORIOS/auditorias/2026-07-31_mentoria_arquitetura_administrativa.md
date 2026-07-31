# Relatório de Auditoria — Arquitetura Administrativa do Repo Mestre

**Repositório:** `takwaratec/Mentoria_Tecnologia_Takwara`  
**Data da auditoria:** 31/07/2026  
**Auditor:** Hermes Agent  
**Escopo:** mapeamento de conteúdo, classificação por natureza, riscos de exposição e proposta de navegação administrativa.  
**Restrição:** nenhum arquivo foi alterado, movido ou excluído. Este relatório é leitura/recomendação.

---

## 1. Resumo Executivo

| Indicador | Valor |
|-----------|-------|
| Visibilidade atual do repositório | **Público** (`"private": false`, `"visibility": "public"`) |
| GitHub Pages ativo | Sim — `https://takwaratec.github.io/Mentoria_Tecnologia_Takwara/` |
| Arquivos em `docs/` | 42 (md/html/png/css) |
| Arquivos administrativos novos | `ADMIN/`, `RELATORIOS/`, `TAREFAS/`, `PLANOS/` |
| Fichas acadêmicas completas detectadas em `docs/` | **2** (`SOC_PER_005`, `SOC_SIN_001`) |
| Dados sensíveis pessoais detectados em `docs/` | **1** isolado preventivamente em `_privado/cartas/` antes desta auditoria |
| Conteúdo com valores/orçamentos em `docs/` | **1** referência (`PASSO_03`: "25 milhões") |
| Volumes de triagem bruta na raiz | `TRIAGEM_BRUTA/` — centenas de e-mails/telefones de fichas legadas |
| Conteúdo adequado para navegação administrativa | `README.md`, `AGENTS.md`, `MANUAL_OPERACAO.md`, `ADMIN/*`, `RELATORIOS/*`, `TAREFAS/*`, `PLANOS/*` |

**Veredicto geral:** o repositório já funciona como maestro, mas mistura quatro naturezas de conteúdo que precisam de fronteiras claras: (a) governança administrativa, (b) material didático de mentoria, (c) fichas acadêmicas e (d) resíduos de triagem bruta com dados pessoais. A prioridade imediata é tornar o repositório **privado** e depois reorganizar o `mkdocs.yml` para expor só a camada administrativa.

---

## 2. Estado de Visibilidade e Risco

### 2.1 Repositório público no GitHub

```json
{
  "name": "Mentoria_Tecnologia_Takwara",
  "private": false,
  "visibility": "public"
}
```

**Risco:** como o GitHub Pages de repositórios públicos é público na internet, qualquer arquivo em `docs/` pode ser indexado por mecanismos de busca mesmo que não esteja no `nav`. Além disso, o repositório em si (incluindo `TRIAGEM_BRUTA/`, `_privado/`, `FRENTES_DE_TRABALHO.md`, etc.) é clonável por qualquer pessoa.

### 2.2 GitHub Pages

- URL: `https://takwaratec.github.io/Mentoria_Tecnologia_Takwara/`
- Último deploy: `48f97e8` (commit `0725c96`, MkDocs 1.6.1)
- Status HTTP: 200
- A carta Bliska retorna 404 no site (foi isolada em `_privado/cartas/` antes do deploy), mas o repositório público ainda contém o arquivo.

---

## 3. Classificação do Conteúdo

### 3.1 Camada Administrativa — adequada ao repo mestre e ao nav

| Arquivo / Diretório | Natureza | Recomendação de nav |
|---------------------|----------|---------------------|
| `README.md` | Apresentação do ecossistema | `Início` |
| `AGENTS.md` | Regras para agentes de IA | `Governança > AGENTS.md` |
| `MANUAL_OPERACAO.md` | Guia de interação com Hermes | `Governança > Manual de Operação` |
| `FRENTES_DE_TRABALHO.md` | Mapa estratégico das frentes | `Governança > Frentes de Trabalho` |
| `ADMIN/REPOSITORIOS.yaml` | Inventário dos repositórios | `Administração > Repositórios` |
| `ADMIN/REGISTRO_EXECUCOES.md` | Log de execuções autorizadas | `Administração > Registro de Execuções` |
| `RELATORIOS/README.md` | Estrutura de relatórios | `Administração > Relatórios` |
| `TAREFAS/README.md` | Estrutura de tarefas | `Administração > Tarefas` |
| `PLANOS/INVENTARIO-ATIVOS-GITHUB-2026.md` | Inventário de ativos GitHub | `Administração > Ativos GitHub` |
| `PLANOS/PLANO-MESTRE-ATUALIZACAO-REPOSITORIOS-2026.md` | Plano mestre de atualização | `Administração > Plano Mestre` |
| `PLANOS/PLANO-FRENTE-09-UNB-MQTF-AMAZONIA10.md` | Plano de projeto específico | `Projetos > UnB/Amazônia+10` (ou manter só em `PLANOS/`) |
| `docs/carta-intencoes-pesquisador-colaborador-generica.md` | Modelo institucional (com CNPJ Ecolaborativa) | `Governança > Modelo de Carta de Intenções` |

### 3.2 Material Didático de Mentoria — pode permanecer, mas com fronteira clara

| Diretório | Conteúdo | Avaliação |
|-----------|----------|-----------|
| `docs/00_METODOLOGIA/` | Ecossistema de ferramentas, manual de parceria, manifesto, dia 6 | **Adequado** ao repo Mentoria |
| `docs/02_BASE_DE_CONHECIMENTO/` | 7 módulos TEC (ecologia, tratamentos, PU, engenharia, etc.) | **Limítrofe** — são resumos didáticos, mas citam documentos internos (`SCI_011`, `ENG-MEM-T01`) e DOIs. Recomenda-se mantê-los como "sínteses para mentoria", nunca como evidência científica. |
| `docs/03_JORNADA_7_PASSOS/` | Passos de 1 a 7 da mentoria | **Adequado** ao repo Mentoria |
| `docs/apresentacao-mentoria.md` | Apresentação comercial | **Adequado** |
| `docs/index.md` / `index_EN.md` | Home do site | **Adequado** |

### 3.3 Fichas Acadêmicas — devem migrar para o Acervo

| Arquivo | Problema | Destino recomendado |
|---------|----------|---------------------|
| `docs/analises/03_habitacao-social-e-athis/11_permacultura_e_bioconstrucao/SOC_PER_005_DIY_HANDBOOK.md` | Ficha Cavichioli completa (8 seções) | `acervo-soberania-tecnologica` |
| `docs/analises/03_habitacao-social-e-athis/12_design_regenerativo_e_efemerizacao/SOC_SIN_001_SYNERGETICS_CAP1.md` | Ficha Cavichioli completa (8 seções), tradução própria | `acervo-soberania-tecnologica` |

**Justificativa:** o `ADMIN/REPOSITORIOS.yaml` e o `INVENTARIO-ATIVOS-GITHUB-2026.md` estabelecem que o `acervo-soberania-tecnologica` é a "única referência científica do ecossistema". Manter fichas completas no repo mestre viola essa fronteira.

### 3.4 Planejamentos Internos — fora do nav, mas podem ficar no repo

| Arquivo | Natureza | Recomendação |
|---------|----------|--------------|
| `docs/_planejamento/levantamento-fichas-pendentes.md` | Levantamento de conteúdo do Takwara-Tech | Manter em `docs/_planejamento/` (ou mover para `PLANOS/`), **não incluir no nav** |
| `docs/_planejamento/mapa-acervo-personagens.md` | Mapeamento de personagens e repositórios | Manter em `docs/_planejamento/` (ou mover para `PLANOS/`), **não incluir no nav** |
| `docs/_planejamento/plano-tacada-final-organizacional.md` | Plano de reorganização dos repos | Manter em `docs/_planejamento/` (ou mover para `PLANOS/`), **não incluir no nav** |

### 3.5 Dados Sensíveis — requer isolamento imediato

| Local | Tipo de dado | Risco |
|-------|--------------|-------|
| `_privado/cartas/carta-bliska-2026-07-09.md` | E-mail particular do Prof. Bliska e do próprio Fabio | Já isolado da pasta `docs/`, mas ainda no repositório público |
| `TRIAGEM_BRUTA/PARA_REVISAO_TT/` | Dezenas de e-mails e telefones de autores de teses, relatórios e artigos | Repositório público — exposição em massa |
| `TRIAGEM_BRUTA/Análise profunda dos materiais químicos utilizados.md` | Telefone (`2179-8087`) | Repositório público |
| `TRIAGEM_BRUTA/Dia 6 Transcrição.md` | Valor ("5 milhões") e possivelmente outros dados | Repositório público |

**Observação:** `TRIAGEM_BRUTA/` não é copiada para o site (está fora de `docs/`), mas está disponível no GitHub público para qualquer clone.

### 3.6 Orçamentos e Valores

| Local | Ocorrência | Avaliação |
|-------|------------|-----------|
| `PLANOS/PLANO-FRENTE-09-UNB-MQTF-AMAZONIA10.md` | R$ 107,1 milhões, R$ 6M–R$ 10M, etc. | **Adequado** — são valores públicos do edital |
| `docs/03_JORNADA_7_PASSOS/PASSO_03_Estrutura_Formato.md` | "25 milhões" | **Verificar contexto** — se for exemplo de mercado, manter; se for orçamento de projeto, mover para repo do projeto |
| `TRIAGEM_BRUTA/` | Diversos valores em fichas legadas | **Não devem ser publicados** sem revisão de contexto |

---

## 4. Proposta de Navegação (`mkdocs.yml`)

Objetivo: acesso rápido e limpo apenas ao conteúdo administrativo e didático. Remover do nav arquivos acadêmicos, planejamentos internos e sensíveis.

```yaml
nav:
  - Início: index.md
  - Governança:
    - README do Ecossistema: README.md
    - AGENTS.md: AGENTS.md
    - Manual de Operação: MANUAL_OPERACAO.md
    - Frentes de Trabalho: FRENTES_DE_TRABALHO.md
    - Modelo de Carta de Intenções: docs/carta-intencoes-pesquisador-colaborador-generica.md
  - Administração:
    - Repositórios: ADMIN/REPOSITORIOS.yaml
    - Registro de Execuções: ADMIN/REGISTRO_EXECUCOES.md
    - Relatórios: RELATORIOS/README.md
    - Tarefas: TAREFAS/README.md
    - Ativos GitHub: PLANOS/INVENTARIO-ATIVOS-GITHUB-2026.md
    - Plano Mestre: PLANOS/PLANO-MESTRE-ATUALIZACAO-REPOSITORIOS-2026.md
  - Metodologia:
    - Ecossistema de Ferramentas: docs/00_METODOLOGIA/ecossistema-ferramentas.html
    - Manual de Parceria: docs/00_METODOLOGIA/manual-parceria.html
    - Manifesto da Transição: docs/00_METODOLOGIA/manifesto-transicao.html
    - DIA 06 — Finalização da Oferta: docs/00_METODOLOGIA/DIA_06_Finalizacao_Oferta.md
  - Base de Conhecimento (sínteses didáticas):
    - Ecologia e Universo do Bambu: docs/02_BASE_DE_CONHECIMENTO/TEC_01_Ecologia_e_Universo_do_Bambu.md
    - Tratamentos e a Magia do Boro: docs/02_BASE_DE_CONHECIMENTO/TEC_02_Tratamentos_e_A_Magia_do_Boro.md
    - O Poliuretano Vegetal: docs/02_BASE_DE_CONHECIMENTO/TEC_03_O_Poliuretano_Vegetal_e_Aplicacao.md
    - Dossiê Comparativo Biopolímeros: docs/02_BASE_DE_CONHECIMENTO/TEC_03_Dossie_Comparativo_Biopolimeros.md
    - Engenharia e Escala Industrial: docs/02_BASE_DE_CONHECIMENTO/TEC_04_Engenharia_e_Escala_Industrial.md
    - Dossiê Tratamentos Bambu: docs/02_BASE_DE_CONHECIMENTO/TEC_04_Dossie_Tratamentos_Bambu.md
    - Bibliografia e Referências: docs/02_BASE_DE_CONHECIMENTO/TEC_05_Bibliografia_e_Referencias.md
    - Histórico de Autoridade: docs/02_BASE_DE_CONHECIMENTO/TEC_06_Historico_Autoridade.md
    - Química dos Tratamentos: docs/02_BASE_DE_CONHECIMENTO/TEC_07_Quimica_dos_Tratamentos.md
  - Jornada 7 Passos:
    - Passo 1 — Diagnóstico: docs/03_JORNADA_7_PASSOS/PASSO_01_Diagnostico_Persona.md
    - Passo 2 — Jornada do Mentorado: docs/03_JORNADA_7_PASSOS/PASSO_02_Jornada_do_Mentorado.md
    - Passo 3 — Estrutura e Formato: docs/03_JORNADA_7_PASSOS/PASSO_03_Estrutura_Formato.md
    - Passo 4 — Entrega e Acompanhamento: docs/03_JORNADA_7_PASSOS/PASSO_04_Entrega_Acompanhamento.md
    - Passo 5 — Precificação: docs/03_JORNADA_7_PASSOS/PASSO_05_Precificacao.md
    - Passo 6 — Oferta e Naming: docs/03_JORNADA_7_PASSOS/PASSO_06_Oferta_Naming.md
    - Passo 7 — Imersão de Vendas: docs/03_JORNADA_7_PASSOS/PASSO_07_Imersao_Vendas.md
```

**Itens propositalmente excluídos do nav:**
- `docs/_planejamento/*` — planejamentos internos
- `docs/analises/*` — fichas acadêmicas a migrar
- `docs/MANUAL_OBS_REUNIOES.md` — manual técnico de gravação (pode ir em Metodologia se desejado)
- `docs/index_EN.md` e versões `_EN.md` — podem ser incluídas como sub-itens se houver demanda
- `docs/apresentacao-mentoria.md` — pode ir em Governança ou Divulgação

---

## 5. Recomendações

### 5.1 Imediatas (antes de qualquer novo deploy)

1. **Tornar o repositório privado no GitHub.**
   - Caminho: `Settings > General > Danger Zone > Change repository visibility > Private`.
   - Impacto: GitHub Pages de repositórios privados em conta pessoa/organização gratuita **será desativado**. Se Pages for necessário, será preciso upgrade ou publicar via Vercel/Netlify com controle de acesso.
   - Alternativa: manter público, mas remover **todos** os dados sensíveis do histórico Git (rewrite) — esforço muito maior e arriscado.

2. **Mover as duas fichas acadêmicas** (`SOC_PER_005` e `SOC_SIN_001`) para o `acervo-soberania-tecnologica` e deletar do repo mestre.

3. **Isolar ou anonimizar `TRIAGEM_BRUTA/`** — adicionar ao `.gitignore` e/ou mover para armazenamento local fora do repositório público. Se for necessário versionar, o repositório deve ser privado.

4. **Manter `_privado/cartas/` fora de `docs/`** — já está correto, mas deve ser protegido pela privacidade do repositório.

### 5.2 Médio prazo

5. Revisar `docs/02_BASE_DE_CONHECIMENTO/` para garantir que os módulos TEC sejam apresentados como **sínteses didáticas** e nunca como evidência científica primária. Substituir referências a documentos internos (`SCI_011`, `ENG-MEM-T01`) por DOIs ou links para o Acervo.

6. Corrigir os warnings do MkDocs:
   - `PU_Vegetal_Linha_de_Produtos.md` e `PU_Vegetal_Ficha_Tecnica_Consolidada.md` estão no nav mas não existem em `docs/`.
   - Decidir se esses arquivos serão recriados, movidos do Acervo ou removidos do nav.

7. Criar `AGENTS.md` e `README.md` nos repositórios irmãos que ainda não possuem, conforme `PLANO-MESTRE-ATUALIZACAO-REPOSITORIOS-2026.md`.

8. Revisar `docs/carta-intencoes-pesquisador-colaborador-generica.md` — contém CNPJ da Ecolaborativa. Verificar se é seguro mantê-lo público.

---

## 6. Inventário por Diretório

| Diretório / Arquivo | Visibilidade no site | Visibilidade no repo | Natureza | Ação recomendada |
|---------------------|:--------------------:|:--------------------:|----------|------------------|
| `README.md` | ✅ Sim | ✅ Público | Administração | Manter no nav |
| `AGENTS.md` | ❌ Não (raiz) | ✅ Público | Administração | Incluir no nav via `AGENTS.md` |
| `MANUAL_OPERACAO.md` | ❌ Não (raiz) | ✅ Público | Administração | Incluir no nav |
| `FRENTES_DE_TRABALHO.md` | ❌ Não (raiz) | ✅ Público | Administração | Incluir no nav |
| `ADMIN/` | ❌ Não | ✅ Público | Administração | Incluir no nav |
| `RELATORIOS/` | ❌ Não | ✅ Público | Administração | Incluir no nav |
| `TAREFAS/` | ❌ Não | ✅ Público | Administração | Incluir no nav |
| `PLANOS/` | ❌ Não | ✅ Público | Administração | Incluir no nav parcialmente |
| `docs/00_METODOLOGIA/` | ✅ Sim | ✅ Público | Didático | Manter no nav |
| `docs/02_BASE_DE_CONHECIMENTO/` | ✅ Sim | ✅ Público | Didático/limítrofe | Revisar referências internas |
| `docs/03_JORNADA_7_PASSOS/` | ✅ Sim | ✅ Público | Didático | Manter no nav |
| `docs/_planejamento/` | ✅ Sim (acessível por URL) | ✅ Público | Interno | Remover do nav; considerar mover para `PLANOS/` |
| `docs/analises/` | ✅ Sim (acessível por URL) | ✅ Público | Acadêmico | Migrar para Acervo |
| `_privado/cartas/` | ❌ Não | ✅ Público | Sensível | Proteger via repo privado |
| `TRIAGEM_BRUTA/` | ❌ Não | ✅ Público | Sensível/legado | Mover para fora do repo público ou tornar repo privado |
| `site/` | ❌ Não (ignorado) | ❌ Não rastreado | Build | Manter no `.gitignore` |

---

## 7. Dados Sensíveis Encontrados (amostra)

A tabela abaixo é uma amostra dos dados sensíveis em `TRIAGEM_BRUTA/`. O scanner completo encontrou dezenas de e-mails e telefones.

| Arquivo | Tipo de dado | Exemplo |
|---------|--------------|---------|
| `TRIAGEM_BRUTA/PARA_REVISAO_TT/01-_ABR-18_Oficina_FUP.md` | E-mail | `takwara.rapuy@gmail.com` |
| `TRIAGEM_BRUTA/PARA_REVISAO_TT/02-MAI-18_SIEX-60015.md` | E-mail | `taniacristina75@gmail.com` |
| `TRIAGEM_BRUTA/PARA_REVISAO_TT/2012_-_Beraldo_BAMBUCOMCIDOPIROLENHOSO.md` | E-mail | `beraldo@feagri.unicamp.br` |
| `TRIAGEM_BRUTA/PARA_REVISAO_TT/16_-_JAN-20_-_Certificado_de_Compete_ncia-IFB.md` | Telefone | `(61) 2196-2653` |
| `TRIAGEM_BRUTA/PARA_REVISAO_TT/19_-_Relatório_-PIBIT_Barreira_Acustica...` | Telefone | `1597-1608` |
| `_privado/cartas/carta-bliska-2026-07-09.md` | E-mail pessoal | `bliskajr@unicamp.br`, `fabiotakwara@gmail.com` |

---

## 8. Próximos Passos (aguardam decisão)

1. **Tornar o repositório privado?** (Sim / Não / Depois)
2. **Autorizar a migração das fichas `SOC_PER_005` e `SOC_SIN_001` para o Acervo?**
3. **Autorizar a remoção/isolamento de `TRIAGEM_BRUTA/` do histórico público?**
4. **Aprovar a nova estrutura de `mkdocs.yml` proposta neste relatório?**
5. **Autorizar a criação de `AGENTS.md` nos repositórios irmãos?**

---

> **Nota de compliance:** este relatório não alterou nenhum arquivo do repositório além de si próprio. Recomendações que envolvam exclusão, movimentação ou mudança de visibilidade devem ser autorizadas explicitamente antes da execução.
