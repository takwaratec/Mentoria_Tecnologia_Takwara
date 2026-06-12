## Deploy no Vercel com Nextra

### Pré-requisitos

- Node.js instalado
- Git instalado
- Conta no GitHub
- Conta no Vercel (vercel.com — login com GitHub)

### Passo a passo completo

#### 1. Criar o projeto

```bash
# Criar com template Nextra
npx create-next-app --example https://github.com/shuding/nextra-docs-template meurepo

# Entrar na pasta
cd meurepo

# Instalar dependências
npm install
```

#### 2. Desenvolvimento local

```bash
# Servidor local com hot-reload
npm run dev

# Build de produção
npm run build

# Servidor de produção local
npm start
```

#### 3. Erros comuns no build

| Erro | Causa | Solução |
|---|---|---|
| `Module not found: Can't resolve '@floating-ui/dom'` | Dependência quebrada do headlessui | `npm install @floating-ui/core @floating-ui/dom @floating-ui/react-dom @floating-ui/react` |
| `export 'computePosition' was not found in '@floating-ui/react-dom'` | Versão incompatible do floating-ui | Instalar todos os 4 pacotes acima |
| `Module not found: Can't resolve '@floating-ui/core'` | Faltou um dos 4 | Instalar todos juntos |
| `ESLint must be installed` | Aviso apenas | Ignorar, não bloqueia o build |
| `Failed to load next.config.js — require(...) is not a function` | Nextra 4+ em ESM | Usar `import nextra from 'nextra'` no lugar de `require()` |
| `Support of "_meta.json" was removed` | Nextra 3.3+ exige `_meta.tsx` | Converter `_meta.json` → `_meta.tsx` com `export default { ... }` |
| Peer dependency warnings | Versões conflitantes | Usar `--legacy-peer-deps` se necessário |

#### 4. Publicar no Vercel

```bash
# Criar repositório no GitHub
git init
git add -A
git commit -m "feat: site Nextra"
git branch -M main
gh repo create user/nome-do-repo --public
git push -u origin main
```

Depois:
1. Acesse https://vercel.com
2. Login com GitHub
3. Clique em **Add New Project**
4. Escolha o repositório criado
5. Clique em **Deploy** (Vercel detecta automaticamente o Next.js)

O site estará no ar em `https://nome-do-repo.vercel.app`

#### 5. Domínio personalizado (opcional)

No dashboard do Vercel:
- Settings → Domains
- Adicione seu domínio
- Configure os registros DNS apontando para Vercel
