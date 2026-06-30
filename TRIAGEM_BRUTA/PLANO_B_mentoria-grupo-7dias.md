# PLANO B — Mentoria Remota em Grupo (7 Dias)

**Para avaliação com comparsas e mentores.**
*Não substitui o plano atual (free unboxing + mentorias individuais). É uma alternativa a ser discutida.*

---

## 1. Estrutura Geral

**Formato:** Remoto em grupo (Zoom ou similar)
**Duração:** 7 dias corridos
**Carga horária diária:** 2 períodos de 1h30 = 3h/dia
**Público:** Grupos de até ___ pessoas (definir)
**Pré-requisito:** Ter o kit Imperveg em mãos

---

## 2. Agenda Diária

| Período | Horário | Atividade |
|---------|---------|-----------|
| ☀️ **Manhã** | 1h30 | Instrução ao vivo (exposição do dia) |
| 🌤️ **Tarde** | 1h30 | Plantão de dúvidas ao vivo |
| 📱 **Permanente** | Horário comercial | WhatsApp — suporte contínuo |
| 🤖 **24h** | Site Vercel | Mentor IA (FAQ + BD estruturado) |

---

## 3. Cronograma dos 7 Dias

### Dia 1 — Apresentação Direta
**Manhã:** Abertura, apresentação do kit, demonstração ao vivo da mistura A+B e aplicação simples.
**Tarde:** Plantão de dúvidas — cada participante mostra seu kit, tira dúvidas iniciais.
**Tarefa:** Preparar o bambu para o dia 2 (cortar, lixar, limpar).

### Dia 2 — Mão na Massa
**Manhã:** Instrução: aplicação do PU Impermeabilizante (UG 132-A) — técnica, camadas, cuidados.
**Tarde:** Plantão — participantes aplicam acompanhados, tiram dúvidas em tempo real.
**Tarefa:** Aplicar a primeira camada e aguardar cura.

### Dia 3 — Conferência + Correção
**Manhã:** Instrução: verificação da cura, identificação de erros (proporção, umidade, irregularidades).
**Tarde:** Plantão — correção guiada de cada participante.
**Tarefa:** Corrigir falhas e aplicar camada final. **Prazo limite para entrega das tarefas.**

### Dia 4 — Conexões e Acabamentos
**Manhã:** Instrução: conexões simples (amarrações, bio-solda), acabamento.
**Tarde:** Plantão de dúvidas.
**Tarefa:** Fazer uma conexão simples entre duas varas.

### Dia 5 — Avanço Livre
**Manhã:** Instrução opcional (conteúdo extra conforme ritmo da turma).
**Tarde:** Plantão de dúvidas.
**Tarefa:** Avançar no projeto pessoal de cada um.

### Dia 6 — Revisão Geral
**Manhã:** Revisão de todos os conceitos, perguntas abertas.
**Tarde:** Plantão final de dúvidas.
**Tarefa:** Finalizar pendências.

### Dia 7 — Fechamento
**Manhã:** Apresentação dos resultados, feedback coletivo.
**Tarde:** Encerramento, próximos passos.
**⚠️ Se alguém não concluiu:** Oferta de **tempo extra de até 2 dias** para finalizar.

---

## 4. Timeline Visual

```
DIA 1 ─── Apresentação direta ─────────────────── 🎤
DIA 2 ─── Mão na massa ────────────────────────── 🛠️
DIA 3 ─── Conferência + Correção ← PRAZO TAREFAS 📋
DIA 4 ─── Conexões e Acabamentos ──────────────── 🔗
DIA 5 ─── Avanço livre ───────────────────────── 🆓
DIA 6 ─── Revisão geral ───────────────────────── 🔄
DIA 7 ─── Fechamento ──────────────────────────── ✅
         ↓ (se necessário)
ATÉ +2 DIAS ─── Tempo extra para conclusão ───── ⏰
```

---

## 5. Canais de Suporte

| Canal | Quando | Para quê |
|-------|--------|----------|
| **Ao vivo (manhã)** | Diário, 1h30 | Instrução |
| **Ao vivo (tarde)** | Diário, 1h30 | Plantão de dúvidas |
| **WhatsApp** | Horário comercial | Dúvidas rápidas, avisos, fotos de andamento |
| **Mentor IA (Vercel)** | 24h | FAQ + BD de perguntas frequentes |

