# Relatório de Análise do Vault +TAKWARA TECH para LLM Wiki

**Data da análise:** 11 de junho de 2026
**Cutoff de idade:** arquivos com mais de 2 anos = modificados antes de junho/2024
**Total de arquivos:** 29 (sendo 4 vazios = 25 com conteúdo)

---

## RESUMO EXECUTIVO

- **28 arquivos (96%)** estao desatualizados (>2 anos, anteriores a jun/2024)
- **1 arquivo** (Sem título.md, jul/2024) tem menos de 2 anos — relativamente atual
- **4 arquivos** estao completamente vazios (0 bytes): +TAKWARA TECH.md, Análises da TTR.md, PATENTES.md, e possivelmente outros com frontmatter minimo
- **Conteúdo predominante**: tecnologia Takwara, tratamento de bambu com PU Vegetal e pirolenhoso, forno ecológico, habitações de interesse social (ATHIS), briquetes/tijolos ecológicos
- **Problema comum**: muitos arquivos foram gerados com auxílio de IA (AIPRM, ChatGPT) e contém HTML remnants, textos repetitivos e versões duplicadas do mesmo conteúdo
- **Prioridade máxima para ingestão**: PU + Papelão.md (cronograma 2023-2026), HIS e BRIQUETES STL.md (plano de negócios), e Sem título.md (conteúdo sobre ATHIS e gênero)

---

## 1. ARQUIVOS RAIZ (10)

### 1.1 +TAKWARA TECH.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-18 (>2,5 anos) |
| Tamanho | 0 bytes |
| Resumo | **ARQUIVO VAZIO** — apenas frontmatter/tags, sem conteúdo. |
| Prioridade LLM Wiki | Nenhuma |
| Ação sugerida | Excluir ou preencher com índice do vault |

### 1.2 Forno Ecológico.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-13 (>2,5 anos) |
| Tamanho | 23.2 KB |
| Resumo | Descreve o Forno Ecológico para tratamento de bambu, inspirado em Estufas Rocket (Estufa de Inércia Térmica). Detalha o processo com vapor de água + sal + pirolenhoso, duas câmaras independentes (cozimento a vapor e secagem), condensador de emissões, e o valor comercial do pirolenhoso. Cita alinhamento com ODS da ONU. **Gerado com AIPRM (SmartWriter)** — contém HTML cru e duas versões do mesmo texto (markdown + HTML). |
| Estado | Desatualizado | 
| Prioridade LLM Wiki | Média — informações técnicas sobre o forno sao relevantes, mas o texto precisa ser limpo de HTML e condensado |
| Ação sugerida | Extrair apenas a descrição técnica (linhas 54-88), remover HTML, atualizar com resultados práticos se houver |

### 1.3 HIS e BRIQUETES STL.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-10 (>2,5 anos) |
| Tamanho | 29.8 KB |
| Resumo | **Plano de negócios completo da Takwara Tech** em Sáo Tomé das Letras, MG. 3 pilares: (1) habitações de bambu sustentáveis, (2) briquetes de biomassa como energia limpa, (3) créditos de carbono. Inclui: análise de mercado global de briquetes (US$ 11,5 bilhoes até 2027), projeções financeiras (R$ 2M investimento, retorno em 5 anos), modelo Canvas, estudo de viabilidade para tijolos ecológicos de biomassa prensada com PU Vegetal, cadeia produtiva (artesanato -> painéis -> tijolos), políticas públicas aplicáveis (PRONAF, PNRS, RenovaBio, Proenergia). |
| Estado | Desatualizado — projeções financeiras e de mercado de 2023 |
| Prioridade LLM Wiki | **Alta** — conteudo denso e estruturado, espinha dorsal do modelo de negócios |
| Ação sugerida | Atualizar projeções financeiras e dados de mercado; remover redundâncias; incorporar ao Wiki como página "Modelo de Negócios" |

### 1.4 Normas para ensaios.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-11-06 (>2,3 anos) |
| Tamanho | 3.7 KB |
| Resumo | Roteiro técnico de ensaios para conexoes de bambu com cabo de aço (tração, flexao, cisalhamento, fadiga, torção) e para tecido resinado (traçao ASTM D5034, rasgamento ASTM D5587, fadiga ASTM E466). Inclui produçao de corpos de prova. |
| Estado | Parcialmente desatualizado — normas ASTM podem ter revisões |
| Prioridade LLM Wiki | Média — conteudo técnico objetivo, útil como referência |
| Ação sugerida | Verificar se as normas citadas ainda sao vigentes; incorporar ao Wiki como página "Protocolos de Ensaio" |

