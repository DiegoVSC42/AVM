# Documento de Requisitos do Produto (DRP)

## Eu Vereador AI
### Assistente de Comunicação para Vereadores

**Versão:** 1.0  
**Data:** 30 de outubro de 2025  
**Status:** MVP em Desenvolvimento  
**Documento:** Versão para Orçamento

*Confidencial - Para Orçamento*

---

## Índice

1. [Visão Executiva](#visão-executiva)
2. [Objetivos de Negócio e Métricas de Sucesso](#objetivos-de-negócio-e-métricas-de-sucesso)
3. [Personas Primária - MVP](#personas-primária---mvp)
4. [Funcionalidades do Produto](#funcionalidades-do-produto)
5. [Jornada do Usuário e Fluxos](#jornada-do-usuário-e-fluxos)
6. [Interface e Design](#interface-e-design)
7. [Arquitetura Técnica e Integrações](#arquitetura-técnica-e-integrações)
8. [Casos de Uso Detalhados](#casos-de-uso-detalhados)
9. [Requisitos Não-Funcionais](#requisitos-não-funcionais)
10. [Critérios de Aceitação do MVP](#critérios-de-aceitação-do-mvp)
11. [Escopo Detalhado de Desenvolvimento](#escopo-detalhado-de-desenvolvimento)
12. [Entregáveis Esperados](#entregáveis-esperados)
13. [Segurança](#segurança)
14. [Suporte Pós-Lançamento](#suporte-pós-lançamento)
15. [Informações para Orçamento](#informações-para-orçamento)
16. [Contatos e Dúvidas](#contatos-e-dúvidas)

---

## Visão Executiva

### Contexto e Problema

Vereadores brasileiros enfrentam desafios significativos na comunicação com seus eleitores. A maioria dos vereadores municipais possui renda mensal de aproximadamente R$ 4.000,00, não dispõe de assessores de comunicação e muitas vezes não possui ensino médio completo. Essa combinação de recursos limitados e baixa escolaridade resulta em dificuldade para interpretar demandas, desenvolver ideias de comunicação e produzir conteúdo estratégico para prestação de contas e engajamento com a população.

### Proposta de Solução

Eu Vereador AI é uma plataforma de inteligência artificial que auxilia vereadores na produção de conteúdo de comunicação personalizado, estratégico e adequado ao contexto específico de cada mandato. A solução utiliza sistema proprietário de IA para gerar conteúdo para diversos canais (redes sociais, discursos, artigos, releases) baseado em informações estruturadas sobre o perfil político, ideológico e geográfico do vereador.

A personalização é alcançada através de um perfil detalhado chamado DNA, que captura desde informações básicas (nome, cidade, mandato) até aspectos estratégicos (ideologia, posicionamento em relação à gestão, bairros-alvo, temas prioritários). O sistema aprende continuamente com as preferências do usuário, refinando o estilo e o tom dos conteúdos gerados ao longo do tempo.

### Proposta de Valor Única

O Eu Vereador AI diferencia-se por combinar três elementos fundamentais: personalização profunda baseada no contexto político e geográfico do mandato, aplicação de metodologia comprovada de comunicação política desenvolvida por Marcelo Vitorino (especialista com mais de 20 anos de experiência) e interface simplificada focada em mobile-first para atender usuários com baixa familiaridade tecnológica.

### Validação Preliminar

Um protótipo do conceito foi testado como custom GPT com vereadores que participaram de curso promovido pela equipe. O protótipo registrou mais de 90 utilizações em menos de um mês, validando a demanda e o interesse pelo tipo de solução proposta. O feedback geral dos usuários foi positivo, embora tenha sido identificada como principal objeção a dificuldade de uso, o que reforça a necessidade de investimento em interface intuitiva e onboarding estruturado.

---

## Objetivos de Negócio e Métricas de Sucesso

### Objetivos do MVP

O MVP tem três objetivos principais que definirão seu sucesso:

**Objetivo 1: Validação de Adoção**

Alcançar 100 usuários mensais ativos que utilizem regularmente a plataforma para geração de conteúdo.

**Objetivo 2: Validação de Retenção**

Manter baixo índice de churn, demonstrando que o produto entrega valor contínuo e se torna ferramenta recorrente na rotina de comunicação dos vereadores.

**Objetivo 3: Validação de Interesse em Evolução**

Identificar interesse manifestado pelos usuários nas ferramentas futuras (Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais).

### Modelo de Monetização

Modelo de assinatura recorrente mensal no valor de R$ 300,00 por usuário. O sistema implementa limitador de uso baseado em custos operacionais internos, com notificações ao usuário quando aproximar-se do limite mensal.

---

## Personas Primária - MVP

### Vereador Municipal de Recursos Limitados

**Demografia:**

Homem ou mulher, idade entre 35 e 55 anos, residente em cidade de pequeno ou médio porte no interior brasileiro. Renda mensal de aproximadamente R$ 4.000,00. Escolaridade até ensino médio incompleto ou completo.

**Contexto Profissional:**

Não possui assessores de comunicação. Gerencia suas redes sociais pessoalmente ou com ajuda de familiar ou pessoa de confiança.

**Dores e Necessidades:**

- Dificuldade em articular ideias e transformá-las em conteúdo estruturado
- Não sabe como se posicionar estrategicamente nas redes sociais
- Dificuldade de interpretar a relevância de suas ações legislativas para comunicar à população
- Não consegue manter frequência e consistência na produção de conteúdo
- Receio de cometer erros que possam prejudicar imagem ou mandato

**Comportamento Digital:**

Utiliza principalmente smartphone. Familiaridade básica com WhatsApp, Facebook e Instagram. Preferência por interfaces simples e diretas. Baixa tolerância para complexidade. Necessita de orientação clara sobre o que fazer em cada etapa.

**Objetivos com o Produto:**

Conseguir produzir conteúdo de qualidade rapidamente. Entender como comunicar suas ações de forma estratégica. Manter presença regular nas redes sociais sem investir tempo excessivo.

---

## Funcionalidades do Produto

### Tipos de Conteúdo Produzidos

O sistema produz os seguintes formatos, adaptados ao canal e tipo de ato selecionados:

#### MVP

- **Publicações para Redes Sociais:** Instagram (post único, carrossel, quiz, stories), Facebook, LinkedIn

#### Pós-MVP

- **Releases:** Textos informativos estruturados para imprensa local
- **Roteiros de Vídeo:** Scripts para Reels, TikTok, YouTube
- **Artigos:** Textos longos para mídia impressa ou digital
- **Discursos:** Redação completa para tribuna, eventos, comissões
- **Resumos Estratégicos:** Preparação para entrevistas e programas
- **Biografia:** Construção de biografia profissional estruturada

### Atos de Mandato Contemplados

- Votações
- Mobilização Social
- Requerimento ao Executivo
- Fiscalização
- Tribuna
- Leis
- Atendimento de Gabinete
- Orçamento
- Eventos, Reuniões, Viagens Oficiais
- Prestação de Contas
- Emendas

### Canais de Comunicação Suportados

- Post para Instagram ou Facebook
- Reels
- Stories
- Quiz
- TikTok
- LinkedIn
- Conteúdo para site institucional
- Roteiro para YouTube

*Nota: O MVP foca na geração de conteúdo textual e roteiros. Geração de imagens, vídeos ou edição de mídia estão fora do escopo inicial.*

---

## Jornada do Usuário e Fluxos

### Onboarding Inicial

**Etapas:**

1. Criação de conta (email, senha, dados básicos)
2. Aceite de termos de uso (conformidade LGPD, responsabilidade sobre conteúdo gerado, uso de IA)
3. Tutorial interativo explicando: conceito de DNA, processo de geração de conteúdo, papel dos atos de mandato e canais
4. Convite para preenchimento de DNA com explicação clara sobre benefícios da personalização
5. Direcionamento para geração do primeiro conteúdo

**Tempo Estimado:** 5 a 10 minutos antes do preenchimento de DNA.

### Construção de DNA

**Formato:** Formulário modal apresentado em blocos progressivos. Cada bloco agrupa perguntas relacionadas e é salvo imediatamente no banco de dados ao ser concluído, permitindo retomada posterior.

**Blocos do DNA:**

1. **Identidade:**
   - Nome (completo ou como prefere ser chamado em público)
   - Mandato (1º ou reeleição)
   - História curta (3 a 8 linhas)
   - Estrutura familiar (opcional) (casado, pai de dois filhos, mora no bairro X)
   - Religião (opcional) (católico, evangélico, espírita, sem religião)

2. **Postura e ideias:**
   - Ideologia (liberal/social/conservador/indefinida)
   - Posição ante a gestão (oposição/situação/neutro)

3. **Território e temas:**
   - Cidade (nome oficial) (São José dos Campos, SP)
   - Bairros-alvo (1 ou mais) (Jardim Paulista, Centro, Vila Maria)
   - Regiões (Zona Norte, Sul, Leste, Oeste, Centro)
   - Até 3 temas prioritários (esporte, educação, saúde)

4. **Públicos e objetivos:**
   - Segmentos-chave (jovens 15-24, mães, professores, atletas, comerciantes, idosos)
   - Objetivos de comunicação, de 1 a 3 objetivos (explicar trabalho, ampliar base, combater boatos, organizar reeleição, etc.)

5. **Tempo e equipe:**
   - Quantas horas por semana planeja se dedicar ao mandato? (10 a 14 horas, 8 a 12 horas)
   - Como é formada a estrutura de sua equipe? (sozinho, uma pessoa, duas pessoas, mais que duas)

6. **Canais e contatos:**
   - Quais os seus canais ativos (Instagram, Facebook, YouTube, WhatsApp, Site)
   - Qual seu canal prioritário? (Instagram, Facebook, YouTube, WhatsApp, Site)
   - WhatsApp (opcional) ((11) 91234-5678)
   - E-mail (opcional) (vereadorjoao@email.com)

7. **Frequência e planejamento:**
   - Qual a sua frequência de publicações por rede? (Instagram - 3x por semana; Facebook - diário; YouTube - quinzenal)
   - Você possui planejamento semanal de conteúdo? Se sim, qual seu planejamento? (segundas para agenda, quartas para ações, sextas para resultados)

8. **Engajamento, resposta e integração:**
   - Qual seu percentual médio de respostas a comentários? (40%, 60%, 80%)
   - Qual o tempo médio de resposta em horas **desde o recebimento do comentário**? (2h, 6h, 24h)
   - Você faz interação com outros perfis? Como são essas interações? (sim, com cidadãos e páginas locais / não, raramente)
   - Você faz integração entre os canais (ex.: link na bio levando ao WhatsApp, site, newsletter etc.)

9. **Prova de trabalho e transparência:**
   - Você faz publicação de votações, requerimentos, fiscalizações, emendas, prestação de contas, etc? (sim, semanalmente / não, ainda não)
   - Você faz prestação de contas recorrente? (resumo semanal, boletim mensal, etc)

10. **Biblioteca de mídia:**
    - Você possui boas fotos? (Boa iluminação, enquadramento, etc)
    - Faz vídeos tipo "b-roll"? (Captações complementares, imagens de apoio)
    - E vinhetas com identidade visual? (Abertura e fechamento com logo, etc)

11. **Identidade visual e linguagem:**
    - Você mantém padrões visuais consistentes? (cores, fontes, logotipo)
    - Faz uso de linguagem padronizada do mandato? (tom, vocabulário, hashtags fixas)

12. **Base de contatos:**
    - Você possui base própria de contatos? (não comprada) (sim, coletada em eventos e formulários / não tenho ainda)
    - Qual o número de contatos ativos no WhatsApp? (350)
    - E no e-mail? (500)

13. **Conformidade e riscos jurídicos:**
    - Os seus contatos foram obtidos com autorização? (formulário de inscrição, QR code com formulário)
    - Você faz uso de base comprada? (não, sim)

14. **Observações finais:**
    - Esse espaço é livre para comentários, pendências ou anotações (opcional)

**Indicador de Progresso:** Percentual de conclusão visível durante todo o preenchimento.

**Características:**
- Preenchimento é opcional mas fortemente recomendado
- Pode ser feito parcialmente e retomado a qualquer momento
- Pode ser editado posteriormente através do perfil do usuário
- Cada salvamento de bloco atualiza imediatamente o banco de dados

### Fluxo Principal - Geração de Conteúdo

**Passo 1: Tela inicial**

Usuário acessa tela principal e seleciona botão "Iniciar Comunicação".

**Passo 2: Seleção de Ato de Mandato**

Tela apresenta blocos visuais representando cada tipo de ato de mandato. Usuário seleciona um ato.

**Passo 3: Seleção de Canais**

Tela apresenta blocos visuais representando cada tipo de canal de comunicação. Usuário pode selecionar múltiplos canais simultaneamente.

**Passo 4: Preenchimento de Formulário Específico**

Sistema apresenta modal com formulário em blocos contendo perguntas específicas sobre o ato selecionado.

**Passo 5: Confirmação**

Sistema exibe resumo: "Você escolheu falar sobre [ato X] nos canais [A, B, C]. Vamos gerar o melhor conteúdo possível para você."

**Passo 6: Geração**

Sistema exibe mensagens de feedback durante geração com tempo estimado de 1 a 3 minutos:
- Analisando seu perfil e preferências...
- Pensando na melhor forma de comunicar...
- Gerando conteúdo personalizado...
- Finalizando os detalhes...

**Passo 7: Apresentação do Conteúdo**

Sistema apresenta duas versões do conteúdo para cada canal com botões de copiar e seleção de preferência.

**Passo 8: Sugestões**

Sistema apresenta sugestões de próximos atos ou canais.

**Passo 9: Integração Contínua**

Usuário pode interagir continuamente via texto ou áudio para ajustes.

### Gestão de Rascunhos

Sistema salva automaticamente formulários incompletos. Na tela inicial, área de rascunhos permite retomar preenchimento de onde parou.

### Gestão de Histórico

Conversas completas são salvas no histórico. Na tela inicial, área de histórico permite retornar a qualquer conversa anterior e continuar interagindo.

---

## Interface e Design

### Princípios de Design

**Mobile-First:** Todo o produto é concebido primariamente para uso em smartphone.

**Simplicidade Extrema:** Interface evita complexidade. Uma ação principal por tela sempre que possível.

**Feedback Constante:** Usuário sempre sabe em que etapa está, o que precisa fazer e o que está acontecendo.

**Acessibilidade:** Fontes legíveis, contraste suficiente, botões grandes, linguagem clara.

### Identidade Visual

**Paleta de Cores:**
- Verde principal: #36BE72
- Verde apoio 1: #0E8A45
- Verde apoio 2: #015242
- Preto apoio: #000B05
- Branco apoio: #F1F2F1

**Tipografia:** Montserrat (sans-serif, redonda)

**Componentes Visuais:** Blocos com cantos arredondados, espaçamento generoso, ícones simples

### Estrutura da Tela Inicial

**Header:** Nome da aplicação "Eu Vereador AI"

**Área de Perfil:** Botão de perfil com acesso a DNA, senha, dados, logout

**Área de Ação Principal:** Botão "Iniciar Comunicação"

**Área de DNA:** Bloco "Construir Biografia" com indicador de progresso

**Área de Histórico:** Lista de conversas anteriores

**Área de Rascunhos:** Lista de formulários parciais

**Área de Ferramentas:** Placeholders para funcionalidades futuras

**Footer:** Links para suporte, termos, privacidade

### Navegação

Navegação simples e linear. Breadcrumbs claros. Botão de voltar sempre visível. Menu hamburger para áreas secundárias.

### Estados de Interface

**Loading:** Mensagens contextuais sobre processamento.

**Empty States:** Mensagens amigáveis com call-to-action claro.

**Error States:** Mensagens claras sem jargões técnicos.

---

## Arquitetura Técnica e Integrações

### Visão Geral

A aplicação é composta por:

**Frontend:** Interface mobile-first desenvolvida pela contratada

**Backend:** Sistema de gestão de usuários, autenticação, bancos de dados

**Sistema de IA:** API proprietária fornecida (endpoints detalhados abaixo)

### Endpoints de Integração com Sistema de IA

#### Endpoint de Geração de Conteúdo

**POST /api/chat**

*Request Body:*
```json
{
  "user_id": "string",
  "message": "string",
  "ato_mandato": "string",
  "canais": ["string"],
  "conversation_id": "string"
}
```

*Response:*
```json
{
  "conversation_id": "string",
  "versao_a": {"conteudo": "string"},
  "versao_b": {"conteudo": "string"},
  "sugestoes": ["string"]
}
```

*Tempo de resposta:* 1-3 minutos

#### Endpoint de Feedback de Preferência

**POST /api/feedback**

*Request Body:*
```json
{
  "conversation_id": "string",
  "versao_a": "string",
  "versao_b": "string",
  "versao_preferida": "a" | "b"
}
```

*Response:* 204 No Content

#### Endpoint de Transcrição de Áudio

**POST /api/transcribe**

*Request:* Multipart/form-data com arquivo de áudio (mp3, wav, m4a, máximo 5 minutos)

*Response:*
```json
{
  "texto": "string"
}
```

*Tempo de resposta:* < 10 segundos

#### Endpoint de Consulta de Uso

**GET /api/usage/{user_id}**

*Response:*
```json
{
  "user_id": "string",
  "percentual_usado": 75.83,
  "proxima_renovacao": "2025-11-01T00:00:00Z"
}
```

### Responsabilidades da Contratada

**Frontend:**
- Interface completa mobile-first conforme design especificado
- Todas as telas e fluxos descritos no documento
- Integração com endpoints fornecidos
- Tratamento de estados de loading, erro e sucesso
- Gravação de áudio no frontend

**Backend:**
- Sistema de autenticação e autorização
- Geração e gestão de tokens de usuário
- Bancos de dados
- Sistema de assinatura e pagamentos
- Gestão de rascunhos e histórico

**Bancos de Dados a serem implementados:**

1. **Banco de Usuários:** Dados de cadastro, autenticação, assinatura, token
2. **Banco de DNA:** Perfil completo, versionamento, atualizações incrementais
3. **Banco de Rascunhos:** user_id, ato_tipo, canais, respostas parciais, timestamp
4. **Banco de Histórico:** user_id, conversation_id, ato_tipo, canais, formulário, mensagens, timestamp

### Stack Tecnológico Sugerido

**Frontend:** React, Vue.js, Next.js, Angular com TailwindCSS

**Backend:** Node.js, Python (Django/FastAPI) ou similar com Supabase e JWT

**Hosting:** Digital Ocean com SSL/HTTPS obrigatório

**Pagamento:** Asaas para assinaturas recorrentes

### Requisitos de Segurança

- Comunicação via HTTPS
- Tokens com expiração
- Validação de inputs
- Proteção contra SQL injection

---

## Casos de Uso Detalhados

### Caso de Uso: Prestação de Contas Mensal

**Ator:** Vereador João, primeiro mandato, atua em bairros periféricos, foco em saúde pública.

**Fluxo:**

1. João acessa aplicação no smartphone
2. Clica em "Iniciar Comunicação"
3. Seleciona ato "Prestação de Contas"
4. Seleciona canais: Post Instagram, Post Facebook, Stories
5. Preenche formulário respondendo perguntas sobre o período e ações realizadas
6. Sistema confirma e inicia geração (frontend exibe loading com mensagens de feedback)
7. Frontend recebe do endpoint duas versões para cada canal
8. João lê ambas versões do post Instagram, prefere a versão B
9. João seleciona versão B, frontend envia feedback para endpoint correspondente
10. João copia conteúdo
11. Sistema sugere próximos atos de mandato

**Resultado:** João conseguiu comunicar suas atividades em menos de 10 minutos.

### Caso de Uso: Posicionamento Urgente sobre Votação

**Ator:** Vereadora Maria, reeleição, posicionamento de oposição.

**Contexto:** Maria precisa comunicar posição sobre votação polêmica rapidamente.

**Fluxo:**

1. Maria acessa aplicação
2. Entra em "Iniciar Comunicação"
3. Seleciona ato "Votações"
4. Seleciona canais: Stories, Post Facebook
5. Preenche formulário sobre o projeto e seu posicionamento
6. Sistema gera conteúdo
7. Maria revisa e percebe que está muito técnico
8. Usa área de interação com áudio: grava "quero uma linguagem mais popular"
9. Frontend envia áudio para endpoint de transcrição
10. Frontend envia texto transcrito + conversation_id para endpoint de chat
11. Maria aprova e publica

**Resultado:** Em menos de 7 minutos, Maria conseguiu comunicar posicionamento claro.

### Caso de Uso: Usuário Sem DNA Preenchido

**Ator:** Vereador Carlos, novo usuário, ainda não preencheu DNA.

**Fluxo:**

1. Carlos cria conta
2. Sistema sugere preenchimento de DNA, mas oferece opção "Fazer depois"
3. Carlos escolhe fazer depois
4. Inicia geração de conteúdo sobre fiscalização
5. Sistema gera conteúdo genérico mas funcional
6. Após copiar, sistema mostra mensagem incentivando preenchimento de DNA

**Resultado:** Produto entrega valor imediato, mas incentiva personalização.

---

## Requisitos Não-Funcionais

### Usabilidade

- Usuário deve conseguir gerar primeiro conteúdo em até 15 minutos
- Toda interface em português brasileiro
- Ausência de anglicismos ou jargões técnicos

### Confiabilidade

- Sistema não perde dados do usuário
- Salvamento automático de rascunhos
- Possibilidade de retomada após erros de conexão

### Conformidade Legal

- **LGPD:** Conformidade total, consentimento explícito, visualização/edição/exclusão de dados, dados não compartilhados.
- **Termos de Uso:** Documento detalhando IA, responsabilidade exclusiva do usuário.

---

## Critérios de Aceitação do MVP

### Funcionalidades Implementadas

- Sistema de cadastro e autenticação funcional
- Termos de uso com aceite obrigatório
- Onboarding com tutorial interativo completo
- Formulário de DNA em blocos com todos os campos
- Indicador de progresso de DNA funcionando
- Salvamento progressivo de blocos de DNA
- Fluxo completo de geração de conteúdo
- Seleção múltipla de canais funcionando
- Formulários específicos por tipo de ato
- Integração com endpoints de IA funcionando
- Apresentação de duas versões de conteúdo
- Botão de copiar funcionando
- Sistema de feedback de preferência
- Interação contínua via texto funcionando
- Entrada por áudio com transcrição
- Histórico salvando conversas
- Rascunhos salvando formulários parciais
- Área de perfil com visualização e edição de DNA
- Sistema de notificação de limite de uso
- Interface mobile-first responsiva
- Identidade visual aplicada consistentemente
- Sistema de pagamento/assinatura funcional

### Qualidade e Performance

- Interface responsiva em dispositivos móveis
- Navegação intuitiva validada com usuários

### Testes Realizados

- Testes funcionais de todos os fluxos principais
- Testes de segurança básicos
- Testes de carga (50 usuários simultâneos)
- Validação de conformidade LGPD

### Documentação

- Termos de uso revisados juridicamente
- Política de privacidade completa
- Documentação técnica de integração
- Vídeos tutoriais produzidos

---

## Escopo Detalhado de Desenvolvimento

### Incluído no MVP

**Telas e Interfaces:**
- Tela de login/cadastro
- Tela de onboarding com tutorial interativo
- Tela inicial (dashboard)
- Tela de seleção de ato de mandato
- Tela de seleção de canais
- Modal de formulários específicos (11 formulários)
- Modal de formulário de DNA (12 blocos)
- Tela de chat/geração de conteúdo
- Tela de perfil do usuário
- Tela de histórico de conversas
- Tela de rascunhos
- Tela de gerenciamento de conta/assinatura

**Funcionalidades Principais:**
- Sistema completo de autenticação
- Gestão de perfil e DNA
- Fluxo completo de geração de conteúdo
- Sistema de rascunhos com salvamento automático
- Sistema de histórico de conversas
- Integração com endpoints de IA
- Sistema de feedback de preferência
- Entrada de texto e áudio
- Sistema de notificação de uso/limite
- Sistema de assinatura e pagamentos
- Área de ferramentas futuras (placeholder)

### Integrações Necessárias

- Endpoints de IA fornecidos
- Gateway de pagamento Asaas
- Serviço de email transacional

---

## Entregáveis Esperados

### Código e Repositórios

- Código fonte completo frontend e backend
- Repositórios Git com histórico
- README com instruções
- Documentação de variáveis de ambiente

### Documentação Técnica

- Documentação da arquitetura implementada
- Diagrama de banco de dados
- Documentação de integração com endpoints

### Testes

- Cobertura de testes unitários (mínimo 60%)
- Testes de integração dos fluxos principais
- Documentação de casos de teste manuais
- Relatório de testes de usabilidade

### Assets e Design

- Todos os assets visuais (ícones, imagens, logos)
- Guia de estilo implementado
- Componentes reutilizáveis documentados

---

## Segurança

- HTTPS obrigatório
- Headers de segurança configurados
- Validação de inputs no backend
- Proteção contra CSRF
- Rate limiting implementado
- Senhas hasheadas com bcrypt ou similar
- Tokens JWT com expiração

---

## Suporte Pós-Lançamento

### Período de Garantia

Esperamos que a contratada ofereça período de garantia para:

- Correção de bugs críticos
- Ajustes de funcionalidades entregues
- Suporte técnico para resolução de problemas

---

## Informações para Orçamento

### O que Incluir na Proposta

**Orçamento Detalhado:**
- Custo de desenvolvimento
- Custos de terceiros (se houver)
- Impostos e taxas

**Cronograma Detalhado:**
- Timeline completo do projeto
- Marcos de entrega

**Metodologia:**
- Processo de desenvolvimento
- Frequência de reuniões
- Ferramentas de gestão
- Processo de QA

**Premissas e Exclusões:**
- O que está incluído no orçamento
- O que está explicitamente excluído
- Condições para mudanças de escopo

### Informações Adicionais Disponíveis

Mediante solicitação, podemos fornecer:

- **Telas de referência:** Forneceremos mockups/wireframes das principais telas que servirão como base conceitual para o produto.

**IMPORTANTE: Estas telas são apenas referência inicial. A contratada deverá aprimorar significativamente o design visual, a experiência do usuário e os detalhes de interface para o lançamento do produto final.** Esperamos evolução substancial da proposta visual apresentada.

- Schemas JSON completos dos bancos de dados
- Exemplos de respostas dos endpoints de IA
- Documentação completa da API de IA

---

## Contatos e Dúvidas

Para esclarecimentos sobre este documento ou sobre o projeto, favor entrar em contato:

**Projeto:** Eu Vereador AI

**Contato:** [WhatsApp Diego](wa.me/+5561996841987)

---

**Versão do Documento**

Versão: 1.0 - Orçamento  
Data: 30 de outubro de 2025  
Autor: Equipe Eu Vereador AI  
Status: Para Orçamento

*Este documento foi preparado especificamente para fins de orçamento. Informações técnicas proprietárias sobre implementação interna de IA foram intencionalmente omitidas. A contratada receberá documentação complementar detalhada dos endpoints de integração.*