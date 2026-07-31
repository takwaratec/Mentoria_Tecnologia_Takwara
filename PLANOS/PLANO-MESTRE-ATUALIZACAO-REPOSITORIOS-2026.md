# Plano Mestre de Atualização dos Repositórios — 2026

> Documento de coordenação do ecossistema Tecnologia Takwara.
> Elaborado em 13/07/2026 a partir da leitura local dos históricos Git.
> Atualizado em 22/07/2026 com a política de administração dos ativos públicos.
> Estado: plano aprovado para orientar as próximas tarefas; nenhuma execução nos repositórios irmãos está implícita.

---

## 1. Objetivo

Atualizar os repositórios do ecossistema um por vez, preservando:

- a cronologia real da trajetória de Fabio Takwara;
- a autoria e a contribuição de cada parceiro;
- as fronteiras entre projetos;
- o histórico Git e as alterações locais existentes;
- a distinção entre pesquisa cidadã, evidência científica publicada e validação institucional;
- a privacidade, os direitos autorais e a segurança dos materiais não públicos.

O trabalho será conduzido em duas leituras complementares:

1. **Cronologia histórica:** explica como o ecossistema surgiu e se desenvolveu.
2. **Ordem operacional:** define qual repositório será saneado primeiro conforme risco, dependências e prioridade atual.

---

## 2. Fontes de verdade

| Fonte | Responsabilidade |
|---|---|
| **Mentoria_Tecnologia_Takwara** | Regência, regras gerais, mapa das frentes e status resumido |
| **Acervo Soberania Tecnológica** | Referências públicas, fichas científicas, estados da arte e perfis documentais |
| **Repositório de cada projeto** | Atas, planos, cartas, proposta, cronograma, responsáveis e estado detalhado do projeto |
| **Material bruto local** | Insumo de trabalho; não é evidência pública nem conteúdo automaticamente publicável |
| **Fonte pública original** | Evidência verificável: artigo, DOI, ISBN, ISSN, norma, edital ou documento institucional público |

### Regra de atualização

O fato é primeiro confirmado e atualizado no repositório responsável. Somente depois o Maestro recebe o resumo.

```text
fonte original → repositório responsável → validação → commit → atualização do Maestro
```

O README do Maestro não deve ser usado como banco de prazos operacionais detalhados. Prazos, responsáveis e pendências ficam no repositório do projeto e são resumidos no `FRENTES_DE_TRABALHO.md`.

---

## 3. Cronologia histórica do ecossistema

As datas abaixo correspondem ao primeiro commit encontrado no histórico Git local. Elas não substituem os 40 anos de autodidatismo, experimentação e atuação de Fabio Takwara que antecedem os repositórios.

| Ordem | Repositório | Primeiro commit local | Papel histórico |
|---:|---|---:|---|
| 1 | `Takwara-Tech` | 30/05/2025 | Repositório histórico da primeira documentação digital consolidada |
| 2 | `UnB/Mulheres_Bioeconomia_Amazonia` | 01/03/2026 | Expansão para a bioeconomia amazônica |
| 3 | `UnB/Mulheres-Tecem-Amazonia` | 18/03/2026 | Desenvolvimento da frente Mulheres Tecem Amazônia |
| 4 | `Mulheres-Tecem-Amazonia_Clone` | 18/03/2026 | Clone local posterior; confirmar qual cópia é canônica antes de qualquer edição |
| 5 | `Mentoria_Tecnologia_Takwara` | 10/06/2026 | Formação do repositório Maestro |
| 6 | `acervo-soberania-tecnologica` | 21/06/2026 | Consolidação do coração científico e documental |
| 7 | `ECOSALA` | 25/06/2026 | Frente coletiva e articulação acadêmica |
| 8 | `fundo-vaga-lumen-2026` | 25/06/2026 | Proposta Vaga Lúmen e memória documental própria |
| 9 | `fabrica-modelo` | 29/06/2026 | Frente independente de industrialização da construção |
| 10 | `ludmila-athis-df` | 30/06/2026 | Frente independente Ludmila / ATHIS-DF |

### Interpretação pública da genealogia