### 1.5 PU + Bambu.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-18 (>2,5 anos) |
| Tamanho | 7.0 KB |
| Resumo | **Artigo promocional** sobre a Tecnologia Takwara: combinaçao PU Vegetal + Bambu. Histórico desde 2012 (Fábio Takwara, artista autodidata). Aborda "solda vegetal", estruturas geodésicas, conexoes de aço. Inclui seçao sobre aplicaçao em Gestao Pública (resíduos sólidos, desenvolvimento econômico, preservaçao ambiental) e importancia da academia (UNB, IFB, CEFET MG). Cita Lei do Bambu 2011, PNRS, ODS. |
| Estado | Desatualizado — texto generalista, carece de dados técnicos atualizados |
| Prioridade LLM Wiki | Média — bom para contextualizaçao histórica, mas precisa de complemento técnico |
| Açao sugerida | Reescrever com foco técnico, adicionar resultados de pesquisa dos últimos 3 anos |

### 1.6 PU + Papelão.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-06-06 (>2,5 anos) |
| Tamanho | **45.7 KB (maior arquivo)** |
| Resumo | Projeto de habitaçao social com bambu + papelao + PU Vegetal, aprovado no **Edital 193/2022 da Nascente/CEFET MG**. Inclui: plano estratégico, cronograma 2023-2026 (com protótipo HIS até julho/2026), testes de resistência, parcerias, desafios. Contém **3 versões do cronograma** (formal, rebuscada e coloquial) — CONTEÚDO REPETITIVO. Descreve a cadeia primária (colheita/tratamento em STL) e secundária (acabamento em CRV). Protótipo domo geodésico. |
| Estado | Desatualizado MAS o cronograma original é referência histórica importante |
| Prioridade LLM Wiki | **Alta** — contém a linha do tempo do projeto mais relevante |
| Açao sugerida | **Prioridade máxima.** Extrair cronograma consolidado (tabela linhas 244-256), remover as 3 versões redundantes (ocupam ~100 linhas desnecessárias). Incorporar ao Wiki como página "Projeto PU + Papelão" |

### 1.7 Pirolenhoso + Bambu.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-13 (>2,5 anos) |
| Tamanho | 12.7 KB |
| Resumo | Proposta de pesquisa sobre uso de pirolenhoso no tratamento do bambu. Inclui: vantagens (resistência a xilófagos, fungos, intempéries), impactos socioambientais (manejo de espécies invasoras, economia circular), ensaios técnicos (absorçao de água, compressao, flexao, durabilidade, impacto), mapeamento de bambuzais abandonados no Sul de Minas, parcerias (UNB, IFB, CEFET). **Contém HTML remnants** e versao em inglês. Bibliografia com 4 referências. |
| Estado | Desatualizado — contém HTML, a pesquisa pode ter avançado |
| Prioridade LLM Wiki | Média-alta — abordagem ecológica relevante e ensaios bem descritos |
| Açao sugerida | Limpar HTML, atualizar com resultados de pesquisa, incorporar ao Wiki como página "Tratamento com Pirolenhoso" |

### 1.8 Sem título.md (NOME PROVISÓRIO)
| Campo | Valor |
|-------|-------|
| Modificação | **2024-07-18** (< 2 anos) |
| Tamanho | **45.3 KB** |
| Resumo | **Documento mais recente e um dos mais extensos.** Aborda ATHIS (Assistência Técnica para Habitaçao de Interesse Social) com perspectiva de gênero. Inclui: discussao sobre gêneros (binário, nao-binário, transgênero, queer etc.), dinâmicas educativas e jogos para conscientizaçao, design organizacional, importancia de infraestrutura de apoio, **cases de sucesso** (Mao ao Barro em Brazlândia/DF, Paraisópolis/SP, Banco Palmas/CE, Morro da Providência/RJ, Complexo do Alemão/RJ). Quadros de associaçao entre gêneros e estilos construtivos. |
| Estado | **Relativamente atual** — único arquivo com menos de 2 anos |
| Prioridade LLM Wiki | **Alta** — conteudo inovador que conecta ATHIS, gênero e sustentabilidade |
| Ação sugerida | Renomear (ex: "ATHIS e Gênero.md"), revisar formataçao, incorporar ao Wiki como página principal sobre ATHIS |

### 1.9 Tecido Resinado.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-09-12 (>2,5 anos) |
| Tamanho | 1.0 KB |
| Resumo | Lista de ensaios para tecido resinado: traçao, rasgamento, abrasao, flexao, intempéries, resistência química, aderência da resina, uniformidade de espessura. |
| Estado | Desatualizado — roteiro básico, sem normas técnicas específicas |
| Prioridade LLM Wiki | Baixa — conteúdo muito enxuto |
| Açao sugerida | Incorporar como subseçao de "Protocolos de Ensaio" (fundir com Normas para ensaios.md) |

