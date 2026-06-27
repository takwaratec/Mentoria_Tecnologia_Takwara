# AGENTS.md — Mentoria Tecnologia Takwara (Master)

> Repositório mestre de instruções. Consolida todo o conhecimento adquirido sobre o ecossistema de repositórios, regras, ferramentas e workflows. Serve como fonte única de verdade para todos os AGENTS.md dos repositórios irmãos.

---

## 1. Filosofia Central

> **"Tecnologia Social "grow" — do fundo de quintal, sem vínculo acadêmico formal, mas com rigor técnico e honestidade absoluta."**

### Princípios
- ✅ **Honestidade técnica** — nunca inflar TRL, nunca apresentar como aplicado o que é laboratorial
- ✅ **Atribuição correta** — cada autor com seu crédito. O que está em chat/áudio/e-mail é delegado ao agente e atribuído ao autor correspondente
- ✅ **Referências públicas** — só artigos com DOI e literatura pública como evidência. Documentos internos (LAB_, ENG_, RES_, SCI_, TAK_) nunca são citados como prova
- ✅ **Linguagem clara** — sem termos metafóricos internos ("biosoberano", "protocolos disso/daquilo") em textos públicos
### ❌ Nunca fabricar citações — usar paráfrase explícita quando não houver transcrição literal verificada
- ❌ **Nunca criar fichas científicas sem autor, DOI/ISBN/ISSN identificados** — documentos incompletos não entram no acervo
- ❌ **Nunca publicar fichas com seções vazias** — toda ficha deve ter 8 seções Cavichioli (2025) completas, com conteúdo extraído do PDF original
- ❌ **Sempre alertar o usuário** sobre dados faltantes antes de prosseguir com a criação de qualquer ficha

---

## 2. Mapa do Ecossistema