- **Fabio Takwara** é pesquisador cidadão, autodidata e idealizador da frente de organização desses projetos em diálogo com a comunidade acadêmica.
- **Resck** guarda parte da camada histórica dos repositórios.
- **takwaratec** é a conta criada para centralizar a produção atual dos projetos.
- O Acervo demonstra capacidade de curadoria, sistematização e articulação documental. Ele não equivale, por si só, à validação acadêmica das tecnologias experimentais.
- Repositórios históricos preservam memória e proveniência, mas não devem ser citados como evidência científica pública.

---

## 4. Escopo atual

### Repositórios em pauta operacional

1. `acervo-soberania-tecnologica`
2. `ECOSALA`
3. `fundo-vaga-lumen-2026`
4. `fabrica-modelo`
5. `ludmila-athis-df`

### Repositório de coordenação

- `Mentoria_Tecnologia_Takwara`, atualizado após cada marco validado.

### Frente futura e privada

- `Mulheres-Tecem-Amazonia` (MQTF): preparação para submissão em 2027; será o único repositório tornado privado nesta rodada.
- A mudança de visibilidade só ocorrerá depois da preservação das alterações locais e da confirmação da cópia canônica.

### Repositórios históricos

- `Takwara-Tech`;
- `UnB/Mulheres_Bioeconomia_Amazonia`;
- `UnB/Mulheres-Tecem-Amazonia`;
- repositório Git aninhado em `UnB/Mulheres_Bioeconomia_Amazonia/01_SOMBRA_AUDITORIA/REPO_EXECUTIVO_2026`.

Esses repositórios entram inicialmente em **modo de preservação e inventário**, sem reorganização, migração ou reescrita de histórico.

---

## 5. Ordem operacional de atualização

### Etapa 0 — Segurança e preparação

Aplicável antes de editar qualquer repositório.

- [ ] Confirmar permissão de escrita somente para o repositório da tarefa.
- [ ] Ler o `AGENTS.md` local completo.
- [ ] Registrar branch, remoto, primeiro e último commit.
- [ ] Registrar arquivos modificados e não rastreados antes da intervenção.
- [ ] Não executar `git pull` quando houver alterações locais sem antes analisar conflitos possíveis.
- [ ] Não apagar, mover ou sobrescrever trabalho preexistente sem identificar sua origem.
- [ ] Não fazer push, deploy ou reescrita de histórico sem autorização explícita de Fabio.

### Etapa 1 — Acervo Soberania Tecnológica

**Motivo da precedência:** é a fonte científica do ecossistema e apresenta risco imediato de publicação de material privado ou protegido.

Objetivos:

- retirar da árvore publicável documentos privados, fiscais, societários e dados pessoais;
- impedir que PDFs comerciais ou obras integrais locais sejam copiados pelo MkDocs;
- separar fichas homologadas, fichas em revisão, visão autoral, perfis, ingestão automática e quarentena;
- corrigir a identidade antiga “Análises e Escrita Científica”;
- definir uma contagem auditável por tipo e estado;
- revisar a atribuição e a referência do protocolo inspirado em Nathalia Cavichiolli;
- reescrever `README.md` e `docs/index.md`;
- corrigir navegação, links e metadados do MkDocs;
- fazer o build estrito encerrar sem avisos relevantes;
- preservar as alterações locais já existentes antes de criar qualquer commit.

**Critério de conclusão:** publicação segura, identidade coerente, inventário reproduzível e alegações públicas rastreáveis.

### Etapa 2 — Primeiro checkpoint do Maestro

Após o Acervo ser validado:

- atualizar no Maestro o nome, função, endereço e números auditados do Acervo;
- registrar o papel de Fabio como idealizador e curador, sem converter curadoria em validação institucional;
- corrigir referências antigas a “Análises e Escrita Científica”;
- não copiar fichas científicas para a Mentoria.

### Etapa 3 — ECOSALA

**Cronologia:** primeiro commit em 25/06/2026.

Objetivos:

- preservar as alterações locais preexistentes antes de editar;
- atualizar README e Index a partir das atas e decisões confirmadas;
- distinguir membro, participante, prospecto, parceiro e instituição anuente;
- revisar o estado real da relação ECOSALA/Vaga Lúmen;
- retirar prazos vencidos ou marcá-los com resultado confirmado;
- separar narrativa de prêmio retrospectivo e proposta FINEP prospectiva;
- garantir que tecnologias experimentais não sejam apresentadas como aplicadas em comunidades;
- revisar links para o Acervo usando apenas endereços públicos estáveis;
- validar o site antes de qualquer deploy.

**Critério de conclusão:** estado coletivo confirmado, papéis honestos, cronograma atual e documentos públicos coerentes com as atas.

### Etapa 4 — Vaga Lúmen

**Cronologia:** primeiro commit em 25/06/2026, após a análise do ECOSALA na ordem operacional por depender da relação entre as duas frentes.

Objetivos:

- preservar o repositório como memória própria da proposta;
- documentar com clareza o que foi incorporado ao ECOSALA e o que permanece autônomo;
- marcar documentos históricos para que não sejam confundidos com versão vigente;
- revisar edital, elegibilidade, TRL, orçamento e status da proposta;
- corrigir README, Index, links e navegação;
- não duplicar no Vaga Lúmen documentos cujo responsável atual seja o ECOSALA.

**Critério de conclusão:** fronteira ECOSALA/Vaga Lúmen explícita e versões históricas claramente identificadas.

### Etapa 5 — Fábrica Modelo

**Cronologia:** primeiro commit em 29/06/2026.

Objetivos:

- atualizar o estado a partir do retorno real de André, Maurilho e Michel;
- diferenciar proposta, negociação, anuência, contratação e parceria confirmada;
- revisar a viabilidade da proponente e da contrapartida sem misturar com ECOSALA;
- preservar Fabio como assessoria técnica e idealizador, não fornecedor automático;
- revisar documentos públicos, README, Index, Vercel e links;
- validar afirmações técnicas apenas com fontes públicas do Acervo.

**Critério de conclusão:** situação negocial fiel, responsabilidades delimitadas e material público sem compromisso presumido.

### Etapa 6 — Ludmila / ATHIS-DF

**Cronologia:** primeiro commit em 30/06/2026.

Objetivos:

- preservar as alterações locais existentes;
- separar contexto histórico, transcrições brutas, atas e documentos públicos;
- revisar consentimento, atribuição e dados pessoais;
- diferenciar trajetória de Ludmila, contribuição de Fabio e documentos institucionais;
- não cruzar a frente pessoal LaPCiS com projetos parceiros;
- revisar README, Index, navegação e estado atual.

**Critério de conclusão:** arquivo histórico organizado, privacidade preservada e papéis corretamente atribuídos.

### Etapa 7 — Mulheres Tecem Amazônia / submissão 2027

Executar somente após estabilizar as frentes de 2026.

Objetivos iniciais:

- identificar qual repositório é canônico entre original, clone e repositório aninhado;
- preservar a genealogia e evitar divergência entre cópias;
- inventariar as centenas de alterações locais antes de qualquer ação;
- planejar a submissão de 2027 em documento próprio;
- separar o legado de bioeconomia amazônica da nova submissão;
- tratar MQTF como sigla interna quando o documento público exigir o nome descritivo do projeto.

**Critério de conclusão inicial:** repositório canônico definido e plano 2027 aprovado, sem perda de histórico.

### Etapa 8 — Repositórios históricos

Somente após autorização específica.

- produzir inventário de proveniência;
- registrar relação com a trajetória de 40 anos de Fabio;
- classificar o que é memória, experimento, documento autoral e fonte pública;
- não reescrever a linguagem histórica para simular conhecimento posterior;
- não usar documentos internos como evidência científica externa;
- não fazer limpeza destrutiva ou reescrita do Git sem cópia de segurança e autorização.

---

## 6. Protocolo aplicado a cada repositório

Cada atualização será uma tarefa própria e seguirá a mesma sequência.

### 6.1 Diagnóstico

- consultar `AGENTS.md` e instruções locais;
- ler README, Index, configuração de publicação e documentos de estado;
- comparar conteúdo declarado com a estrutura real;
- executar inventário de arquivos, links e navegação;
- identificar conteúdo privado, protegido, incompleto ou fora de escopo;
- registrar o estado inicial do Git.

