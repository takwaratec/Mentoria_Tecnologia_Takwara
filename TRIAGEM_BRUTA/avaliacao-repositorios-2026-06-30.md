# Avaliação de Conformidade dos Repositórios — 30/06/2026

Protocolos de referência: AGENTS.md na raiz, README.md, mkdocs.yml (e pastas); TRIAGEM/ ou TRIAGEM-BRUTA/ para material bruto; .md soltos na raiz vão para docs/; transcrições NUNCA versionadas; docs de mentoria NÃO em repos de projeto.

---

## 1. ECOSALA

**Estado da raiz:**
- AGENTS.md ✅ | README.md ✅ | mkdocs.yml ✅
- sentinel_monitor.py ⚠️ (solta na raiz — ideal: mover para scripts/)

**AGENTS.md:** ✅ Completo. Escopo, estrutura, fronteiras, instruções para agentes, links externos.

**TRIAGEM-BRUTA:** ✅ Existe e está no .gitignore (nada versionado dentro).

**Links quebrados:** Nenhum. mkdocs.yml nav → todos os caminhos de arquivo existem. Links externos (GH Pages, GitHub) parecem válidos.

**Transcrições:** ❌ docs/12_REUNIOES/ contém 2 arquivos .txt TRANSCRICAO versionados:
  - 2026-06-06_TRANSCRICAO_REUNIAO_ALINHAMENTO_PROPOSTA_VIVEIRO.txt
  - 2026-06-06_TRANSCRICAO_REUNIAO_PLANEJAMENTO_VIVEIRO.txt
  Violam regra: transcrições NUNCA versionadas (só ATAS/ memoriais .md).

**Docs de mentoria/ecossistema:** ⚠️ docs/mensagem-andre-whatsapp.md é uma mensagem pessoal/Fabio → André, não pertence ao repo do coletivo.

**Ações recomendadas:**
1. Mover sentinel_monitor.py para scripts/
2. Remover ou mover transcrições .txt de docs/12_REUNIOES/ para TRIAGEM-BRUTA/ com .gitignore
3. Remover mensagem-andre-whatsapp.md ou mover para repositório pessoal
4. Converter transcrições necessárias em ATAS .md (apenas pautas/atas)

---

## 2. plataforma-juventude-solidaria-2026 (MSTJS)

**Estado da raiz:**
- AGENTS.md ✅ | README.md ✅ | mkdocs.yml ✅
- sentinel_monitor.py ⚠️ (solta na raiz)
- boletim_sentinel_editais_2026.md ❌ (.md solto na raiz — deve ir para docs/)
- PROPOSTA_GABARITO_JUVENTUDE_SOLIDARIA.md ❌ (duplicado na raiz e em docs/projetos/)

**AGENTS.md:** ✅ Completo. Escopo, estrutura, fronteiras, instruções para agentes.

**TRIAGEM-BRUTA:** ❌ NÃO existe. .gitignore referencia a pasta, mas ela não foi criada.

**Links quebrados:** mkdocs.yml referencia logo/favicon em `assets/images/terra_viva.png` — verificar existência. Demais links OK.

**Transcrições:** ✅ Nada identificado.

**Binários versionados:** ⚠️ planilha-orcamentaria.xlsx (65KB), 3 .png de cartografia (~2.7MB total), e diversas imagens em docs/assets/ — parcialmente aceitável em docs/assets/ mas .xlsx deveria estar em TRIAGEM-BRUTA.

**Pastas numeradas:** 02_PROPOSTAS, 06_CARTOGRAFIA_IMAGENS, 07_DOCUMENTOS_PROJETO, 08_REDES_SOCIAIS, 09_IDENTIDADE_VISUAL, 13_PROJETOS, 14_MIDIAS_ASSETS, 15_EXTRACAO_PDFS — herança de exportação WhatsApp. Misturam processado com bruto. Sem TRIAGEM-BRUTA para isolar.