| Repositório | GH Pages | Conteúdo | Público |
|---|---|---|---|
| **Mentoria_Tecnologia_Takwara** | ✅ [takwaratec.github.io/Mentoria...](https://takwaratec.github.io/Mentoria_Tecnologia_Takwara/) | **← Master.** Metodologia, fichas técnicas, 7 módulos TEC, materiais didáticos. Campanha pública futura | Mentoria |
| **ECOSALA** | ✅ [takwaratec.github.io/ECOSALA](https://takwaratec.github.io/ECOSALA/) | Coletivo 12 membros — atas, projetos, editais, fichas | Grupo |
| **fundo-vaga-lumen-2026** | ❌ Só GitHub | Proposta FINEP Vaga Lúmen | FINEP |
| **plataforma-juventude-solidaria-2026** | ✅ [takwaratec.github.io/...](https://takwaratec.github.io/plataforma-juventude-solidaria-2026/) | MST Mário Lago, Viveiro-Educador | MST |
| **Analises-e-escrita-cientifica** | ✅ [takwaratec.github.io/...](https://takwaratec.github.io/Analises-e-escrita-cientifica/) | Acervo ~80 fichas, 7 eixos | Acadêmico |
| **Personagens-Bambu** | — | 8 personas bambu + biotipos | Geral |
| **Mulheres_Bioeconomia_Amazonia** | Zenodo DOI: 10.5281/zenodo.18827106 | Série Técnica, cartilhas | Zenodo |

> ⚠️ **Regra de ouro:** Cada repo tem seu próprio GH Pages (ou nenhum). NUNCA cruzar links entre repositórios. Links compartilhados com grupos não podem quebrar.

---

## 3. Mapa de Atribuições — Atores

| Ator | Papel | Tipo de contribuição |
|---|---|---|
| **Fabio Takwara** | Autodidata, tecnologias sociais | Inserções manuais de documentos (Chapada, Holambra, PU Vegetal, Série Técnica). Chat/áudio/e-mail → delegado ao agente |
| **André Blanco** | Arquiteto, diretor TEIA | TEIA - Tecnologia, Educação, Inovação e Ambiente Ltda. Labiapa = projeto de Gestão de APAs. Áudios WhatsApp |
| **Marcos Paron** | Dr. Microbiologia, prof. IFSP | Coordenação ECOSALA, ecoformação, articulação acadêmica |
| **Gisele Vilela** | Pesquisadora Embrapa | Documentos técnicos, articulação institucional |
| **Joaquim Sando** | Eng. Agrônomo, MST | Articulação territorial |
| **Vicente Borges** | Dr. Educação, prof. IFB | Bambu, MPTDF |
| **Daniela Maciel** | Drª Embrapa Territorial | Transferência de tecnologia, avaliação de impacto (reunião pendente) |
| **Murilo Miguel** | Coletivo Terra Viva | Operação de campo, viveiro |
| **Demais membros** | ECOSALA | Fichas pessoais |

---

## 4. Ferramentas de Trabalho

| Ferramenta | Função | Status | Como usar |
|---|---|---|---|
| **Pandoc** | DOCX/ODT → MD | ✅ | `pandoc arquivo.docx -t markdown -o arquivo.md` |
| **PyMuPDF** (fitz) | Extração de texto de PDFs | ✅ | Python `import fitz` |
| **python-docx** | Leitura/escrita DOCX | ✅ | Python `import docx` |
| **ffmpeg** (conda) | Conversão de áudio (opus → wav) | ✅ | `ffmpeg -i audio.opus audio.wav` |
| **faster-whisper** | Transcrição de áudio | ✅ | `conda run -n whisper_env python3` |
| **pdfplumber** | PDF tabular | ⏳ Pendente | `pip install pdfplumber` |

### Fluxo de processamento de áudio
```bash
# 1. Converter opus para wav
ffmpeg -i audio.opus -ar 16000 -ac 1 audio.wav -y

# 2. Transcrever com whisper
conda run -n whisper_env python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('base', device='cpu', compute_type='int8')
segments, _ = model.transcribe('audio.wav', language='pt')
for seg in segments: print(seg.text)
"
```

---

## 5. Regras para Propostas (FINEP e afins)

### O que NUNCA fazer
- ❌ NUNCA citar documentos internos (prefixos LAB_, ENG_, RES_, SCI_, TAK_) como evidência
- ❌ NUNCA usar termos "biosoberano" ou "protocolos disso/daquilo"
- ❌ NUNCA inflar TRL — tecnologia Takwara é proposta TRL laboratorial, nunca como aplicada em comunidades
- ❌ NUNCA fabricar citações de figuras públicas (cientistas, autores, entrevistados)

### O que SEMPRE fazer
- ✅ Só artigos públicos com DOI como base de evidência
- ✅ Referências em formato ABNT
- ✅ Tecnologia descrita pelo que faz, não por codificação interna
- ✅ Atribuir com honestidade
- ✅ Se não tem transcrição literal verificada, usar paráfrase explícita

---

## 6. Workflow Padrão

```bash
# 1. Sincronizar
git pull

# 2. Fazer alterações (converter documentos, editar, etc.)

# 3. Versionar
git add <arquivos>
git commit -m "tipo: descrição concisa"
git push

# 4. Publicar (se houver MkDocs)
mkdocs gh-deploy --clean
```

### Por tipo de material

| Material | Ação |
|---|---|
| **DOCX/ODT** | Converter com Pandoc → .md |
| **PDF (texto)** | Extrair com PyMuPDF → .md |
| **PDF (escaneado)** | Extrair imagens → salvar em `imagens/` |
| **Áudio .opus** | ffmpeg → wav → whisper → txt |
| **Imagens** | Analisar com visão computacional |

---

## 7. Estrutura de Diretórios (Mentoria_Tecnologia_Takwara)

```
📂 docs/
├── 00_METODOLOGIA/        ← Metodologia da mentoria
├── 01_TRIAGEM_BRUTA/      ← Material bruto de triagem
├── 02_BASE_DE_CONHECIMENTO/  ← 7 módulos TEC
│   ├── TEC_01_Ecologia.md
│   ├── TEC_02_Tratamentos_Boro.md
│   ├── TEC_03_Poliuretano_Vegetal.md
│   ├── TEC_04_Engenharia_Industrial.md
│   ├── TEC_05_Dossie_Comparativo.md
│   ├── TEC_06_Historico_Autoridade.md
│   └── TEC_07_Quimica_dos_Tratamentos.md
├── 03_JORNADA_7_PASSOS/   ← Jornada do mentorado
📂 _privado/               ← Documentos restritos
📂 raiz/                   ← Documentos consolidados
├── PU_Vegetal_Ficha_Tecnica_Consolidada.md
├── PU_Vegetal_Linha_de_Produtos.md
├── TAK_proposta_estrategica_imperveg.md
└── mapa-acervo-personagens.md
```

---

## 8. Personagens-Bambu (Conexão com a Mentoria)

| Personagem | Eixo | Repositório |
|---|---|---|
| **Sabia-mamona** | PU Vegetal, TEC_03, TEC_07 | Mentoria + Personagens-Bambu |
| **Bambusa** | Ecologia (TEC_01) | Personagens-Bambu |
| **Dr. Burocrata** | Histórico (TEC_06) | Personagens-Bambu |
| **Taboca** | Bioeconomia | Personagens-Bambu |
| **Vulgaris** | BD-BAMBU | Personagens-Bambu |
| **Cacique-Asper** | MQTF | Personagens-Bambu |
| **Tuldoides** | Comunidades | Personagens-Bambu |
| Dr. Motosserra | Crítica | Personagens-Bambu |

---

*AGENTS.md Master mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
*Consolida todo o aprendizado das sessões com Fabio Takwara — ECOSALA, Vaga Lúmen, MST, Acervo Científico*