### 1.10 Tijolos Briquetes.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-10 (>2,5 anos) |
| Tamanho | 30.9 KB |
| Resumo | **Estudo de viabilidade completo** para produçao de tijolos ecológicos de biomassa prensada com PU Vegetal. Inclui: análise de mercado, referências acadêmicas (Embrapa, UFLA, INT), projeções financeiras detalhadas (R$ 6M investimento inicial, R$ 400K faturamento mensal em briquetes, adaptaçao para tijolos por R$ 1,5M), capacidade produtiva (3.000 tijolos/dia, 480 residências/ano), Modelo Canvas completo. Aborda uso de resíduos de café, milho e mineraçao do Sul de Minas. Referências: ARAÚJO et al. 2021, SANTOS et al. 2019, VASCONCELOS et al. 2020. |
| Estado | Desatualizado — projeções financeiras de 2023 |
| Prioridade LLM Wiki | **Alta** — estudo de viabilidade mais completo e bem referenciado do vault |
| Ação sugerida | Atualizar projeções financeiras e dados de mercado; extrair modelo Canvas; incorporar ao Wiki como página "Estudo de Viabilidade - Tijolos Ecológicos" |

---

## 2. SUBPASTA ANÁLISES DA TTR (17)

Nota geral: sao análises multidisciplinares do projeto PU + Bambu, provavelmente geradas com IA (ChatGPT). Cada uma aborda uma perspectiva diferente. Todas de 2023 (>2 anos). Conteúdo genérico e opinativo, sem dados quantitativos originais.

### 2.1 Arquivos vazios ou índice
| Arquivo | Data | Tam | Observaçao |
|---------|------|-----|------------|
| Análises da TTR.md | 2024-04-12 | 0 B | **VAZIO** |
| Análises da Proposta.md | 2023-10-13 | 369 B | Apenas índice de links para as outras análises |

### 2.2 Análises temáticas (individuais)

| # | Arquivo | Data | Tam | Resumo | Prioridade Wiki |
|---|---------|------|-----|--------|-----------------|
| 1 | **Roteiro para testes.md** | 2023-10-13 | 2.3 KB | Ensaios para PU + Bambu: resistência mecânica, durabilidade, envelhecimento acelerado, aderência, certificaçoes ABNT NBR 15575 | Média |
| 2 | **Analise Ambiental.md** | 2023-05-28 | 2.3 KB | Sustentabilidade, gestao de resíduos, biodiversidade, educaçao ambiental | Baixa |
| 3 | **Analise BNDES.md** | 2023-09-12 | 2.7 KB | Enquadramento nas linhas de financiamento do BNDES: viabilidade técnica, parcerias CEFET/UnB | Baixa |
| 4 | **Analise Economica.md** | 2023-05-27 | 2.4 KB | Viabilidade financeira, mercado de construçoes sustentáveis, potencial de financiamento | Baixa |
| 5 | **Analise Edificaçoes.md** | 2023-05-27 | 2.7 KB | Planejamento de obra, normas técnicas, controle de qualidade, mão de obra | Baixa |
| 6 | **Analise Estratégia.md** | 2023-09-12 | 2.5 KB | Modelagem financeira, parcerias, fontes de financiamento, riscos | Baixa |
| 7 | **Analise Inv Anjo.md** | 2023-09-12 | 2.3 KB | Perspectiva de investidor-anjo: mercado, diferencial, equipe, estratégia de saída | Baixa |
| 8 | **Analise Marketing.md** | 2023-05-27 | 3.2 KB | Posicionamento, branding, divulgaçao multicanal, networking | Baixa |
| 9 | **Analise Saude e Segurança.md** | 2023-05-27 | 3.1 KB | Gestao de riscos, ergonomia, higiene ocupacional (exposiçao a químicos), EPIs | Média |
| 10 | **Analise Sintetica.md** | 2023-05-28 | 1.2 KB | Resumo multidisciplinar: economia, jurídico, marketing, social | Baixa |
| 11 | **Analise Sustentabilidade.md** | 2023-05-27 | 3.1 KB | Uso do bambu, eficiência energética, ciclo de vida, certificaçoes LEED/BREEAM | Média |
| 12 | **Analise de gestão.md** | 2023-08-15 | 3.0 KB | Escopo, riscos, cronograma, alocaçao de recursos, monitoramento | Baixa |
| 13 | **Analise social.md** | 2023-05-28 | 5.1 KB | Impacto social, habitaçao de interesse social, inclusao, preservaçao cultural, participaçao comunitária | Média |
| 14 | **Analises diversas.md** | 2023-05-27 | 2.3 KB | Compilaçao de perspectivas: economia, jurídico, marketing, saúde, ciências sociais | Baixa |
| 15 | **Análise Gestao Pública.md** | 2023-05-27 | 2.7 KB | Relevância social, alinhamento com políticas públicas, governança, transparência | Baixa |