### 6.2 Plano local

- listar achados por prioridade: crítico, alto, médio e editorial;
- definir arquivos que serão alterados;
- identificar decisões que dependem de Fabio;
- confirmar o destino de arquivos que pertencem a outro repositório;
- interromper a execução se a ação exigir mudança de escopo ou de autoria.

### 6.3 Execução

- fazer alterações mínimas e rastreáveis;
- preservar arquivos não relacionados e mudanças preexistentes;
- usar somente fontes públicas verificáveis como evidência externa;
- indicar paráfrases e não fabricar citações literais;
- rotular claramente material experimental, proposta, prospecto e parceria confirmada;
- manter documentos brutos, privados e protegidos fora da árvore publicável.

### 6.4 Validação

- revisar o diff completo;
- testar links internos;
- executar build estrito quando houver MkDocs;
- verificar referências, DOI/ISBN/ISSN e atribuições;
- procurar dados pessoais e documentos indevidamente publicáveis;
- apresentar o resultado a Fabio antes de push ou deploy.

### 6.5 Versionamento

- um commit lógico por repositório e etapa;
- mensagem de commit descritiva;
- nunca misturar arquivos de dois repositórios no mesmo commit;
- push e deploy somente após revisão e autorização;
- registrar no Maestro apenas o que foi efetivamente concluído.

---

## 7. Estados documentais padronizados

Todo documento público ou inventariado deve receber um estado compreensível.

| Estado | Significado | Pode ser publicado? |
|---|---|:---:|
| **Homologado documentalmente** | Metadados, original e estrutura conferidos; não significa validação científica da tecnologia | Sim |
| **Em revisão** | Conteúdo utilizável, mas ainda depende de conferência | Somente em área explicitamente marcada, se necessário |
| **Extração preliminar** | Resultado automático ainda não revisado | Não |
| **Visão autoral** | Interpretação ou proposição de Fabio, claramente identificada | Sim, com atribuição e separação da evidência |
| **Documento histórico** | Preservado para memória, não representa o estado vigente | Conforme privacidade e direitos |
| **Privado/restrito** | Dados pessoais, fiscais, contratos ou material interno | Não |
| **Protegido por direitos autorais** | Obra de terceiro sem licença pública suficiente | Não distribuir; publicar apenas uso permitido |
| **Quarentena** | Incompleto, duplicado, sem identificação ou fora de escopo | Não |

---

## 8. Critérios gerais de qualidade

Uma etapa somente será considerada concluída quando:

- [ ] nenhuma informação privada estiver na árvore publicável;
- [ ] nenhum produto comercial ou obra integral de terceiro for distribuído sem licença;
- [ ] README, Index, AGENTS e configuração do site usarem o mesmo nome e endereço;
- [ ] números publicados vierem de inventário reproduzível;
- [ ] citações literais tiverem fonte e localização verificáveis;
- [ ] referências científicas apresentarem autor e identificador aplicável;
- [ ] fichas incompletas não forem apresentadas como homologadas;
- [ ] prospectos não forem apresentados como parceiros;
- [ ] propostas laboratoriais não forem apresentadas como aplicação comunitária comprovada;
- [ ] links e navegação forem testados;
- [ ] mudanças locais preexistentes forem preservadas;
- [ ] o Maestro refletir somente fatos confirmados.

---

## 9. Estado Git observado em 13/07/2026

Este quadro é apenas uma fotografia inicial. Deve ser refeito no começo de cada tarefa.

| Repositório | Último commit local | Alterações locais observadas |
|---|---:|---:|
| Acervo Soberania Tecnológica | 09/07/2026 | 5 |
| Mentoria / Maestro | 09/07/2026 | 2 |
| ECOSALA | 09/07/2026 | 33 |
| Vaga Lúmen | 30/06/2026 | 0 |
| Fábrica Modelo | 08/07/2026 | 0 |
| Ludmila / ATHIS-DF | 07/07/2026 | 2 |
| Mulheres Tecem Amazônia — clone | 26/06/2026 | 1 |
| Takwara-Tech | 26/06/2026 | 8 |
| `UnB/Mulheres-Tecem-Amazonia` | 13/04/2026 | 780 |
| `UnB/Mulheres_Bioeconomia_Amazonia` | 11/06/2026 | 33 |

