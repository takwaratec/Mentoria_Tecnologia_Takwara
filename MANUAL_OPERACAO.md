# Manual de Operação — Fabio Takwara + Hermes Agent

> Guia prático de como interagir com o Hermes Agent para extrair o máximo do ecossistema de repositórios.
> Versão: 1.0 — 26/06/2026

---

## 1. Como Pedir — Frases que Funcionam

### Processamento de Arquivos

| Pra dizer | Eu entendo e faço |
|---|---|
| "Decupa esse áudio" | Transcrevo com whisper, extraio informações, atualizo fichas |
| "Converte esse PDF" | Extraio texto com PyMuPDF, salvo como .md |
| "Converte esse DOCX" | Pando c para .md |
| "Extrai as imagens desse PDF" | PyMuPDF salva cada página como JPEG |
| "Faz a triagem desse material" | Leio, extraio o relevante, organizo em documento |
| "Busca produção acadêmica do/da [nome]" | Pesquiso online (Lattes, Google Scholar), crio ficha |

### Edital / Proposta

| Pra dizer | Eu entendo e faço |
|---|---|
| "Verifica esse edital" | Acesso o link, extraio regras, prazos, valores |
| "Cria ficha desse edital" | Estruturo: regulamento → formulário espelho → checklist |
| "Atualiza a proposta com [informação]" | Incorporo no texto existente, contextualizo |
| "Fecha o orçamento" | Calculo valores, sugiro complementos |

### Repositórios

| Pra dizer | Eu entendo e faço |
|---|---|
| "Atualiza o README do [repo]" | Reescrevo com novas informações |
| "Commita isso" | `git add` + `git commit` + `git push` |
| "Faz deploy do site" | `mkdocs gh-deploy --clean` |
| "Atualiza o AGENTS.md" | Reviso as instruções do agente praquele repo |

### Integração

| Pra dizer | Eu entendo e faço |
|---|---|
| "Cruza essas informações" | Relaciono dados entre repositórios |
| "O que falta no [repo]?" | Verifico pendências, checklist, fichas vazias |
| "Mensagem pro grupo sobre [assunto]" | Redijo texto pra WhatsApp |
| "Relatório de atualização" | Consolid o mudanças em documento |

---

## 2. Fluxo de Trabalho Padrão

```
VOCÊ                              HERMES
  │                                 │
  ├─ Manda arquivo (áudio/PDF/DOCX) │
  │  para TRIAGEM-BRUTA/            │
  │                                 ├── Leio e processo
  │                                 ├── Crio .md em docs/
  │                                 ├── Commit + push
  │                                 └── Aviso que terminou
  │                                 │
  ├─ Pede "busca produção do/da X"  │
  │                                 ├── Pesquiso online
  │                                 ├── Crio/atualizo ficha
  │                                 └── Commit + push
  │                                 │
  ├─ Pede "atualiza proposta"       │
  │                                 ├── Leio o documento
  │                                 ├── Incorporo mudanças
  │                                 └── Commit + push
  │                                 │
  ├─ Pede "msg pro grupo"           │
  │                                 └── Redijo e apresento
  │                                 │
  └─ Diz "pode enviar"              │
                                    └── (você copia e manda)
```

---

## 3. O Que Faço Automático vs. O Que Peço Autorização

### ✅ Faço automático (sem perguntar)
- Processar arquivos em TRIAGEM-BRUTA
- Criar/atualizar fichas técnicas
- Commitar arquivos .md processados
- Pesquisar online
- Redigir documentos, relatórios, mensagens
- Atualizar AGENTS.md com regras aprendidas

### ⚠️ Peço autorização ou aviso
- `git commit` com `rm -rf` ou destructive commands
- Alterar arquivos que você acabou de mencionar como pessoais
- Links compartilhados com grupos (confirmo qual repo)
- Mensagens para o grupo (você revisa antes)

### ❌ Nunca faço
- Fabricar citações de figuras públicas
- Inflar TRL em propostas
- Usar "biosoberano" ou termos metafóricos internos em textos públicos
- Citar documentos LAB_, ENG_, RES_, SCI_, TAK_ como evidência
- Atribuir autoria errada (cada documento ao seu autor)
- Mexer em links compartilhados sem confirmar

---

## 4. Ferramentas Disponíveis

| Ferramenta | Uso | Comando (se aplicável) |
|---|---|---|
| **Pandoc** | DOCX/ODT → MD | `pandoc arquivo.docx -t markdown -o arquivo.md` |
| **PyMuPDF** (fitz) | Extrair texto de PDFs | `import fitz` (Python) |
| **python-docx** | Ler/escrever DOCX | `import docx` (Python) |
| **ffmpeg** | Áudio opus → wav | `ffmpeg -i audio.opus -ar 16000 -ac 1 audio.wav` |
| **faster-whisper** | Transcrição de áudio | `model.transcribe('audio.wav', language='pt')` |
| **MkDocs** | Site GH Pages | `mkdocs gh-deploy --clean` |
| **Git** | Versionamento | `git add/commit/push` |
| **delegate_task** | Tarefas paralelas | Útil para processar múltiplos arquivos |

---

## 5. Mapa dos Repositórios

