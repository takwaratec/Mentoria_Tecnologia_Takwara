# TRIAGEM DE DICAS DE TECNOLOGIA — RAVI → FABIO

Fonte: Conversa do WhatsApp (08/07/2025 a 25/06/2026, 5209 linhas)
Arquivo: `01_TRIAGEM_BRUTA/Ravi/Conversa do WhatsApp com Ravi Resck.txt`
Data da extração: 26/06/2026

---

## SUMÁRIO

- [1. FERRAMENTAS IA](#1-ferramentas-ia)
- [2. PROGRAMAS E EXTENSÕES](#2-programas-e-extensoes)
- [3. INFRAESTRUTURA](#3-infraestrutura)
- [4. DICAS TÉCNICAS](#4-dicas-tecnicas)
- [5. CONTEÚDO RECOMENDADO](#5-conteudo-recomendado)
- [6. DICAS EXTRAS (NÃO-TEC)](#6-dicas-extras-nao-tec)
- [APÊNDICE: LINHAS DO TEMPO](#apendice-linhas-do-tempo)

---

## 1. FERRAMENTAS IA

### Perplexity Pro
- **O que Ravi recomendou:** Assinar o plano Pro da Perplexity. "O plano Pro tá mto maravilhoso, vc vai curtir." Usou pra fazer análises de carros (busca até em vídeos do YouTube).
- **Contexto (linhas 18, 39-48):** 08/07/2025 — Logo no início da conversa. Ravi tem o plano da Vivo que inclui Perplexity Pro.
- **Contexto (linha 450-462):** 21/07/2025 — Fabio diz que não consegue instalar a versão desktop pois só roda no macOS 15+ (ele tem Monterey 12).
- **Contexto (linhas 461, 478, 1145):** Ravi sugere usar Perplexity para diversas tarefas: perguntar sobre limitações do macOS, explicar bases vetoriais, etc. Perplexity Finance (25/08/2025).
- **Status: ⏳ PENDENTE** — Fabio menciona ter testado, mas o desktop app não roda no Mac dele. O celular/app web deve funcionar.

### Lovable.dev
- **O que Ravi recomendou:** IA que cria sites. Ele enviou o link https://lovable.dev/ depois de Fabio perguntar qual era o site de criação de sites.
- **Contexto (linhas 76-85):** 14/07/2025 — Fabio perguntou "como é mesmo o site de criação de sites?" e Ravi respondeu "esqueci de te passar o site".
- **Status: ⏳ PENDENTE** — Mencionado, mas não há evidência de Fabio ter usado ativamente.

### n8n
- **O que Ravi recomendou:** Ferramenta de automação low-code. "Ali da pra fazer tudo isso e mto mais." Falou que levaria as criações de Fabio para "outro nível de complexidade mto mais rápido".
- **Contexto (linhas 483-485, 504):** 21/07/2025 — Fabio estava fazendo processos manuais e Ravi disse que ele estava "num caminho mto old school".
- **Status: ⏳ PENDENTE** — Fabio disse que aprender algo do zero iria atrasá-lo. Ravi insistiu na linha 504 que já tem vídeos mostrando tudo passo a passo.

### Pinecone (bases vetoriais)
- **O que Ravi recomendou:** Usar Pinecone para base vetorial em vez de fazer manualmente. "Se tem pinecone pra isso e serviço de embedding?"
- **Contexto (linhas 472-478):** 21/07/2025 — Fabio estava extraindo tabelas de PDFs manualmente para criar BD para IA. Ravi questionou o método.
- **Status: ⏳ PENDENTE** — Fabio continuou com abordagem manual + agentes.

### Ada (OpenAI embeddings)
- **O que Ravi recomendou:** Usar o serviço de embedding da OpenAI (Ada) para criar base vetorial, integrado com Pinecone.
- **Contexto (linha 478):** 21/07/2025 — "Pede pro perplexity te explicar como fazer uma base vetorial no pinecone e usando o Ada da openai."
- **Status: ⏳ PENDENTE**

### NotebookLM (Google)
- **O que Ravi recomendou:** Geração de podcast com ~20 minutos. "Notebooklm, da Google."
- **Contexto (linha 2036-2038):** 15/11/2025 — Fabio perguntou qual era a ferramenta de geração de podcast.
- **Contexto (linhas 2832-2843, 3524-3525):** 18/02/2026 e 03/03/2026 — Fabio usando ativamente para gerar conteúdo.
- **Status: ✅ APLICADO** — Fabio usou extensivamente, gerou podcasts, imagens e relatórios.

### Antigravity (antigravity)
- **O que Ravi recomendou:** Plataforma de agente que roda no terminal. "Ferramenta mto foda."
- **Contexto (linhas 2829-2831, 2854-2855):** 14/02/2026 — Ravi menciona "Antigravity, Gemini CLI, pesquisar sobre skills com IA".
- **Contexto (linhas 2852-2859, 2930-2957, 3115-3116, 3771-3773, 3882):** Uso intenso em fevereiro-março de 2026.
- **Contexto (linhas 4573-4615):** 06/06/2026 — Antigravity mudou a interface e ficou ruim. Ravi migrou para outras ferramentas.
- **Status: ✅ APLICADO** — Fabio usou intensamente por meses. Depois migrou para Hermes.

### Gemini CLI
- **O que Ravi recomendou:** Agente de codificação no terminal. "Mesma coisa que um agente de codificação altamente eficaz. Mais rápido. Créditos adicionais do PRO."
- **Contexto (linhas 2830, 3058-3063, 3879, 3895-3928):** 14/02/2026 a 12/03/2026 — Ravi insistiu para Fabio instalar e usar. Deu instruções detalhadas de instalação via brew.
- **Contexto (linha 4240):** 25/03/2026 — Fabio: "GEMINI CLI Rodando!!! Outro nível agora."
- **Status: ✅ APLICADO** — Fabio instalou e rodou com sucesso.

### Hermes Agent
- **O que Ravi recomendou:** Novo agente autônomo. "Ele é o mais próximo q tem de um agente autonomo mesmo. Cria skills automaticamente, lembra das coisas."
- **Contexto (linhas 4573-4615):** 06/06/2026 — Ravi explica que parou de usar Antigravity e agora usa Hermes Agent. Dá instrução de instalação: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
- **Contexto (linhas 4622-4738, 4779, 4783-4797):** Fabio instala, Ravi cria um guia (https://guiahermes.vercel.app/).
- **Status: ✅ APLICADO** — Fabio instalou e está usando (ainda em transição do Antigravity). Gastou créditos rapidamente.

### Opencode Go
- **O que Ravi recomendou:** Plano de API com modelos open source. "10 usd mensais."
- **Contexto (linhas 4580-4588, 4732-4753):** 06/06/2026 — Ravi recomenda assinar em opencode.ai e usar no Hermes.
- **Contexto (linha 4771-4773):** Ravi envia link com ref: https://opencode.ai/go?ref=TGXZ6E2GJ7
- **Status: ✅ APLICADO** — Fabio assinou e configurou no Hermes (linha 4874).

### Deepseek V4 Flash
- **O que Ravi recomendou:** Modelo chinês "bem fodão e muuuuito barato". Usar via Opencode Go no Hermes.
- **Contexto (linhas 4597-4598):** 06/06/2026
- **Contexto (linha 4849):** 08/06/2026 — Ravi: "seleciona deepseek v4 flash como modelo"
- **Status: ✅ APLICADO** — Fabio configurou no Hermes como modelo principal.

### OpenAI (ChatGPT) — Plano Pago
- **O que Ravi recomendou:** "Plano pago da open ai de 20usd. Os modelos da open ai voltaram a ficar mto bons."
- **Contexto (linha 4594-4595):** 06/06/2026
- **Status: ⏳ PENDENTE** — Ravi usa, mas não há confirmação de Fabio ter assinado.

### Google AI Studio (aistudio.google.com)
- **O que Ravi recomendou:** "Geração de imagens é dentro do gemini.google.com, não é no notebooklm." Também recomendou o AI Studio para geração e testes de imagem.
- **Contexto (linhas 2862, 3018-3020, 3886-3895):** 18/02/2026 e 12/03/2026
- **Contexto (linhas 3887-3888):** Google Labs Flow: https://labs.google/fx/tools/flow
- **Status: ⏳ PENDENTE** — Fabio disse que nunca conseguiu os mesmos resultados do Antigravity lá.

### Google AI Pro (assinatura)
- **O que Ravi recomendou:** "Vc ja assina um pacote da google ai pro q tem absolutamente tudo. Cê só não tá usando direito."
- **Contexto (linha 3021-3023, 3526-3531):** 03/03/2026 — Fabio estava usando versão gratuita com cotas limitadas.
- **Contexto (linha 4593):** 06/06/2026 — Ravi diz que cancelou o plano Google e paga só espaço no Drive.
- **Status: ⏳ PENDENTE** — Fabio nunca ativou o Pro de fato, depois Ravi mesmo cancelou o dele.

### Qwen Coder
- **O que Ravi recomendou:** Modelo chinês, alternativa ao Gemini CLI/Antigravity.
- **Contexto (linha 4184):** 23/03/2026 — "qwen coder (te falei desse né?)"
- **Status: ⏳ PENDENTE**

### OpenRouter.ai
- **O que Ravi recomendou:** Usar API do OpenRouter para acessar GPT-4-oss-120b e outros modelos de forma barata.
- **Contexto (linhas 4049-4053):** 17/03/2026 — Ravi: "Pega a api no openrouter.ai. Vc não vai pagar nem 3 reais usando esse cara aqui."
- **Status: ⏳ PENDENTE**

### Google Workspace CLI
- **O que Ravi recomendou:** Ferramenta para agentes acessarem Google Workspace diretamente. https://github.com/googleworkspace/cli
- **Contexto (linha 3522):** 03/03/2026
- **Status: ⏳ PENDENTE**

### Agent Browser (skills.sh)
- **O que Ravi recomendou:** Skill para navegador que permite agente acessar websites, clicar em coisas, preencher formulários. https://skills.sh/vercel-labs/agent-browser/agent-browser
- **Contexto (linhas 3515-3523):** 03/03/2026 — Ravi: "consegui fazer a automação de emissao da nf com essa skill."
- **Status: ⏳ PENDENTE**

### Feynman.is
- **O que Ravi recomendou:** Projeto interessante. https://www.feynman.is/
- **Contexto (linha 4256):** 27/03/2026
- **Status: ⏳ PENDENTE**

### Gemini-2.5-flash-lite (modelo econômico)
- **O que Ravi recomendou:** Usar este modelo porque é o mais barato para processamento em lote.
- **Contexto (linhas 4046-4048):** 17/03/2026
- **Status: ⏳ PENDENTE**

---

## 2. PROGRAMAS E EXTENSÕES

### VS Code
- **O que Ravi recomendou:** Usar o VS Code com terminal integrado para programar.
- **Contexto (linha 459):** 21/07/2025 — Fabio: "eu tô usando o VSCode, tudo no terminal"
- **Status: ✅ APLICADO** — Fabio usa desde o início.

### Obsidian
- **O que Ravi recomendou:** Apenas mencionado como ferramenta que Fabio já usava.
- **Contexto (linhas 486, 3109):** 21/07/2025 e 05/03/2026 — Fabio: "ela já indexou todos os meus artigos e todo o vault obsidian"
- **Status: ✅ APLICADO** — Fabio já usava e integrou com agentes.

### Firebase / Google Cloud
- **O que Ravi recomendou:** "tem mtas formas diferentes de vc usar um terminal e maquinas virtuais na nuvem. Esse q eu mandei aí é uma mistura de lovable + vs code da google."
- **Contexto (linhas 499-503, 506):** 21/07/2025 — Enviou link do Firebase (https://firebase.google.com/) e mencionou Cloud Shell.
- **Status: ⏳ PENDENTE** — Fabio olhou, nunca implementou de fato.

### GitHub Pages
- **O que Ravi recomendou:** Usar GitHub Pages para publicar sites simples.
- **Contexto (linha 4161-4163):** 23/03/2026 — Fabio: "vou usar o mkdocs do ghpage enquanto isso"
- **Status: ✅ APLICADO** — Fabio publica vários sites no ghpages (takwaratec.github.io).

### Netlify
- **O que Ravi recomendou:** "Faz no netlify, ele vai te guiar a fazer isso. Netlify + github."
- **Contexto (linhas 2934, 3304, 3642, 4166-4187):** 24/02/2026 a 23/03/2026 — Ravi explicou o fluxo completo: site no Antigravity → commit → Netlify automaticamente.
- **Contexto (linha 4141):** Fabio perguntou se valia pagar o Netlify; Ravi disse "nope, vai pro vercel".
- **Status: ✅ APLICADO** — Fabio publicou múltiplos sites no Netlify.

### Vercel
- **O que Ravi recomendou:** "É um serviço igual" ao Netlify, gratuito.
- **Contexto (linhas 3305, 4143):** 09/03/2026 e 23/03/2026
- **Contexto (linha 4789):** 07/06/2026 — Ravi publicou o guia do Hermes no Vercel.
- **Status: ✅ APLICADO** — Fabio também publicou sites no Vercel.

### Warp (terminal)
- **O que Ravi recomendou:** Terminal moderno com IA embutida. "Baixa esse aqui https://www.warp.dev/"
- **Contexto (linhas 4635-4665):** 06/06/2026 — Ravi: "terminal moderno, bonitão. Tem IA embutida nele."
- **Contexto (linhas 4825-4826):** Fabio baixou e depois usou junto com Hermes.
- **Status: ✅ APLICADO** — Fabio instalou e usa.

### Canva
- **O que Ravi recomendou:** Abrir no Canva para editar textos e remover marca d'água com IA.
- **Contexto (linha 2844-2845):** 18/02/2026
- **Status: ⏳ PENDENTE** — Não há confirmação de uso.

### Docling
- **O que Ravi recomendou:** Alternativa para processamento de documentos. https://github.com/docling-project/docling
- **Contexto (linha 4061):** 17/03/2026
- **Status: ⏳ PENDENTE**

### Docmd
- **O que Ravi recomendou:** Gerador de wikis a partir de markdown. "Vem pronto, chama-se docmd. Facil de modificar."
- **Contexto (linhas 4968-4971):** 11/06/2026 — Ravi enviou https://docmd.io/
- **Status: ⏳ PENDENTE** — Fabio disse que ia testar.

### Plannotator
- **O que Ravi recomendou:** Leitor de planos que abre no navegador bonito para leitura e comentários. https://plannotator.ai/
- **Contexto (linhas 4973-4976, 5143-5147):** 11/06/2026 e 19/06/2026
- **Status: ⏳ PENDENTE**

### Open Design AI
- **O que Ravi recomendou:** Design system com IA. "Vai voltar aos seus tempos de diagramador no mundo da IA." https://open-design.ai/
- **Contexto (linha 5010-5011):** 12/06/2026
- **Status: ⏳ PENDENTE**

### Design.md Directory
- **O que Ravi recomendou:** Templates de design para consistência visual. https://designdotmd.directory/
- **Contexto (linhas 4998-5001, 5092):** 12/06/2026 e 19/06/2026 — Ravi: "escolhe um design q te agrada, copia o design.md e fala pro seu agente usar."
- **Status: ⏳ PENDENTE** — Fabio disse que ia usar.

### Zenodo
- **O que Ravi recomendou:** Registro de citação com DOI.
- **Contexto (linhas 2942-2943, 3113):** 24/02/2026 a 06/03/2026 — Fabio: "vou publicar e fazer o registro de citação no zenodo"
- **Status: ✅ APLICADO** — Fabio registrou a coleção com DOI (linha 3113).

### Cal.com
- **O que Ravi recomendou:** Agenda online. "Ou marcar aqui cal.com/rresck"
- **Contexto (linha 2824):** 13/02/2026
- **Status: ⏳ PENDENTE** — Fabio apenas recebeu o link, não usou o seu próprio.

---

## 3. INFRAESTRUTURA

### GitHub + Terminal (vs GitHub Desktop)
- **O que Ravi recomendou:** "Vc pode fazer qualquer coisa no Github pelo terminal. A versão desktop só é mais amigável."
- **Contexto (linhas 456-457):** 21/07/2025
- **Status: ✅ APLICADO** — Fabio usa terminal + git.

### Linux (alternativa ao macOS)
- **O que Ravi recomendou:** "Pq aí é melhor rodar um Linux. Se tá com tantas limitações" (referindo-se ao macOS Monterey 12 sem updates).
- **Contexto (linhas 462-464):** 21/07/2025
- **Status: ❌ NÃO APLICÁVEL** — Fabio manteve macOS e lidou com as limitações.

### Cloud / Nuvem (programar sem computador bom)
- **O que Ravi recomendou:** "Eu tenho amigos q programam de tudo sem ter um computador bom… eles fazem isso por opção, pq hj em dia vc faz tudo na nuvem."
- **Contexto (linha 502-503):** 21/07/2025
- **Status: ⏳ PENDENTE**

### Nubank PJ
- **O que Ravi recomendou:** "O nubank tá imbatível nas facilidades. O app deles é de longe o melhor, até pra gerir portfolio de investimentos." Ravi passou a usar Nubank PJ, convidou Fabio para acesso compartilhado.
- **Contexto (linhas 1268-1269, 2303-2323):** 01/09/2025 e 01/12/2025 — Ravi: "vou matar o Sicoob aos poucos."
- **Contexto (linha 2656):** 03/02/2026 — Ravi: "ir abandonando o Sicoob aos poucos."
- **Status: ✅ APLICADO** — Fabio tem acesso ao Nubank PJ.

### Sicoob (insatisfação e abandono)
- **O que Ravi recomendou:** Abandonar o Sicoob progressivamente. "Mto ruim esse serviço da fran e esse app."
- **Contexto (linhas 1265-1268, 2304-2311, 2653-2657):** Setembro de 2025 a fevereiro de 2026
- **Contexto (linhas 4543-4544):** 19/05/2026 — Ravi: "tamo pouco a pouco torrando a grana q ta la, nao vou mais receber nada por la tbm"
- **Status: ✅ APLICADO** — Em processo de encerramento.

### Starlink / Internet no sítio
- **O que Ravi recomendou:** "Vamos ter q instalar starlink?" Questionou planos de consumo, antenas 4G/5G.
- **Contexto (linhas 4206-4225, 5025-5045):** 23/03/2026 e 12/06/2026 — Discutiram opções: Starlink (R$249/mês + R$5k equipamento), CPE 4G (Aquário CA-42SX4G), antena externa.
- **Status: ⏳ PENDENTE** — Fabio contratou mais 100GB de dados móveis. Ainda sem solução definitiva.

### Transferência Digital de Veículo (Detran SP)
- **O que Ravi recomendou:** Usar o sistema digital do Detran SP para transferência de veículo.
- **Contexto (linhas 1173-1189, 1243, 1281-1288):** 27/08/2025 a 02/09/2025 — Fabio pesquisou e iniciou o processo digital.
- **Status: ✅ APLICADO** — Fizeram a solicitação digital. Teve problemas com prazos de vistoria, mas o sistema foi usado.

### GovBR (selo prata/ouro)
- **O que Ravi recomendou:** Necessário para assinar documentos digitais e transferência de veículo.
- **Contexto (linha 1186, 1200-1205, 1232-1235, 1484):** Múltiplas ocasiões — Fabio constantemente pedia códigos de acesso do GovBR ao Ravi.
- **Status: ✅ APLICADO** — Usado extensivamente.

### Youse (seguro auto)
- **O que Ravi recomendou:** "Meu amigo recomendou a youse." Seguro online, mensal, sem fidelidade, tudo pelo app.
- **Contexto (linhas 629-690):** 23/07/2025
- **Status: ✅ APLICADO** — Ravi contratou para o carro dele.

---

## 4. DICAS TÉCNICAS

### Bases vetoriais com Pinecone + Ada
- **O que Ravi recomendou:** Usar Pinecone (base vetorial) + Ada (OpenAI embeddings) em vez de fazer manualmente.
- **Contexto (linhas 472-478):** 21/07/2025
- **Status: ⏳ PENDENTE** — Fabio continuou com abordagem de agentes + scripts Python.

### Prompt Injection (segurança)
- **O que Ravi recomendou:** Alertou sobre o risco de prompt injection. "Eles nao tão prontos pra isso. Não existe segurança contra prompt injection no momento."
- **Contexto (linhas 3569-3583):** 03/03/2026 — Agente de Fabio disparou e-mail sem autorização para uma editora.
- **Status: ✅ APLICADO** — Fabio foi alertado e está ciente.

### Cuidado com Agentes com acesso a e-mail
- **O que Ravi recomendou:** "Desliga ae os acessos a email. Tem q tomar mto cuidado qdo vc tiver brincando com coisas q dao acesso ao mundo externo e dados sensíveis."
- **Contexto (linhas 3568-3583):** 03/03/2026
- **Contexto (linhas 3578-3580):** "por exemplo, vc pode dar acesso a um email criado só pra isso."
- **Status: ✅ APLICADO**

### Efeito Dunning-Kruger
- **O que Ravi recomendou:** "Meu maior medo com essa tecnologia o tempo todo é o conhecido efeito dunning-kruger." Alertou Fabio sobre o excesso de confiança com IA.
- **Contexto (linhas 3193, 3205-3221, 3240-3256):** 08/03/2026 — Fabio se autodenominou "pós-doutor informal em IH/IA" e Ravi criticou duramente.
- **Status: ✅ APLICADO** — Fabio ouviu e removeu/excluiu o conteúdo.

### Estratégia de persona e posicionamento
- **O que Ravi recomendou:** "Fica ligado na construção da sua persona externa. Deixa baixo esse papo de IA. O que tem q estar em foco é o produto final, não o processo e a ferramenta."
- **Contexto (linhas 3212-3221, 3235-3238, 3243-3256):** 08/03/2026 — Discussão intensa sobre visibilidade do uso de IA.
- **Status: ✅ APLICADO** — Fabio ajustou o discurso.

### Débito Técnico (testar um por um)
- **O que Ravi recomendou:** "No mundo dev tem um termo pra isso: débito técnico. A gente vai acumulando esse débito pq vai ficando com preguiça de manter algo q vai ficando enorme. Então é melhor vc sempre exaurir os testes de cada funcionalidade."
- **Contexto (linhas 3086-3098):** 05/03/2026
- **Status: ⏳ PENDENTE**

### Documentação em .md (criar docs/)
- **O que Ravi recomendou:** "Documenta, cria uma documentação do seu agente legível pra humanos em arquivos markdown numa pasta docs por exemplo."
- **Contexto (linha 3094):** 05/03/2026
- **Status: ✅ APLICADO** — Fabio adotou amplamente o formato .md para tudo.

### Engenharia reversa de prompts de imagem
- **O que Ravi recomendou:** "Vc pode pegar uma img dessa e tentar fazer uma engenharia reversa pra ele te dar o prompt q geraria essa img. Aí vc aprende a estrutura do prompt e consegue replicar."
- **Contexto (linha 3891-3892):** 12/03/2026
- **Status: ⏳ PENDENTE**

### Open Memory (cavira.app)
- **O que Ravi recomendou:** "Vc pode pedir pra ele te ajudar a configurar issaqui openmemory.cavira.app/. Ele vai criando memorias do agente e vc consegue recuperar coisas depois."
- **Contexto (linha 3902-3903):** 12/03/2026
- **Status: ⏳ PENDENTE**

### Geração de imagens
- **O que Ravi recomendou:** O melhor lugar para testar geração de imagens é o gemini.google.com. Também recomendou https://labs.google/fx/tools/flow
- **Contexto (linhas 3018-3020, 3885-3895):** 03/03/2026 e 12/03/2026
- **Status: ⏳ PENDENTE**

### Cartalax / BPC-157 / TB-500 (peptídeos)
- **O que Ravi recomendou:** Pesquisa sobre peptídeos para regeneração de disco (hérnia). Cartalax (bioregulador peptídico russo), BPC-157 e TB-500 para inflamação, Link-N para regeneração de disco.
- **Contexto (linhas 2721-2776, 2965-2972):** 10/02/2026 a 24/02/2026 — Ravi fez pesquisa profunda sobre o tema para a condição de Fabio.
- **Status: ⏳ PENDENTE** — Fabio se interessou, mas não conseguiu encontrar fornecedor no Brasil. Ravi disse "eu consigo os canais".

### Extração de cannabis para óleo
- **O que Ravi recomendou:** "Tem q fzr a extração logo pra nao estragar. Comer é mto mais eficaz, mto mais potente, dura mais. Apostando q vai reduzir sua ânsia de ficar fumando."
- **Contexto (linhas 2074-2085, 2375-2400):** 19/11/2025 e 05/12/2025
- **Status: ⏳ PENDENTE** — Fabio fez extração, mas ainda fumava.

### Metodologia Raízes / Curso Mare Educação
- **O que Ravi recomendou:** Alertou que poderia ser golpe de venda de curso. "Tá cheirando mto ruim... parece fórmula de lançamento do Enrico Rocha, uma das paradas mais desonestas no mercado digital."
- **Contexto (linhas 5085-5155):** 19/06/2026 — Fabio comprou curso Raízes (Mare Educação) por R$3.400. Ravi investigou e alertou.
- **Status: ⏳ PENDENTE** — Fabio disse que teve "resultados concretos" e criou ferramenta de diagnóstico.

### Automação de emissão de NF
- **O que Ravi recomendou:** Criou automação com script que controla browser para emitir notas fiscais automaticamente (agent-browser skill).
- **Contexto (linhas 2901-2902, 3515-3519, 3531-3533):** 23/02/2026 e 03/03/2026
- **Status: ✅ APLICADO** — Ravi usou para as NFs dele.

### Docling + PDFKit
- **O que Ravi recomendou:** "OCR morreu faz tempo. Hj é uma combinação de machine learning com LLM e OCR." Recomendou Docling e Fabio criou solução com PDFKit nativo do macOS.
- **Contexto (linhas 4003-4059, 4061):** 17/03/2026
- **Status: ✅ APLICADO** — Fabio criou script Python que extrai texto de +200 PDFs.

### API Fogo Cruzado
- **O que Ravi recomendou:** API pública de dados de conflitos armados. https://api.fogocruzado.org.br/
- **Contexto (linhas 2993-2994):** 01/03/2026
- **Status: ⏳ PENDENTE**

### Fator R e planejamento tributário
- **O que Ravi recomendou:** Várias discussões sobre alíquotas, pró-labore, INSS, IRPF. Ele questionou constantemente a contabilidade e buscou entender os números exatos.
- **Contexto (múltiplas linhas entre 1330-3493):** Setembro de 2025 a março de 2026
- **Status: ✅ APLICADO** — Implementaram a manobra do pró-labore para reduzir alíquota de 17% para ~10%.

---

## 5. CONTEÚDO RECOMENDADO

### Livros
| Recomendação | Contexto | Status |
|---|---|---|
| **"Tecnofeudalismo"** — Yanis Varoufakis | 08/07/2025 (linha 33) — Ravi comprou para Fabio de presente de aniversário. | ✅ APLICADO — Fabio leu e citou em discussões. |
| **"Humanure"** — Livro sobre compostagem | 13/03/2026 (linha 3997-4000) — Ravi: "veja la o que houve com as ideias do humanure, esse carinha era brabo" | ⏳ PENDENTE |

### Canais YouTube / Conteúdo
| Recomendação | Contexto | Status |
|---|---|---|
| **Jones Manoel** — Canal Farol Brasil (historiador comunista, críticas ao governo) | 21/07/2025 (linhas 440-449) — Ravi: "ele é o cara que melhor bate no governo atual que conheço" | ⏳ PENDENTE — Fabio disse que iria ver. |
| **Gilberto Maringoni** (economista comunista) no canal Farol Brasil | 21/07/2025 (linha 441) — Ravi enviou link do YouTube | ⏳ PENDENTE |
| **Entrevista do Lula na CNN** | 21/07/2025 (linhas 411-417) — Ravi: "foi sinistro cara" | ⏳ PENDENTE |
| **Documentário sobre dependência de opióides** | 15/11/2025 (linha 2015) — Fabio compartilhou, Ravi respondeu. | ✅ APLICADO |

### Editoras
| Recomendação | Contexto | Status |
|---|---|---|
| **Bambual Editora** | 09/03/2026 (linhas 3602-3604, 3617-3622) — "Essa aqui é bem fácil de conseguir parceria." | ⏳ PENDENTE — Fabio preparou email de contato. |
| **Boitempo, Ubu** | 09/03/2026 (linha 3601) — Editoras alinhadas politicamente | ⏳ PENDENTE |
| **Diálogo Freiriano** | 03/03/2026 (linha 3561-3562) — Agente de Fabio disparou contato automaticamente | ❌ Ravi alertou ser "caçador de leads" |

### Instituições / Parcerias
| Recomendação | Contexto | Status |
|---|---|---|
| **IPE — Instituto de Pesquisa** | 19/03/2026 (linhas 4071-4105) — Ravi firmou parceria, conseguiu contato de físico com +40 patentes para assessorar Fabio. | ✅ APLICADO — Ravi já firmou parceria, está atendendo o IPE. |

### Podcasts / Áudio
| Recomendação | Contexto | Status |
|---|---|---|
| **Geração de podcast com NotebookLM** | 15/11/2025 (linha 2036) — Ravi responde quando Fabio pergunta qual ferramenta de podcast. | ✅ APLICADO |

---

## 6. DICAS EXTRAS (NÃO-TEC)

### Gestão financeira / Impostos
- **Esvaziar Sicoob e migrar para Nubank PJ** (linhas 1265-1275, 2296-2323, 2653-2657, 4543-4544) — Ravi liderou essa migração.
- **Distribuição de lucros com isenção** (linhas 2272-2275, 2284-2311) — Planejamento para retirar grana da PJ antes do fim do ano.
- **Pró-labore e Fator R** (múltiplas linhas) — Constante monitoramento.

### Carro
- **Compra da EcoSport Titanium 2.0** — Ravi comprou, Fabio ajudou com a burocracia (consórcio, financiamento, Detran, seguro).
- **Dicas de direção** — "usa o modo manual em subida, a resposta é melhor" (linha 240-243)
- **Capa do estepe** para evitar roubo (linha 871-874)
- **Despachante** para transferência (linhas 1132-1135, 1885, 2614-2615, 2668-2673, 4554)

### Saúde
- **Ibogaína** para desmame de opióides (linha 1982-1984)
- **Bufo (sessão com Wilson Sapito)** (linhas 1991-1996, 2403)
- **Peptídeos** BPC-157, TB-500, Cartalax (linhas 2721-2776)
- **Cannabis** extração de óleo (linhas 2074-2085)
- **Osteopatia + sauna/gelo** — Ravi apoiou (linha 1900-1903)
- **Manta elétrica para cama** (linha 4532)

---

## APÊNDICE: LINHAS DO TEMPO

### Fase 1 — Julho a Novembro de 2025 (primeiros contatos)
- Perplexity Pro, Lovable.dev, n8n, Pinecone, Firebase
- Livro Tecnofeudalismo
- Compra do carro e burocracia (consórcio, seguro Youse, Detran)
- Canal Jones Manoel

### Fase 2 — Novembro de 2025 a Fevereiro de 2026 (adoção de IA)
- NotebookLM (✅)
- Antigravity + Gemini CLI (✅)
- Google AI Studio
- Peptídeos Cartalax/BPC-157
- Cannabis oil extraction

### Fase 3 — Fevereiro a Maio de 2026 (intensificação)
- Migração Nubank PJ (✅)
- Automação de NF (✅)
- Netlify + Vercel (✅)
- Repositório GitHub estruturado (✅)
- Projeto UnB Amazônia
- Parceria IPE (✅)

### Fase 4 — Junho de 2026 (migração)
- Hermes Agent + Opencode Go + Deepseek V4 (✅)
- Warp terminal (✅)
- Docmd, Plannotator, Design.md
- Curso Raízes (Mare Educação)

---

## RESUMO ESTATÍSTICO

| Status | Quantidade |
|---|---|
| ✅ APLICADO | ~30 itens |
| ⏳ PENDENTE | ~40 itens |
| ❌ NÃO APLICÁVEL | 1 item (Linux) |

**Total de dicas extraídas: ~70**
