# Resumo de Commits - 13/02/2026

Resumo das atividades e alterações realizadas nos repositórios hoje.

## 📱 EuVereadorAI-client (Frontend)

- **396cdd5** - `feat: optimize pix and boleto flow and update page content`
  - Otimização do checkout: geração automática de PIX/Boleto ao abrir o modal.
  - Ajustes textuais em `Support.tsx` e `TermsOfUse.tsx`.
- **ff03ec4** - `fix(dna): resolve step 5 saving issue and update support page content`
  - Correção do salvamento da Etapa 5 do DNA (redes sociais).
  - Primeira rodada de ajustes nos textos de ajuda.
- **6d76e88** - `docs: atualiza política de privacidade e termos de uso`
  - Atualização integral dos textos legais.
- **22abd96** - `docs: sync and refine Terms of Use content`
  - Refinamento inicial e sincronização dos termos.

---

## ⚙️ EuVereadorAI-server (Backend)

- **b6d93fb** - `feat(dna): refactor schema to individual social media columns and ignore env files`
  - Refatoração do banco de dados: troca de JSONB por colunas individuais (`instagram`, `facebook`, etc.).
  - Atualização do validador Zod e do serviço de mapeamento.
  - Configuração de segurança: `.env.production` adicionado ao `.gitignore` e removido do cache do Git.