> Alteração local não significa erro. Pode ser trabalho válido de Fabio ou de sessões anteriores e deve ser preservada até identificação.

---

## 10. Sequência resumida

```text
0. Segurança e inventário
   ↓
1. Acervo Soberania Tecnológica
   ↓
2. Checkpoint no Maestro
   ↓
3. ECOSALA
   ↓
4. Vaga Lúmen
   ↓
5. Fábrica Modelo
   ↓
6. Ludmila / ATHIS-DF
   ↓
7. Mulheres Tecem Amazônia — preparação 2027
   ↓
8. Repositórios históricos — preservação e proveniência
   ↓
9. Consolidação final no Maestro
```

---

## 11. Próxima tarefa autorizável

Iniciar a **Etapa 1 — Acervo Soberania Tecnológica**, em uma tarefa própria, com este primeiro recorte:

1. inventariar e proteger conteúdo privado ou protegido;
2. definir a taxonomia de estados documentais;
3. reconstruir a contagem real do acervo;
4. propor a nova redação de README e Index;
5. corrigir a publicação somente após aprovação de Fabio.

---

## 12. Política de administração dos ativos públicos — decisão de 22/07/2026

### 12.1 Decisão de visibilidade

- **Privado:** somente `Mulheres-Tecem-Amazonia` (MQTF), alteração concluída em 22/07/2026 após salvaguarda local.
- **Públicos:** os demais repositórios permanecem acessíveis aos participantes e ao público após saneamento de informações sensíveis.
- **Canônico científico:** `acervo-soberania-tecnologica` será a única referência científica do ecossistema.
- **Repositórios de projeto:** documentam gestão, memória, propostas e entregas de sua própria frente; não funcionam como bases científicas paralelas.
- **Repositório Maestro:** `Mentoria_Tecnologia_Takwara` administra regras, mapa de ativos e estado resumido; não replica fichas nem documentos dos projetos.

Manter um repositório público, ainda que sem divulgação ativa, significa disponibilizá-lo publicamente. Por isso, a ausência de promoção não substitui a triagem de sigilo, dados pessoais, direitos autorais ou propriedade intelectual.

### 12.2 Inventário administrativo da conta TakwaraTec

A consulta da conta em 22/07/2026 identificou 15 repositórios públicos. A classificação abaixo é administrativa e não atribui validade científica ao conteúdo.

| Classe | Repositórios | Regra principal |
|---|---|---|
| Referência científica | `acervo-soberania-tecnologica` | Curadoria, fontes verificáveis, versões e depósitos citáveis |
| Coordenação e método | `Mentoria_Tecnologia_Takwara`, `Mentoria_Comunidades_RaioX` | Governança, formação e ferramentas; sem duplicar o Acervo |
| Projetos ativos ou latentes | `ECOSALA`, `fundo-vaga-lumen-2026`, `fabrica-modelo`, `eco-prancha`, `plataforma-juventude-solidaria-2026`, `unb-desafios-amazonia-2026`, `ludmila-athis-df` | Somente conteúdo da frente, com estado e papéis explícitos |
| Divulgação e interfaces | `Personagens-Bambu`, `takwara-mentoria-vercel` | Conteúdo educacional ou de apresentação, sem alegações científicas autônomas |
| Legado, agregação ou teste | `projetos`, `docmd-test-takwara` | Auditar finalidade; arquivar ou despublicar quando não houver função ativa |
| Futuro e restrito | `Mulheres-Tecem-Amazonia` | Tornar privado após salvaguarda; preparação para 2027 |

Os repositórios históricos da conta Resck e as cópias locais da UnB permanecem em inventário próprio. Eles não devem ser confundidos com os 15 ativos públicos atuais da conta TakwaraTec.

### 12.3 Níveis de informação

