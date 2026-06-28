# Plano — Frente 09: UnB / MQTF / Amazônia+10

> Proposta de criação do repositório e estrutura para a parceria UnB (Profa Tania),
> edital Desafios da Amazônia (Amazônia+10 / CONFAP / BNDES / Fundo Amazônia)
> Versão: Plano preliminar para aprovação — 28/06/2026

---

## 1. Dados do Edital (Confirmados na Fonte Oficial)

| Campo | Valor |
|---|---|
| **Programa** | 1ª Chamada do Programa Desafios da Amazônia |
| **Realização** | CONFAP + BNDES + Fundo Amazônia + FAPs |
| **Valor total** | R$ 107,1 milhões (R$ 72M Fundo Amazônia + R$ 35,1M contrapartida FAPs) |
| **Valor por projeto** | R$ 6M a R$ 10M (R$ 6-8M Fundo + contrapartida FAP) |
| **Cadeias** | Açaí, Castanha, Cacau, Babaçu, Pesca |
| **Pré-proposta** | Até **01/09/2026** (submissão via SIGCONFAP) |
| **Proposta final** | Até 08/12/2026 |
| **Site oficial** | https://www.amazoniamaisdez.org.br/chamadas-abertas |
| **Sistema** | https://sig.confap.org.br/ |
| **Contato** | desafios@amazoniamaisdez.org |

### Elegibilidade (resumo)

A Rede de Pesquisa e Inovação deve ter:
1. **ICT Executora** — sediada na Amazônia Legal, pública ou privada sem fins lucrativos
2. **ICT Co-Executora** — sediada na Amazônia Legal, EM ESTADO DIFERENTE da Executora
3. **OSP (Organização Socioprodutiva)** — cooperativa ou associação, 2+ anos, sediada na Amazônia Legal

### ⚠️ Ponto de Atenção

O edital exige **mínimo de R$ 6M** por projeto (R$ 6-8M Fundo Amazônia + contrapartida FAPs).
Você mencionou **R$ 3M seguindo linha MQTF** — isso pode ser:
  (a) Um recorte menor de uma proposta maior em consórcio
  (b) Outro edital/distribuição via FAP específica
  (c) Uma conversa preliminar ainda não calibrada com o valor do edital

**Sugiro esclarecermos esse ponto antes de estruturar o orçamento.**

---

## 2. Estrutura Proposta do Repositório

### Nome sugerido

```
takwaratec/unb-desafios-amazonia-takwara
```

### Público-alvo

- **Avaliadores do edital** — linguagem formal, impessoal, submission-ready
- **Profa Tania e equipe UnB** — documentos técnicos compartilháveis
- **Parceiros da Rede** — ICTs e OSPs co-executoras

### Estrutura de diretórios

```
unb-desafios-amazonia-takwara/
├── AGENTS.md              # Instruções para o Hermes
├── README.md              # Didático para o grupo
├── .gitignore             # TRIAGEM-BRUTA/ e site/
│
├── TRIAGEM-BRUTA/         # Material bruto (NÃO versionado)
│   ├── 01_REUNIOES/       # Áudios, transcrições, atas
│   ├── 02_DOCUMENTOS/     # PDFs, DOCX, planilhas dos parceiros
│   ├── 03_REGULAMENTOS/   # Edital baixado + anexos
│   └── 04_REFERENCIAS/    # Artigos, notas técnicas
│
├── docs/                  # Documentos processados (versionados)
│   ├── index.md           # Homepage do projeto
│   ├── edital/            # Ficha completa do edital
│   │   ├── regulamento.md         # Edital transcrito
│   │   ├── formulario-espelho.md  # Campos do SIGCONFAP
│   │   └── anexos.md              # Anexos I a IV
│   ├── proposta/          # Rascunho da proposta
│   │   ├── resumo-executivo.md
│   │   ├── justificativa.md
│   │   ├── metodologia.md
│   │   ├── orcamento.md
│   │   └── cronograma.md
│   ├── rede/              # Membros da Rede
│   │   ├── ict-executora.md
│   │   ├── ict-co-executora.md
│   │   └── osp.md
│   └── anexos-obrigatorios/
│       ├── carta-icts.md
│       ├── carta-territorios.md
│       └── declaracao-ambiental.md
│
└── mkdocs.yml             # GH Pages (se desejado)
```