**Avaliaçao geral das Análises da TTR:** Conteúdo genérico e opinativo, provavelmente gerado por IA. Útil como framework de análise multidisciplinar, mas sem dados originais ou específicos. **Prioridade baixa para o LLM Wiki** — podem ser condensadas em uma única página de "Análise Multidisciplinar do Projeto" (resumo de 2-3 parágrafos cada) ou descartadas em favor de documentos mais substanciais.

---

## 3. SUBPASTA PATENTES (2)

### 3.1 PATENTES.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-12-23 (>2 anos) |
| Tamanho | 0 bytes |
| Resumo | **ARQUIVO VAZIO** |
| Açao sugerida | Excluir |

### 3.2 Proposta de Registro.md
| Campo | Valor |
|-------|-------|
| Modificação | 2023-10-31 (>2,5 anos) |
| Tamanho | 1.5 KB |
| Resumo | Proposta de proteçao intelectual da Takwara Tech: (1) **Marca de Certificaçao "Takwara Green"** em 3 níveis (Bronze/Prata/Ouro); (2) **Patente de Invençao do Forno Ecológico** — licenciamento aberto nao exclusivo, co-titularidade CEFET-MG; (3) **Patente das conexoes flexíveis** para domos geodésicos — privada, para comercializaçao. Datado de 31/10/2023. |
| Estado | Desatualizado — nao sabemos se os registros foram protocolados |
| Prioridade LLM Wiki | **Alta** — estratégia de PI é relevante para o Wiki |
| Açao sugerida | Verificar status atual dos registros (foram protocolados? deferidos?), depois incorporar ao Wiki |

---

## 4. PRIORIDADES PARA INGESTAO NO LLM WIKI

### Prioridade Máxima (ingerir com revisao)
1. **PU + Papelão.md** — cronograma 2023-2026 e escopo do projeto HIS
2. **Sem título.md** — conteúdo mais recente sobre ATHIS e gênero
3. **HIS e BRIQUETES STL.md** — modelo de negócios completo
4. **Tijolos Briquetes.md** — estudo de viabilidade mais robusto
5. **Proposta de Registro.md** (PATENTES) — estratégia de PI

### Prioridade Média (ingerir após revisao)
6. **Forno Ecológico.md** — descriçao técnica (limpar HTML)
7. **Pirolenhoso + Bambu.md** — abordagem ecológica e ensaios
8. **Normas para ensaios.md** + **Tecido Resinado.md** — fundir em protocolos
9. **PU + Bambu.md** — contextualizaçao histórica
10. **Roteiro para testes.md** — ensaios específicos

### Prioridade Baixa (condensar ou pular)
11. **Análises da TTR (15 com conteudo)** — gerar uma única página resumo multidisciplinar de 2-3 parágrafos cada
12. **+TAKWARA TECH.md, Análises da TTR.md, PATENTES.md** — vazios, excluir

---

## 5. RECOMENDAÇOES GERAIS

1. **Limpeza de HTML:** Forno Ecológico.md, Pirolenhoso + Bambu.md contêm HTML cru (tags `<p>`, `<h1>`, `<table>` etc.) que precisam ser removidos antes da ingestao.

2. **Deduplicaçao:** PU + Papelão.md tem 3 versoes do mesmo cronograma (formal, rebuscada e coloquial) que ocupam ~100 linhas desnecessárias — manter apenas uma.

3. **Padronizaçao de nomes:** "Sem título.md" precisa ser renomeado. Arquivos com acentos e espaços (ex: "Forno Ecológico.md") funcionam no Obsidian mas podem causar problemas em ferramentas de linha de comando.

4. **Verificaçao de status:** Para os documentos de PI (Proposta de Registro.md) e cronograma (PU + Papelão.md), seria importante verificar o andamento real dos registros de patente e a conclusao do protótipo HIS (prazo julho/2026 está próximo).

5. **Estratégia de ingestao:** Sugiro criar 5-7 páginas principais no LLM Wiki:
   - Tecnologia Takwara (visao geral + histórico)
   - Forno Ecológico (descriçao técnica)
   - Tratamento com Pirolenhoso
   - Modelo de Negócios (HIS, briquetes, tijolos, créditos de carbono)
   - Projeto PU + Papelão (cronograma e escopo)
   - ATHIS e Gênero (conteúdo do Sem título.md)
   - Propriedade Intelectual (patentes e marcas)

---

*Relatório gerado em 11/06/2026. 29 arquivos analisados, 29 lidos integralmente.*