| Nível | Conteúdo | Destino |
|---|---|---|
| **P0 — Público citável** | Ficha homologada, referência identificada, caderno final, versão depositada e documento institucional público | Acervo ou serviço de depósito, conforme a natureza |
| **P1 — Público de projeto** | Apresentação, ata saneada, edital público, cronograma, entrega, autoria e papéis consentidos | Repositório responsável pelo projeto |
| **P2 — Interno operacional** | Áudio, transcrição, minuta, negociação, orçamento não publicado, fonte privada, contato pessoal, relatório bruto | Armazenamento local protegido; nunca na árvore Git pública |
| **P3 — Restrito** | Credencial, documento pessoal, assinatura, contrato reservado, segredo comercial ou detalhe técnico potencialmente protegível | Cofre ou pasta privada com acesso nominal; nunca em Git público |

O diretório `_privado/` só é aceitável dentro de um repositório local quando estiver efetivamente ignorado e nunca tiver sido versionado. Para material sensível de longo prazo, prefere-se armazenamento separado do clone público.

### 12.4 Fronteira que protege o Acervo

1. O Acervo recebe fichas científicas completas, fontes originais identificadas e documentos autorais claramente rotulados.
2. Atas, propostas, contratos, transcrições e gestão de parceiros permanecem nos repositórios dos projetos ou em armazenamento privado.
3. Um relatório interno pode orientar pesquisa, mas não será citado como comprovação científica externa.
4. Repositórios de projeto não duplicam fichas nem mantêm versões concorrentes de cadernos científicos.
5. Quando um projeto precisar de fundamento científico, cita a fonte pública original ou a versão estável depositada com DOI; não depende de um arquivo mutável de outro repositório.
6. Conteúdo experimental declara hipótese, inferência, ensaio planejado ou resultado observado de acordo com a evidência disponível, sem inflar TRL.
7. Perfis e atribuições públicas exigem fonte institucional vigente ou aprovação da própria pessoa; notas internas de revisão não aparecem no material publicado.
8. Nenhuma sincronização automática copia documentos de projetos para o Acervo.

### 12.5 Kit mínimo de governança de cada repositório público

Cada ativo público deve ter, proporcionalmente ao seu tamanho:

- `README.md`: finalidade, público, responsável, estado atual e limites do repositório;
- `STATUS.md`: ativo, latente, suspenso, histórico, experimental ou arquivado, com data de revisão;
- `GOVERNANCA_CONTEUDO.md`: o que pode e o que não pode ser publicado;
- `.gitignore`: credenciais, `_privado/`, fontes privadas, áudios, transcrições brutas, arquivos temporários e exportações locais;
- canal de contato para correção de autoria, privacidade ou exposição acidental;
- licença compatível com os materiais realmente publicados;
- `CITATION.cff` apenas quando o repositório for uma obra efetivamente citável, evitando conferir aparência de publicação científica a espaços de gestão.

O rodapé ou aviso editorial dos projetos deve dizer, em essência: **“Este repositório documenta uma frente de trabalho. Alegações científicas dependem das fontes primárias citadas e não são validadas pela simples presença neste repositório.”**

### 12.6 Portão de publicação

Nenhuma alteração pública relevante passa diretamente do material bruto para `main` ou para o site.

```text
material bruto
  → classificação P0/P1/P2/P3
  → revisão de autoria, consentimento e direitos
  → revisão de evidência e linguagem
  → revisão de propriedade intelectual
  → teste de links e publicação
  → diff apresentado a Fabio
  → commit, tag e deploy autorizados
```

Para o Acervo, acrescentam-se a conferência do original, das oito seções Cavichiolli, dos metadados e do estado documental. Para projetos, acrescentam-se a confirmação de papéis, compromissos, orçamento e vigência.

### 12.7 Saneamento dos repositórios públicos

Aplicar a cada repositório, um por vez:

1. congelar uma fotografia do Git e preservar mudanças locais;
2. localizar credenciais, dados pessoais, assinaturas, contatos, contratos, áudios, transcrições e fontes privadas;
3. localizar formulações, parâmetros e descrições técnicas que possam exigir decisão de propriedade intelectual;
4. retirar P2/P3 da versão pública e registrar apenas a existência administrativa do material, quando necessário;
5. verificar se o conteúdo sensível já apareceu no histórico Git;
6. rotacionar imediatamente qualquer credencial exposta — apagar o arquivo atual não invalida o segredo nem o remove do histórico;
7. decidir reescrita de histórico somente para ocorrências graves, com cópia de segurança, mapa de impactos e autorização específica;
8. padronizar README, estado, governança, licença e `.gitignore`;
9. revisar Pages/Vercel e confirmar que o site publica somente a árvore autorizada;
10. validar e versionar sem misturar repositórios.

### 12.8 Salvaguarda e privatização do MQTF

Antes da mudança de visibilidade:

1. identificar a cópia canônica entre o diretório UnB e o clone local;
2. produzir backup íntegro do repositório, patch das alterações rastreadas, lista dos não rastreados e somas de verificação;
3. conciliar os commits existentes somente após compreender as divergências;
4. registrar colaboradores que continuarão com acesso;
5. tornar o repositório privado mediante autorização expressa;
6. verificar o estado do GitHub Pages e qualquer publicação externa;
7. conferir acesso dos participantes e manter a preparação de 2027 isolada do Acervo público.

### 12.9 Rotina de administração

| Frequência | Controle |
|---|---|
| A cada alteração pública | Portão de publicação, diff, teste e autorização |
| Mensal | Varredura de segredos/dados pessoais, links, visibilidade e páginas publicadas |
| Trimestral | Revisão de status, colaboradores, licenças, repositórios sem função e material duplicado |
| Antes de edital, DOI ou release | Auditoria editorial, científica, jurídica e de propriedade intelectual proporcional ao risco |
| Ao encerrar uma frente | Marcar como histórica, retirar publicação desnecessária e arquivar sem apagar a memória |

O inventário mestre deve registrar: conta, repositório, finalidade, classe, visibilidade, responsável, participantes com acesso, Pages/Vercel, licença, última auditoria, riscos abertos e próxima revisão.

### 12.10 Responsabilidades

**Codex pode executar, após autorização da etapa:**

- inventariar repositórios locais e remotos;
- produzir relatórios de risco e listas de arquivos sensíveis;
- preparar backups e conciliar cópias sem destruir alterações;
- propor ou aplicar saneamento, `.gitignore`, documentos de governança e verificações automáticas;
- revisar README, Index, Pages/Vercel, links, metadados e coerência editorial;
- preparar commits separados e apresentar os diffs;
- alterar visibilidade, fazer push, deploy ou release somente com autorização explícita.

**Fabio decide ou executa diretamente:**

- revogação e rotação de credenciais em serviços externos;
- quem mantém acesso ao MQTF e a materiais privados;
- consentimento de perfis, contatos e atribuições que não tenham fonte pública suficiente;
- escolhas de licenciamento, exploração econômica e propriedade intelectual;
- aprovação final de depósitos no Zenodo, DOI, mudança de visibilidade, reescrita de histórico, push e deploy.

### 12.11 Ordem recomendada desta rodada

1. **Segurança imediata:** revogar a credencial GitHub anteriormente exposta e higienizar os remotos locais.
2. **MQTF:** preservar as 780 alterações locais, definir a cópia canônica e então tornar privado.
3. **Inventário mestre:** reconciliar as 13 frentes do documento com os 15 repositórios públicos da conta.
4. **Acervo:** concluir saneamento, auditoria de propriedade intelectual, README/Index e primeira versão citável.
5. **Repositórios de maior exposição:** ECOSALA, Vaga Lúmen, Fábrica Modelo e Ludmila/ATHIS.
6. **Demais projetos públicos:** Juventude Solidária, Desafios Amazônia, Eco Prancha e interfaces de mentoria.
7. **Legado e testes:** decidir função de `projetos` e `docmd-test-takwara`; arquivar ou despublicar se não tiverem público ativo.
8. **Rotina contínua:** auditoria mensal e revisão trimestral do inventário.

---

*Plano elaborado por Codex em colaboração com Fabio Takwara · Tecnologia Takwara · 13/07/2026.*