**Ações recomendadas:**
1. Criar TRIAGEM-BRUTA/ e mover material bruto (planilha .xlsx, imagens de cartografia, PDFs não convertidos)
2. Mover sentinel_monitor.py para scripts/ ou TRIAGEM-BRUTA/
3. Mover boletim_sentinel_editais_2026.md para docs/
4. Remover PROPOSTA_GABARITO_JUVENTUDE_SOLIDARIA.md da raiz (manter só em docs/projetos/)
5. Avaliar se pastas numeradas devem ser consolidadas em docs/ ou TRIAGEM-BRUTA/

---

## 3. eco-prancha (prancha vegetal)

**Estado da raiz:**
- AGENTS.md ✅ | README.md ✅
- mkdocs.yml ❌ AUSENTE — não há configuração de site MkDocs
- .gitignore ❌ AUSENTE

**AGENTS.md:** ✅ Sucinto (46 linhas). Escopo, fronteiras bem definidas. Instruções para agente básicas.

**TRIAGEM-BRUTA:** ❌ NÃO existe. Material bruto está em docs/02_TRIAGEM/WhatsApp Chat - Marcello Pedro/ — DENTRO de docs/ ❌.

**Links quebrados:** AGENTS.md referencia `docs/01_PESQUISA/ESTADO_DA_ARTE.md` que ✅ existe. README.md com 8 links Instagram (externos, OK se válidos).

**Transcrições:** ❌ GRAVE: docs/02_TRIAGEM/WhatsApp Chat - Marcello Pedro/_chat.txt está VERSIONADO (git ls-files confirmou). Conversa WhatsApp completa com mídias versionadas.

**Binários versionados:** ❌ 13 arquivos binários versionados em docs/02_TRIAGEM/ (4 .opus áudio, 2 .mp4 vídeo, 3 .jpg, 2 .pdf, 2 .webp sticker). Sem .gitignore para proteger.

**Sem mkdocs.yml:** Repositório não gera site GH Pages — é só repositório de documentação. Docs/ existe mas sem mkdocs.yml para navegação.

**Ações recomendadas:**
1. CRIAR .gitignore (TRIAGEM-BRUTA/, __pycache__/, .DS_Store, site/)
2. MOVER docs/02_TRIAGEM/ para TRIAGEM-BRUTA/ na raiz (criar a pasta)
3. REMOVER do versionamento: _chat.txt e todos os binários dentro de 02_TRIAGEM
4. CRIAR mkdocs.yml se houver intenção de site GH Pages; senão, considerar estrutura mais simples
5. Adicionar AGENTS.md com referência ao mkdocs (se houver)

---

## 4. unb-desafios-amazonia-2026

**Estado da raiz:**
- AGENTS.md ✅ | README.md ✅ | mkdocs.yml ✅ | .agents/ ✅ (scripts)
- Nada solto na raiz além do esperado ✅

**AGENTS.md:** ✅ Completo e bem estruturado (80 linhas). Escopo, estrutura, fronteiras, instruções para agentes, scripts disponíveis, links externos.

**TRIAGEM-BRUTA:** ✅ Existe e está no .gitignore. Subpastas organizadas (01_REUNIOES, 02_DOCUMENTOS, 03_REGULAMENTOS, 04_REFERENCIAS).

**Links quebrados:** README.md referências locais (`docs/index.md`, `docs/edital/regulamento.md`, etc.) — todos existem ✅. Link externo GOV_PROTOCOLO_SEGURANCA_CANCUN.md ✅.

**Transcrições:** ✅ TRIAGEM-BRUTA/WhatsApp /_chat.txt dentro de pasta no .gitignore — não versionado. Decupagens de áudio em .md dentro de TRIAGEM-BRUTA/ — ignorados.

**Documentos de mentoria:** ✅ Nada identificado.

**Observações:** Melhor estrutura entre os 5 repositórios avaliados. A única ressalva é o diretório TRIAGEM-BRUTA/WhatsApp  (com espaço no final do nome) — convenção de nomenclatura.

**Ações recomendadas:**
1. Renomear pasta TRIAGEM-BRUTA/WhatsApp  para TRIAGEM-BRUTA/01_REUNIOES/WhatsApp (remover espaço no final)
2. Manter estrutura — é o repo mais conforme