---

## 3. Enquadramento no Edital — Desafios Possíveis

O Anexo I (Notas Técnicas dos Desafios) detalha os gargalos de cada cadeia.
Para posicionar a Tecnologia Takwara, as cadeias mais promissoras são:

| Cadeia | Sinergia com Takwara | Observação |
|---|---|---|
| **Açaí** | Bambu + PU para beneficiamento, estruturas, transporte | Resíduos de açaí podem virar biocompósitos |
| **Castanha** | Equipamentos de beneficiamento em bambu, secadores | Forno ecológico MPTDF aplicável |
| **Cacau** | Secagem, fermentação, estruturas de viveiro | Bambu como substituto de madeira nativa |
| **Babaçu** | Extração do óleo, quebra do coco, resíduos | Tecnologia de prensagem + PU vegetal |
| **Pesca** | Barcos/catamarãs de bambu+PU, caixas isotérmicas | Protótipo de embarcação vegetal |

> **Nota:** A escolha da cadeia depende da Profa Tania e da OSP parceira. Este plano prepara o terreno para qualquer uma delas.

---

## 4. O que Fabio Faz / O que Hermes Faz

| Etapa | Fabio | Hermes |
|---|---|---|
| **1. Aprovar este plano** | ✅ Ler e autorizar | — |
| **2. Criar repositório** | — | ✅ `gh repo create` + estrutura |
| **3. Baixar edital** | Compartilhar PDF/link | ✅ Extrair texto com PyMuPDF |
| **4. Mapear Profa Tania** | Compartilhar contato/contexto | ✅ Criar ficha da parceria |
| **5. Identificar OSP parceira** | Indicar OSP na Amazônia Legal | ✅ Pesquisar OSPs elegíveis |
| **6. Identificar ICT Co-Executora** | Definir qual ICT em outro estado | ✅ Mapear possibilidades |
| **7. Pré-proposta (Fase 1)** | Revisar e aprovar conteúdo | ✅ Redigir conforme edital |
| **8. Submissão SIGCONFAP** | Submeter (login próprio) | ✅ Preparar todos os campos |

---

## 5. Cronograma Sugerido

| Data | Marco |
|---|---|
| 28/06 | ✅ Plano apresentado |
| 01/07 | 🔄 Início submissões SIGCONFAP |
| ~05/07 | Criar repositório + estrutura |
| ~15/07 | Definir ICTs e OSP parceiras |
| ~30/07 | 1º rascunho da pré-proposta |
| ~15/08 | Revisão com Profa Tania |
| ~25/08 | Fechamento da pré-proposta |
| **01/09** | **⛔ PRAZO PRÉ-PROPOSTA** |
| 08/12 | Prazo proposta final (se aprovado) |

---

## 6. Próximos Passos (o que você precisa decidir)

- [ ] **1.** O valor de R$ 3M que você mencionou é para este edital (mínimo R$ 6M) ou outro?
- [ ] **2.** Qual cadeia produtiva faz mais sentido para a Profa Tania?
- [ ] **3.** Já existe OSP/ICT parceira em mente na Amazônia Legal?
- [ ] **4.** Posso criar o repositório com a estrutura acima?
- [ ] **5.** Tem áudios, mensagens ou documentos da Profa Tania para eu processar?

---

> Plano elaborado pelo Hermes Agent · Tecnologia Takwara · 28/06/2026
> Aguardando sua aprovação para executar a criação do repositório.