| Repo | GH Pages | Pra que uso |
|---|---|---|
| **Mentoria_Tecnologia_Takwara** | ✅ | Master. Metodologia, campanha pública, manual |
| **ECOSALA** | ✅ | Grupo 12 membros, atas, editais |
| **fundo-vaga-lumen-2026** | ❌ Só GitHub | Proposta FINEP |
| **plataforma-juventude-solidaria-2026** | ✅ | MST Mário Lago |
| **Analises-e-escrita-cientifica** | ✅ | Acervo científico ~80 fichas |
| **Personagens-Bambu** | — | 8 personas |
| **Mulheres_Bioeconomia_Amazonia** | Zenodo | Série Técnica, cartilhas |

---

## 6. Comandos Rápidos (Slash)

Durante a conversa, posso usar comandos internos:

| Comando | Efeito |
|---|---|
| `/model` | Troca modelo/provider |
| `/compress` | Comprime contexto (quando a conversa fica longa) |
| `/new` | Começa sessão nova |
| `/todos` | Mostra lista de tarefas |
| `mkdocs gh-deploy --clean` | Publica site após alterações |

---

## 8. Dicas do Ravi — O que Podemos Aplicar no Fluxo

Das ~40 recomendações pendentes, estas são aplicáveis agora no nosso ecossistema:

### 🔥 Alta Prioridade (fácil de implementar, alto retorno)

| Dica | Como aplicar no fluxo | Esforço |
|---|---|---|
| **Bases vetoriais locais** | Já temos PyMuPDF + python-docx. Posso criar um script que transforma nossos .md em buscas semânticas com embeddings locais (sem Pinecone). Tipo um "Google particular" dos repositórios | Médio |
| **Engenharia reversa de prompts** | Me manda uma imagem de referência que eu extraio o prompt usado para gerar. Aprendemos a estrutura e replicamos | Baixo |
| **Design.md Directory** | Escolhe um template visual no https://designdotmd.directory/ que eu aplico no tema MkDocs de qualquer repositório | Baixo |
| **Open Memory** | O Hermes já tem memória permanente (o que salvamos com `memory`). Posso criar uma ficha de memória expandida para cada repositório | Baixo |

### 🟡 Média Prioridade (precisa de setup)

| Dica | Como aplicar | Setup necessário |
|---|---|---|
| **n8n** | Automação visual de workflows (ex: ao receber áudio no Telegram → transcrever → salvar → notificar). R$ 20/mês self-hosted | Instalação via Docker |
| **OpenRouter.ai** | Acesso a GPT-4-oss, Claude, etc. por centavos. Útil para tarefas pesadas | Criar conta + configurar chave |
| **Docling** | Alternativa ao PyMuPDF para PDFs complexos (tabelas, imagens). `pip install docling` | Testar |

### 🔵 Baixa Prioridade (úteis mas não urgentes)

| Dica | Pra que serve |
|---|---|
| **Lovable.dev** | Criar landing pages e sites com IA |
| **Feynman.is** | Ferramenta de estudo/aprendizado |
| **Cal.com** | Agenda online para reuniões do ECOSALA |
| **Google Workspace CLI** | Acessar Google Drive/Docs via terminal |

### ❌ Não aplicável por enquanto
- Peptídeos (questão médica), Starlink (infraestrutura física), Canva/Plannotator (design especializado)

---

## 9. Telegram Bot — @takwara_bot

O bot já está **configurado e rodando** no gateway do Hermes. Você pode interagir com ele pelo Telegram.

### Como usar

1. Abra o Telegram e busque **@takwara_bot**
2. Inicie a conversa com `/start`
3. Mande mensagens de texto, áudio, documentos ou imagens
4. O bot responde com o processamento do Hermes

### O que funciona pelo bot

| Tipo | O que acontece |
|---|---|
| **Texto** | O Hermes lê e responde normalmente |
| **Áudio** | O gateway transcreve automaticamente (faster-whisper) e processa |
| **Documentos** (PDF, DOCX) | Extraio o conteúdo e respondo |
| **Imagens** | Analiso com visão computacional |
| **Comandos** | `/model`, `/new`, `/help` funcionam pelo bot também |

### Importante

- O bot usa o **mesmo Hermes** da sessão CLI — mesmo contexto, mesmas regras
- Áudios enviados pelo Telegram já chegam transcritos (não preciso processar manualmente)
- Para tarefas longas, posso pedir confirmação antes de executar

### Comandos úteis no Telegram

| Comando | Efeito |
|---|---|
| `/start` | Inicia conversa |
| `/help` | Lista comandos disponíveis |
| `/new` | Reseta a sessão |
| `/model` | Troca modelo |
| `/sethome` | Define este chat como canal principal |

---

## 8. Dicas para Máximo Aproveitamento

1. **Uma tarefa por mensagem** — processar áudio + buscar + atualizar = tudo certo, mas rende mais se for passo a passo
2. **Contexto é rei** — quanto mais informação der no pedido, mais preciso sou
3. **Confirme os links** — antes de compartilhar com grupos, aviso se o link está certo (já errei uma vez e aprendi)
4. **Revisão prévia** — toda mensagem pro grupo passa por você antes
5. **Pendências** — se algo ficou pra depois, me cobra que eu continuo de onde parei

---

*Manual mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