---

## 5. Personagens-Bambu

**Estado da raiz:**
- AGENTS.md ✅ | README.md ✅ | mkdocs.yml ✅
- Pastas na raiz: assets/, design-system/, flow-projetos/, personagens/, prompts/

**AGENTS.md:** ✅ (49 linhas). Escopo e estrutura definidos. Instruções para agentes resumidas. Menciona GitHub Actions para deploy.

**TRIAGEM-BRUTA:** ❌ NÃO existe. .gitignore só exclui assets/raw/.

**Diretórios duplicados (raiz + docs/):** ❌
  - `personagens/` (raiz) → só template.md · `docs/personagens/` → elenco.md, biotipos-e-roteiro.md + template.md
  - `prompts/` (raiz) → workbook-referencia.md · `docs/prompts/` → workbook-referencia.md (duplicado)
  - `design-system/` (raiz) → README.md · `docs/design-system/` → README.md + index.md
  - `flow-projetos/` (raiz) → vazio? · `docs/flow-projetos/` → index.md
  - `assets/` (raiz) → raw/ + README.md · `docs/assets/` → images/ + svg/

  Conteúdo duplicado ou distribuído inconsistentemente entre raiz e docs/.

**Links quebrados:** Nenhum. Links externos para Google Flow, HeyGen, ChatGPT, Kling AI.

**Transcrições:** ✅ Nada identificado.

**Documentos de mentoria:** ⚠️ README.md menciona "Mentoria Tecnologia Takwara — 7 Lições do Bambu + 7 Pilares de Edgar Morin" — são os temas do projeto em si (os personagens são baseados nisso), não docs de mentoria propriamente ditos. Aceitável.

**Ações recomendadas:**
1. CRIAR TRIAGEM-BRUTA/ para assets crus (imagens, vídeos, fontes)
2. CONSOLIDAR diretórios: escolher entre raiz ou docs/ para cada pasta. Sugestão: usar docs/ como fonte do site (MkDocs) e raiz apenas para AGENTS.md, README.md, mkdocs.yml. Mover personagens/, prompts/, design-system/, flow-projetos/ definitivamente para docs/.
3. Remover duplicações
4. Adicionar .gitignore com TRIAGEM-BRUTA/ se criada

---

## Resumo Geral

| Critério | ECOSALA | MSTJS | eco-prancha | unb-desafios | Personagens |
|---|---|---|---|---|---|
| AGENTS.md na raiz | ✅ | ✅ | ✅ | ✅ | ✅ |
| Instruções para agentes | ✅ completo | ✅ completo | ✅ básico | ✅ completo | ✅ básico |
| mkdocs.yml | ✅ | ✅ | ❌ ausente | ✅ | ✅ |
| TRIAGEM/BRUTA | ✅ | ❌ | ❌ | ✅ | ❌ |
| Transcrições versionadas | ❌ 2 .txt | ✅ | ❌ _chat.txt | ✅ | ✅ |
| .md soltos na raiz | ⚠️ 1 .py | ❌ 2 .md | ✅ | ✅ | ❌ pastas duplicadas |
| Docs mentoria no repo | ⚠️ msg pessoal | ✅ | ✅ | ✅ | ⚠️ aceitável |
| Binários versionados | ✅ | ⚠️ .xlsx+.png | ❌ 13 binários | ✅ | ✅ |
| **Nota** | **Regular** | **Ruim** | **Crítico** | **Bom** | **Regular** |

**Prioridade de ações corretivas:**
1. 🚨 eco-prancha — mais crítico: transcrição e binários versionados, sem .gitignore, sem TRIAGEM
2. ⚠️ MSTJS — sem TRIAGEM, .md duplicados na raiz, .xlsx versionado
3. ⚠️ ECOSALA — transcrições versionadas, msg pessoal no repo
4. ⚠️ Personagens-Bambu — pastas duplicadas raiz/docs, sem TRIAGEM
5. ✅ unb-desafios — quase conforme (só renomear pasta WhatsApp)

*Relatório gerado por Hermes Agent em 30/06/2026*