---

## 6. Mentor IA no Site Vercel

**Resposta curta:** Sim, é possível e prático.

**Resposta longa:** O site takwara-mentoria-vercel usa **Nextra** (Next.js + MDX), que já tem busca full-text embutida. Um FAQ bem estruturado é perfeitamente viável e não requer backend externo.

### Opção A — FAQ Estruturado com Busca (Recomendada)

**Como funciona:**
1. O FAQ é uma página MDX normal com perguntas categorizadas
2. O Nextra já indexa todo o conteúdo para busca — o usuário pesquisa e encontra
3. As respostas ficam visíveis na própria página (acordeão ou links âncora)

**Implementação:**
```jsx
// pages/faq.mdx
# FAQ — Mentoria Takwara

## 🧪 PU Vegetal
<details><summary>Qual a proporção correta da mistura A+B?</summary>

A proporção padrão é ______ (especificar). Misturar até homogeneidade total.
</details>

<details><summary>Quanto tempo leva a cura?</summary>

24 a 48h dependendo da temperatura e umidade do ambiente.
</details>

## 🔧 Aplicação
<details><summary>Precisa lixar o bambu antes?</summary>

Sim. Lixar com lixa #36, limpar com álcool 100% para máxima ancoragem química.
</details>
```

**Vantagens:** Zero custo, zero manutenção de servidor, zero API.

### Opção B — Busca Avançada por Categoria

Além do search do Nextra, pode-se adicionar filtros por categoria usando React puro (sem backend). Exemplo de componente:

```tsx
// components/FaqFilter.tsx
export default function FaqFilter({ categories, onFilter }) {
  return (
    <div className="flex gap-2 mb-6">
      {categories.map(cat => (
        <button onClick={() => onFilter(cat)} className="...">{cat}</button>
      ))}
    </div>
  )
}
```

### Opção C — Chatbot com Knowledge Base (Futuro)

Para um chatbot que responde em linguagem natural:
- Frontend React no Vercel
- Backend: API Route do Next.js (fica no próprio Vercel)
- Modelo: OpenRouter com modelo barato (ex: deepseek-v4-flash) ou o próprio Hermes
- Knowledge base: arquivo JSON com perguntas e respostas validadas
- **Custo:** centavos por consulta em token de API

**⚠️ Não recomendado para o lançamento — começar pela Opção A.**

### Instruções para Implementação (Opção A)

1. Criar `pages/faq.mdx` no repositório takwara-mentoria-vercel
2. Estruturar perguntas em categorias usando `<details>` (acordeão nativo)
3. O search do Nextra já indexa automaticamente
4. Adicionar link "FAQ" no menu `_meta.tsx`
5. Manter o FAQ atualizado conforme surgem dúvidas reais nas mentorias

> **Nota:** O mentor IA não substitui o suporte humano. Ele cobre as dúvidas repetitivas (80% dos casos) e libera o mentor para focar no que realmente precisa de atenção personalizada.

---

## 7. Plano A vs. Plano B

| Aspecto | Plano A (atual) | Plano B (este) |
|---------|-----------------|----------------|
| **Formato** | Individual (2 dias) | Grupo (7 dias) |
| **Porta de entrada** | Unboxing gratuito (YouTube) | *** |
| **Produtos** | 6 mentorias específicas | Mentoria única em grupo |
| **Suporte** | 2 dias máx. | 7 dias + até 2 extras |
| **Kit Imperveg** | Incluso nas mentorias | Incluso |
| **Preço sugerido** | *** | **R$ 1.999,00** (já incluso o kit) |
| **Mentor IA** | Planejado (futuro) | Desde o lançamento (FAQ + BD) |
| **Status** | ✅ Implementando | ⏳ Em avaliação com comparsas |

---

## 8. Próximos Passos para Avaliação

- [ ] Definir valor do Plano B (por participante)
- [ ] Definir número máximo de participantes por turma
- [ ] Testar viabilidade do FAQ/Vercel (Opção A)
- [ ] Validar com comparsas e mentores
- [ ] Decidir: Plano A, Plano B, ou ambos?

---

*Documento gerado em 15/06/2026 para avaliação com comparsas e mentores. Não substitui o plano atual.*
