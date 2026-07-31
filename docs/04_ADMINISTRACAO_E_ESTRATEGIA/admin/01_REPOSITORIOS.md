```yaml
# ADMIN/REPOSITORIOS.yaml
# Inventário central dos repositórios do ecossistema Tecnologia Takwara.
# Versão legível por automações.
# Fonte: PLANOS/INVENTARIO-ATIVOS-GITHUB-2026.md + FRENTES_DE_TRABALHO.md + auditoria local (30/07/2026)
# Regra: um documento, um repositório. NUNCA cruzar documentos entre repositórios.

repositorios:

  - nome: Mentoria_Tecnologia_Takwara
    classe: maestro
    descricao: "Repositório mestre de instruções. Regência do ecossistema, AGENTS.md, FRENTES_DE_TRABALHO.md, manual de operação, regras metodológicas."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara
    remoto: takwaratec/Mentoria_Tecnologia_Takwara
    frente: "Frente 1 — Mentoria (Maestro)"
    status: ativo
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/Mentoria_Tecnologia_Takwara/
    permite_automacao: administrativa
    exige_aprovacao_editorial: true
    acoes_proibidas:
      - receber_fichas_cientificas
      - receber_documentos_de_projeto

  - nome: acervo-soberania-tecnologica
    classe: referencia-cientifica
    descricao: "Fichas científicas (8 seções Cavichioli), resenhas, estados da arte, perfis documentais. Fonte única de referências para todas as frentes."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica
    remoto: takwaratec/acervo-soberania-tecnologica
    frente: "Frente 6 — Acervo Científico"
    status: ativo
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/acervo-soberania-tecnologica/
    permite_automacao: diagnostico
    exige_aprovacao_editorial: true
    ultima_verificacao: 2026-07-30
    observacoes: "8 alterações não commitadas. Site com dados de 24/07."

  - nome: ECOSALA
    classe: projeto
    descricao: "Coletivo de 12 pesquisadores. Atas, projetos, editais, fichas dos membros."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/ECOSALA
    remoto: takwaratec/ECOSALA
    frente: "Frente 2 — ECOSALA"
    status: em-reorganizacao
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/ECOSALA/
    permite_automacao: diagnostico
    acao_externa_bloqueada: true
    ultima_verificacao: 2026-07-30
    observacoes: "Editais suspensos. Grupo em reorganização. Nenhuma ação externa até alinhamento interno."

  - nome: fundo-vaga-lumen-2026
    classe: projeto
    descricao: "Documentos históricos da proposta FINEP Vaga Lúmen. Agora fusionado com ECOSALA."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/fundo-vaga-lumen-2026
    remoto: takwaratec/fundo-vaga-lumen-2026
    frente: "Frente 2 — ECOSALA (fusionado)"
    status: arquivado
    publicacao: nenhuma
    permite_automacao: diagnostico
    ultima_verificacao: 2026-07-30

  - nome: fabrica-modelo
    classe: projeto
    descricao: "Industrialização da construção civil com redução de impacto ambiental. Proposta FINEP Mais Inovação."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/fabrica-modelo
    remoto: takwaratec/fabrica-modelo
    frente: "Frente 4 — Fábrica Modelo"
    status: aguardando-patrocinadores
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/fabrica-modelo/
    permite_automacao: diagnostico
    ultima_verificacao: 2026-07-30
    observacoes: "Reunião com IPT realizada. Posicionamento de Fabio formalizado (29/07). Aguardando patrocinadores definirem escopo, orçamento e governança."

  - nome: plataforma-juventude-solidaria-2026
    classe: projeto
    descricao: "Repositório canônico de memória do Coletivo Terra Viva no Assentamento Mário Lago. 8 frentes: memória, viveiro, juventude, Zayed, app triagem."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/plataforma-juventude-solidaria-2026
    remoto: takwaratec/plataforma-juventude-solidaria-2026
    frente: "Frente 5 — MST Juventude Solidária"
    status: ativo
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/plataforma-juventude-solidaria-2026/
    permite_automacao: diagnostico
    exige_aprovacao_editorial: true
    ultima_verificacao: 2026-07-30

  - nome: ludmila-athis-df
    classe: projeto
    descricao: "Acompanhamento da parceria com Dra. Ludmila Correia (CAU-DF). Formação ATHIS 2026, Sol Nascente, Zayed."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/ludmila-athis-df
    remoto: takwaratec/ludmila-athis-df
    frente: "Frente 13 — Ludmila / ATHIS-DF"
    status: ativo
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/ludmila-athis-df/
    permite_automacao: diagnostico
    exige_aprovacao_editorial: true
    ultima_verificacao: 2026-07-30

  - nome: unb-desafios-amazonia-2026
    classe: projeto
    descricao: "Proposta Desafios da Amazônia (Amazônia+10). Carreira LaPCiS/UnB."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/unb-desafios-amazonia-2026
    remoto: takwaratec/unb-desafios-amazonia-2026
    frente: "Frente 10 — UnB / Desafios Amazônia"
    status: pre-proposta
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/unb-desafios-amazonia-2026/
    permite_automacao: diagnostico
    ultima_verificacao: 2026-07-30
    observacoes: "Refutação técnica encaminhada à Profa Tânia. Pré-proposta para 01/09."

  - nome: eco-prancha
    classe: projeto
    descricao: "Prancha de surf 100% vegetal. Marcello Pedro (Grupo Raízes) + Fabio Takwara."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/eco-prancha
    remoto: takwaratec/eco-prancha
    frente: "Frente 11 — Eco Prancha"
    status: aguardando-call
    publicacao: nenhuma
    permite_automacao: diagnostico
    ultima_verificacao: 2026-07-30

  - nome: Personagens-Bambu
    classe: divulgacao
    descricao: "8 personas bambu + biotipos. Material de divulgação e formação."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/Personagens-Bambu
    remoto: takwaratec/Personagens-Bambu
    frente: "Frente 7 — Personagens-Bambu"
    status: publicado
    publicacao: nenhuma
    permite_automacao: leitura
    ultima_verificacao: 2026-07-30

  - nome: Takwara-Tech
    classe: legado
    descricao: "Repositório histórico. NUNCA citar em documentos públicos."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/Takwara-Tech
    remoto: Resck/Takwara-Tech
    frente: "Frente 8 — Takwara-Tech (Legacy)"
    status: legado
    publicacao: github-pages
    url_publicacao: https://resck.github.io/Takwara-Tech/
    permite_automacao: leitura
    acoes_proibidas:
      - citar_em_documentos_publicos
    ultima_verificacao: 2026-07-30
    observacoes: "3 commits ahead do origin. 8 alterações não commitadas. Docs avulsos (COP30, Floresta_em_Pe)."

  - nome: Mulheres-Tecem-Amazonia_Clone
    classe: projeto
    descricao: "Clone local do MQTF. Cópia canônica do histórico Git. Latente."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/Mulheres-Tecem-Amazonia_Clone
    remoto: takwaratec/Mulheres-Tecem-Amazonia
    frente: "Frente 9 — Mulheres Bioeconomia Amazônia / MQTF"
    status: latente
    publicacao: github-pages
    url_publicacao: https://takwaratec.github.io/Mulheres-Tecem-Amazonia/
    permite_automacao: leitura
    ultima_verificacao: 2026-07-30
    observacoes: "MQTF é sigla de uso interno. Em docs públicos, referenciar como 'projeto de bioeconomia amazônica do consórcio UnB/UFAC/UFRR'."

  - nome: Mentoria_Comunidades_RaioX
    classe: coordenacao
    descricao: "Raio-X de comunidades. Auditoria de conteúdo e fronteira pendente."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/Mentoria_Comunidades_RaioX
    remoto: a_confirmar
    frente: "Nenhuma"
    status: a_auditar
    publicacao: desconhecida
    permite_automacao: leitura
    ultima_verificacao: desconhecida
    observacoes: "Listado no INVENTARIO-ATIVOS. Confirmar função e estado."

  - nome: takwara-mentoria-vercel
    classe: interface
    descricao: "Interface Vercel. Auditar publicação e dados."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/takwara-mentoria-vercel
    remoto: a_confirmar
    frente: "Nenhuma"
    status: a_auditar
    publicacao: vercel
    permite_automacao: leitura
    ultima_verificacao: desconhecida

  - nome: docmd-test-takwara
    classe: teste
    descricao: "Repositório de teste. Definir necessidade; depois arquivar ou restringir."
    caminho_local: /Users/fabiotakwara/Documents/GitHub/docmd-test-takwara
    remoto: a_confirmar
    frente: "Nenhuma"
    status: a_auditar
    publicacao: desconhecida
    permite_automacao: leitura
    ultima_verificacao: desconhecida

```
