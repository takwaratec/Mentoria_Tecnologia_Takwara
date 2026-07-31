# RELATORIOS/README.md

> Relatórios de auditoria, diagnóstico e verificação do ecossistema.
> Gerados pelo Hermes Agent após varreduras autorizadas.

## Estrutura

```
RELATORIOS/
├── auditorias/       ← Relatórios de auditoria de repositórios
├── status-git/       ← Estado Git de cada repositório (branch, HEAD, status, remotos)
├── builds/           ← Resultados de mkdocs build --strict
└── seguranca/        ← Verificações de segurança e conformidade
```

## Convenções

- Relatórios são **apenas leitura**. Não versionar conclusões não autorizadas.
- Nomear arquivos como `YYYY-MM-DD_repo_assunto.md`.
- Relatórios de repositórios irmãos são diagnósticos — não copiam conteúdo dos projetos.
- Relatórios não substituem os documentos originais dos projetos.

## Fonte

Os dados são coletados via comandos Git, leitura de AGENTS.md locais e verificação de
estrutura de diretórios. Nenhuma informação sensível (credenciais, tokens, contatos
pessoais) deve constar nestes relatórios.

---

*Estrutura criada em 30/07/2026. Nenhum relatório versionado ainda.*
