# Product Requirements Document (PRD)

## Eu Vereador AI - Assistente de Comunicação para Vereadores

**Versão:** 1.0  
**Data:** 28 de outubro de 2025  
**Status:** MVP em Desenvolvimento  
**Documento:** Versão para Orçamento

---

## 1. Visão Executiva

### 1.1 Contexto e Problema

Vereadores brasileiros enfrentam desafios significativos na comunicação com seus eleitores. A maioria dos vereadores municipais possui renda mensal de aproximadamente R$ 4.000,00, não dispõe de assessores de comunicação e muitas vezes não possui ensino médio completo. Essa combinação de recursos limitados e baixa escolaridade resulta em dificuldade para interpretar demandas, desenvolver ideias de comunicação e produzir conteúdo estratégico para prestação de contas e engajamento com a população.

### 1.2 Proposta de Solução

Eu Vereador AI é uma plataforma de inteligência artificial que auxilia vereadores na produção de conteúdo de comunicação personalizado, estratégico e adequado ao contexto específico de cada mandato. A solução utiliza sistema proprietário de IA para gerar conteúdo para diversos canais (redes sociais, discursos, artigos, releases) baseado em informações estruturadas sobre o perfil político, ideológico e geográfico do vereador.

A personalização é alcançada através de um perfil detalhado chamado DNA, que captura desde informações básicas (nome, cidade, mandato) até aspectos estratégicos (ideologia, posicionamento em relação à gestão, bairros-alvo, temas prioritários). O sistema aprende continuamente com as preferências do usuário, refinando o estilo e o tom dos conteúdos gerados ao longo do tempo.

### 1.3 Proposta de Valor Única

O Eu Vereador AI diferencia-se por combinar três elementos fundamentais: personalização profunda baseada no contexto político e geográfico do mandato, aplicação de metodologia comprovada de comunicação política desenvolvida por Marcelo Vitorino (especialista com mais de 20 anos de experiência) e interface simplificada focada em mobile-first para atender usuários com baixa familiaridade tecnológica.

### 1.4 Validação Preliminar

Um protótipo do conceito foi testado como custom GPT com vereadores que participaram de curso promovido pela equipe. O protótipo registrou mais de 90 utilizações em menos de um mês, validando a demanda e o interesse pelo tipo de solução proposta. O feedback geral dos usuários foi positivo, embora tenha sido identificada como principal objeção a dificuldade de uso, o que reforça a necessidade de investimento em interface intuitiva e onboarding estruturado.

---

## 2. Objetivos de Negócio e Métricas de Sucesso

### 2.1 Objetivos do MVP

O MVP tem três objetivos principais que definirão seu sucesso:

**Objetivo 1: Validação de Adoção**  
Alcançar 100 usuários mensais ativos que utilizem regularmente a plataforma para geração de conteúdo.

**Objetivo 2: Validação de Retenção**  
Manter baixo índice de churn, demonstrando que o produto entrega valor contínuo e se torna ferramenta recorrente na rotina de comunicação dos vereadores.

**Objetivo 3: Validação de Interesse em Evolução**  
Identificar interesse manifestado pelos usuários nas ferramentas futuras (Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais).

### 2.2 Métricas Quantitativas Primárias

- **Usuários Ativos Mensais (MAU):** Meta mínima: 100 MAU
- **Taxa de Retenção Mensal:** Indicador crítico de product-market fit

### 2.3 Métricas Quantitativas Secundárias

- **Tempo até Primeiro Valor:** Meta: 15 minutos com preenchimento de DNA, 5 minutos sem preenchimento
- **Conteúdos Gerados por Usuário por Mês**
- **Taxa de Conclusão de DNA**
- **Taxa de Feedback de Preferência**
- **Cliques em Sugestões de Ferramentas Futuras**

### 2.4 Modelo de Monetização

Modelo de assinatura recorrente mensal no valor de R$ 300,00 por usuário. O sistema implementa limitador de uso baseado em custos operacionais internos, com notificações ao usuário quando aproximar-se do limite mensal.

---

## 3. Personas e Segmentação

### 3.1 Persona Primária - MVP

#### Vereador Municipal de Recursos Limitados

**Demografia:**  
Homem ou mulher, idade entre 35 e 55 anos, residente em cidade de pequeno ou médio porte no interior brasileiro. Renda mensal de aproximadamente R$ 4.000,00. Escolaridade até ensino médio incompleto ou completo.

**Contexto Profissional:**  
Primeiro ou segundo mandato. Não possui assessores de comunicação. Gerencia suas redes sociais pessoalmente ou com ajuda de familiar ou pessoa de confiança.

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

## 4. Funcionalidades do Produto

### 4.1 Tipos de Conteúdo Produzidos

O sistema produz os seguintes formatos, adaptados ao canal e tipo de ato selecionados:

- **Releases:** Textos informativos estruturados para imprensa local
- **Publicações para Redes Sociais:** Instagram (post único, carrossel, quiz, stories), Facebook, LinkedIn
- **Roteiros de Vídeo:** Scripts para Reels, TikTok, YouTube
- **Artigos:** Textos longos para mídia impressa ou digital
- **Discursos:** Redação completa para tribuna, eventos, comissões
- **Resumos Estratégicos:** Preparação para entrevistas e programas
- **Biografia:** Construção de biografia profissional estruturada

### 4.2 Atos de Mandato Contemplados

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

### 4.3 Canais de Comunicação Suportados

- Post para Instagram ou Facebook
- Reels
- Stories
- TikTok
- Conteúdo para site institucional
- Roteiro para YouTube

*Nota: O MVP foca na geração de conteúdo textual e roteiros. Geração de imagens, vídeos ou edição de mídia estão fora do escopo inicial.*

---

## 5. Jornada do Usuário e Fluxos

### 5.1 Onboarding Inicial

**Etapas:**

1. Criação de conta (email, senha, dados básicos)
2. Aceite de termos de uso (conformidade LGPD, responsabilidade sobre conteúdo gerado, uso de IA)
3. Tutorial interativo explicando: conceito de DNA, processo de geração de conteúdo, papel dos atos de mandato e canais
4. Convite para preenchimento de DNA com explicação clara sobre benefícios da personalização
5. Direcionamento para geração do primeiro conteúdo

**Tempo Estimado:** 5 a 10 minutos antes do preenchimento de DNA.

### 5.2 Construção de DNA

**Formato:** Formulário modal apresentado em blocos progressivos. Cada bloco agrupa perguntas relacionadas e é salvo imediatamente no banco de dados ao ser concluído, permitindo retomada posterior.

**Blocos do DNA:**

**Bloco 1 - Identificação Básica:**
- Nome completo
- Cidade de atuação
- Mandato (primeiro mandato ou reeleição)
- Contatos (WhatsApp, email)

**Bloco 2 - Perfil Pessoal:**
- História curta (trajetória até a política)
- Estrutura familiar
- Religião

**Bloco 3 - Posicionamento Político:**
- Ideologia (liberal, social, conservador, indefinida)
- Posicionamento em relação à gestão atual (oposição, situação, neutro)

**Bloco 4 - Atuação Territorial:**
- Bairros-alvo (múltipla seleção)
- Regiões de atuação
- Segmentos da população com maior afinidade

**Bloco 5 - Agenda Temática:**
- Temas prioritários do mandato (mínimo 1, máximo 3)
- Segmentos-chave de atuação
- Objetivos de comunicação

**Bloco 6 - Estrutura e Canais:**
- Tempo semanal disponível para comunicação (em horas)
- Estrutura de equipe (sozinho, 1 pessoa, 2-3 pessoas, mais de 3)
- Canais ativos (Instagram, Facebook, YouTube, WhatsApp, Email)
- Rede prioritária

**Bloco 7 - Frequência e Planejamento:**
- Frequência de publicação semanal por rede
- Se planeja conteúdo semanalmente
- Se há integração entre canais

**Bloco 8 - Engajamento:**
- Percentual de comentários que responde
- Tempo médio de resposta a comentários (em horas)
- Se interage com outros perfis nas redes sociais

**Bloco 9 - Prestação de Contas e Transparência:**
- Prova de trabalho publicada
- Se prestação de contas é recorrente

**Bloco 10 - Recursos de Produção:**
- Biblioteca de mídia disponível
- Base própria de contatos

**Bloco 11 - Padronização:**
- Se possui padrões visuais consistentes
- Se possui linguagem padronizada

**Bloco 12 - Conformidade:**
- Riscos jurídicos
- Observações gerais

**Indicador de Progresso:** Percentual de conclusão visível durante todo o preenchimento.

**Características:**
- Preenchimento é opcional mas fortemente recomendado
- Pode ser feito parcialmente e retomado a qualquer momento
- Pode ser editado posteriormente através do perfil do usuário
- Cada salvamento de bloco atualiza imediatamente o banco de dados

### 5.3 Fluxo Principal - Geração de Conteúdo

**Passo 1: Tela Inicial**  
Usuário acessa tela principal e seleciona botão "Iniciar Comunicação".

**Passo 2: Seleção de Ato de Mandato**  
Tela apresenta blocos visuais representando cada tipo de ato de mandato. Usuário seleciona um ato.

**Passo 3: Seleção de Canais**  
Tela apresenta blocos visuais representando cada tipo de canal de comunicação. Usuário pode selecionar múltiplos canais simultaneamente.

**Passo 4: Preenchimento de Formulário Específico**  
Sistema apresenta modal com formulário em blocos contendo perguntas específicas sobre o ato selecionado. As perguntas variam conforme o tipo de ato. Cada bloco é salvo como rascunho automaticamente.

**Passo 5: Confirmação**  
Sistema exibe resumo: "Você escolheu falar sobre [ato X] nos canais [A, B, C]. Vamos gerar o melhor conteúdo possível para você."

**Passo 6: Geração**  
Enquanto o conteúdo está sendo gerado, sistema exibe mensagens de feedback:
- "Analisando seu perfil e preferências..."
- "Pensando na melhor forma de comunicar..."
- "Gerando conteúdo personalizado..."
- "Finalizando os detalhes..."

Tempo estimado: 1 a 3 minutos.

**Passo 7: Apresentação do Conteúdo**  
Sistema apresenta duas versões do conteúdo para cada canal selecionado. Para cada versão há:
- Botão de copiar
- Visualização formatada do conteúdo
- Botão para selecionar como versão preferida

Após seleção da versão preferida, feedback é enviado ao sistema para aprendizado.

**Passo 8: Sugestões**  
Sistema apresenta sugestões: "Gostaria de criar um [outro ato de mandato]?" e "Gostaria de publicar em [outro canal]?"

**Passo 9: Interação Contínua**  
Usuário pode interagir com o conteúdo gerado através de área de texto ou gravação de áudio:
- Solicitar ajustes de tom
- Pedir para trocar palavras específicas
- Solicitar foco maior em determinado tópico
- Pedir versão mais curta ou mais longa
- Solicitar adaptação para outro canal

Cada interação gera nova resposta mantendo contexto da conversa.

### 5.4 Gestão de Rascunhos

Sempre que usuário está preenchendo formulário de ato de mandato e interrompe o processo antes de concluir, o sistema salva automaticamente como rascunho. Na tela inicial, área de rascunhos permite retomar o preenchimento exatamente de onde parou.

### 5.5 Gestão de Histórico

Sempre que conteúdo é efetivamente gerado, a conversa completa é salva no histórico. Na tela inicial, área de histórico permite retornar a qualquer conversa anterior e continuar interagindo.

---

## 6. Interface e Design

### 6.1 Princípios de Design

**Mobile-First:** Todo o produto é concebido primariamente para uso em smartphone. A interface desktop é adaptação da versão mobile. Elementos de interface, tamanho de botões, espaçamento e navegação são otimizados para telas pequenas e interação touch.

**Simplicidade Extrema:** Interface evita complexidade. Uma ação principal por tela sempre que possível. Fluxos lineares e claros. Ausência de jargões técnicos.

**Feedback Constante:** Usuário sempre sabe em que etapa está, o que precisa fazer e o que está acontecendo. Indicadores de progresso visíveis. Mensagens claras durante processamento.

**Acessibilidade:** Fontes legíveis em tamanhos adequados. Contraste suficiente entre texto e fundo. Botões grandes o suficiente para toque preciso. Linguagem clara e direta.

### 6.2 Identidade Visual

**Paleta de Cores:**
- Verde principal: #36be72 (ações primárias, destaques positivos)
- Verde apoio 1: #0e8a45 (hover states, elementos secundários)
- Verde apoio 2: #015242 (backgrounds sutis, bordas)
- Preto apoio: #000b05 (textos principais, elementos de alta hierarquia)
- Branco apoio: #f1f2f1 (backgrounds, textos sobre fundos escuros)

**Tipografia:**
- Família: Montserrat (sans-serif, redonda)
- Uso: Clara, legível, moderna e profissional

**Componentes Visuais:**
- Blocos com cantos arredondados
- Espaçamento generoso entre elementos
- Ícones simples e universalmente compreensíveis
- Botões com estados visuais claros (normal, hover, pressed, disabled)

### 6.3 Estrutura da Tela Inicial

**Header:**
- Nome da aplicação centralizado no topo: "Eu Vereador AI"

**Área de Perfil:**
- Botão de perfil (ícone de usuário) posicionado no canto superior
- Ao clicar, acesso a: visualização e edição de DNA, alteração de senha, dados da conta, logout

**Área de Ação Principal:**
- Botão destacado "Iniciar Comunicação"
- Redireciona para tela de seleção de atos de mandato

**Área de DNA:**
- Bloco dedicado "Construir Biografia"
- Indicador de percentual de conclusão do DNA
- Redireciona para formulário de DNA em modal

**Área de Ferramentas (Placeholder):**
- Bloco dedicado "Ferramentas"
- Botões para: Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais
- Visual indica que são funcionalidades futuras (ícones com indicação "Em breve")
- Botões desabilitados mas visíveis para criar expectativa

**Área de Histórico:**
- Bloco com lista de conversas anteriores
- Ao clicar, retorna ao chat de onde parou com contexto preservado

**Área de Rascunhos:**
- Bloco com lista de formulários parcialmente preenchidos
- Ao clicar, retorna ao preenchimento com informações já inseridas preservadas

**Footer:**
- Links para suporte, termos de uso, política de privacidade

### 6.4 Navegação

Navegação simples e linear. Breadcrumbs ou indicação clara de onde usuário está no fluxo. Botão de voltar sempre visível. Menu hamburger para acesso a áreas secundárias.

### 6.5 Estados de Interface

**Loading:**  Mensagens contextuais sobre o que está acontecendo.

**Empty States:** Mensagens amigáveis quando não há histórico, rascunhos ou DNA preenchido, com call-to-action claro.

**Error States:** Mensagens claras sobre erros, sem jargões técnicos, com sugestão de próximos passos.

---

## 7. Arquitetura Técnica e Integrações

### 7.1 Visão Geral

A aplicação é composta por:
- **Frontend:** Interface mobile-first desenvolvida pela software house
- **Backend:** Sistema de gestão de usuários, autenticação, bancos de dados desenvolvido pela software house
- **Sistema de IA:** API proprietária que será fornecida (endpoints de integração detalhados abaixo)

### 7.2 Endpoints de Integração com Sistema de IA

A software house deverá integrar com os seguintes endpoints que serão fornecidos:

#### 7.2.1 Endpoint de Geração de Conteúdo

**POST /api/chat**

**Headers:**
```
Authorization: Bearer {token_do_usuario}
Content-Type: application/json
```

**Request Body:**
```json
{
  "user_id": "string",
  "message": "string",
  "ato_mandato": "string",
  "canais": ["string"],
  "conversation_id": "string (para memória e histórico)"
}
```

**Response:**
```json
{
  "conversation_id": "string",
  "versao_a": {
    "conteudo": "string",
  },
  "versao_b": {
    "conteudo": "string",
  },
  "sugestoes": ["string"]
}
```

**Tempo de resposta esperado:** 1-3 minutos

#### 7.2.2 Endpoint de Feedback de Preferência

**POST /api/feedback**

**Headers:**
```
Authorization: Bearer {token_do_usuario}
Content-Type: application/json
```

**Request Body:**
```json
{
  "conversation_id": "string",
  "versao_a": "string",
  "versao_b": "string",
  "versao_preferida": "a" | "b"
}
```

**Response:** 204 No Content

#### 7.2.3 Endpoint de Transcrição de Áudio

**POST /api/transcribe**

**Headers:**
```
Authorization: Bearer {token_do_usuario}
Content-Type: multipart/form-data
```

**Request Body:**
```
audio: File (formato: mp3, wav, m4a | máximo: 5 minutos)
```

**Response:**
```json
{
  "texto": "string"
}
```

**Tempo de resposta esperado:** < 10 segundos

#### 7.2.4 Endpoint de Consulta de Uso

**GET /api/usage/{user_id}**

**Headers:**
```
Authorization: Bearer {token_do_usuario}
```

**Response:**
```json
{
  "user_id": "string",
  "percentual_usado": 75.83,
  "proxima_renovacao": "2025-11-01T00:00:00Z"
}
```

### 7.3 Responsabilidades da Software House

**Frontend:**
- Interface completa mobile-first conforme design especificado
- Todas as telas e fluxos descritos no documento
- Integração com endpoints fornecidos
- Tratamento de estados de loading, erro e sucesso
- Gravação de áudio no frontend 

**Backend:**
- Sistema de autenticação e autorização
- Geração e gestão de tokens de usuário
- Bancos de dados (especificações abaixo)
- Sistema de assinatura e pagamentos
- Gestão de rascunhos e histórico

**Bancos de Dados a serem implementados:**

1. **Banco de Usuários:**
   - Dados de cadastro
   - Autenticação
   - Status de assinatura
   - Token de acesso

2. **Banco de DNA:**
   - Perfil completo do usuário conforme schemas fornecidos
   - Versionamento para histórico de mudanças
   - Atualizações incrementais por bloco

3. **Banco de Rascunhos:**
   - user_id
   - ato_tipo
   - canais selecionados
   - respostas parciais
   - timestamp

4. **Banco de Histórico:**
   - user_id
   - conversation_id
   - ato_tipo
   - canais
   - formulário completo
   - histórico de mensagens
   - timestamp

### 7.4 Stack Tecnológico Sugerido

**Frontend:**
- React, Vue.js, Next.js, Angular
- TailwindCSS para estilização
- Biblioteca de componentes mobile-friendly

**Backend:**
- Node.js, Python (Django/FastAPI) ou similar
- Supabase para bancos de dados
- JWT para autenticação

**Hosting:**
- Servidor cloud Digital Ocean
- SSL/HTTPS obrigatório

**Pagamento:**
- Integração com gateway de pagamento brasileiro Asaas
- Suporte a assinaturas recorrentes

### 7.5 Requisitos de Segurança

- Criptografia de dados sensíveis em repouso
- Comunicação via HTTPS
- Tokens com expiração
- Validação de inputs
- Proteção contra SQL injection, XSS
- Rate limiting em endpoints

### 7.6 Requisitos de Performance

- Tempo de resposta de navegação: < 300ms
- Carregamento de histórico/rascunhos: < 2 segundos
- Upload de áudio: suportar até 10MB
- Interface responsiva em dispositivos móveis (iOS e Android)

---

## 8. Casos de Uso Detalhados

### 8.1 Caso de Uso: Prestação de Contas Mensal

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

### 8.2 Caso de Uso: Posicionamento Urgente sobre Votação

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

### 8.3 Caso de Uso: Usuário Sem DNA Preenchido

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

## 9. Requisitos Não-Funcionais

### 9.1 Usabilidade

- Usuário com baixa familiaridade tecnológica deve conseguir gerar primeiro conteúdo em até 15 minutos
- Toda interface em português brasileiro
- Ausência de anglicismos ou jargões técnicos

### 9.2 Confiabilidade

- Sistema não perde dados do usuário
- Salvamento automático de rascunhos
- Possibilidade de retomada após erros de conexão

### 9.3 Conformidade Legal

**LGPD:**
- Conformidade total com Lei Geral de Proteção de Dados
- Consentimento explícito na criação de conta
- Possibilidade de visualização, edição e exclusão de dados pessoais
- Dados não compartilhados com terceiros

**Termos de Uso:**
- Documento detalhando que conteúdo é gerado por IA
- Responsabilidade do conteúdo é exclusivamente do usuário
- Sistema não se responsabiliza por uso inadequado ou consequências

---

## 10. Critérios de Aceitação do MVP

### 10.1 Funcionalidades Implementadas

- [ ] Sistema de cadastro e autenticação funcional
- [ ] Termos de uso com aceite obrigatório
- [ ] Onboarding com tutorial interativo completo
- [ ] Formulário de DNA em blocos com todos os campos
- [ ] Indicador de progresso de DNA funcionando
- [ ] Salvamento progressivo de blocos de DNA no banco de dados
- [ ] Fluxo completo de geração de conteúdo para todos os atos listados
- [ ] Seleção múltipla de canais funcionando
- [ ] Formulários específicos por tipo de ato implementados
- [ ] Integração com endpoints de IA funcionando
- [ ] Apresentação de duas versões de conteúdo
- [ ] Botão de copiar funcionando em cada versão
- [ ] Sistema de feedback de preferência funcionando
- [ ] Interação contínua via texto funcionando
- [ ] Entrada por áudio com transcrição funcionando
- [ ] Histórico salvando conversas e permitindo retomada
- [ ] Rascunhos salvando formulários parciais e permitindo retomada
- [ ] Área de perfil com visualização e edição de DNA
- [ ] Sistema de notificação de limite de uso
- [ ] Interface mobile-first responsiva em todas as telas
- [ ] Identidade visual aplicada consistentemente
- [ ] Sistema de pagamento/assinatura funcional

### 10.2 Qualidade e Performance

- [ ] Interface responsiva em dispositivos móveis (iPhone, Android)
- [ ] Navegação intuitiva validada com pelo menos 5 usuários representativos

### 10.3 Testes Realizados

- [ ] Testes funcionais de todos os fluxos principais
- [ ] Testes de segurança básicos
- [ ] Testes de carga com simulação de pelo menos 50 usuários simultâneos
- [ ] Validação de conformidade LGPD

### 10.4 Documentação

- [ ] Termos de uso redigidos e revisados juridicamente
- [ ] Política de privacidade completa
- [ ] Documentação técnica de integração com endpoints
- [ ] Vídeos tutoriais de funcionalidades principais produzidos

---

## 11. Escopo Detalhado de Desenvolvimento

### 11.1 Incluído no MVP

**Telas e Interfaces:**
- Tela de login/cadastro
- Tela de onboarding com tutorial interativo
- Tela inicial (dashboard) com todas as áreas especificadas
- Tela de seleção de ato de mandato
- Tela de seleção de canais
- Modal de formulários específicos por ato (11 formulários diferentes)
- Modal de formulário de DNA (12 blocos)
- Tela de chat/geração de conteúdo com apresentação das duas versões
- Tela de perfil do usuário
- Tela de histórico de conversas
- Tela de rascunhos
- Tela de gerenciamento de conta/assinatura

**Funcionalidades Principais:**
- Sistema completo de autenticação (registro, login, recuperação de senha)
- Gestão de perfil e DNA do usuário
- Fluxo completo de geração de conteúdo
- Sistema de rascunhos com salvamento automático
- Sistema de histórico de conversas
- Integração com todos os endpoints de IA fornecidos
- Sistema de feedback de preferência
- Entrada de texto e áudio para interações
- Sistema de notificação de uso/limite
- Sistema de assinatura e pagamentos recorrentes
- Área de ferramentas futuras (placeholder visual)

**Bancos de Dados:**
- Tabela de usuários completa
- Tabela de DNA com todos os campos especificados
- Tabela de rascunhos
- Tabela de histórico de conversas
- Tabela de assinaturas/pagamentos

### 11.2 Explicitamente Fora do MVP

**Não deve ser desenvolvido:**
- Ferramentas extras (Bio, MiniBio, Alinhamento Ideológico, etc.) - apenas placeholders visuais
- Integração direta com redes sociais para publicação automática
- Geração de imagens ou vídeos
- Sistema de colaboração ou múltiplos usuários por conta
- Diferenciação de experiência por tipo de público (assessores, agências)
- Aplicativo mobile nativo (apenas web responsiva)

### 11.3 Integrações Necessárias

- Endpoints de IA fornecidos (chat, feedback, transcrição, uso)
- Gateway de pagamento brasileiro Asaas
- Serviço de envio de email transacional (confirmação de cadastro, recuperação de senha)

---

## 12. Entregáveis Esperados

### 12.1 Código e Repositórios

- Código fonte completo do frontend
- Código fonte completo do backend
- Repositórios Git com histórico de commits
- README com instruções de instalação e configuração
- Documentação de variáveis de ambiente

### 12.2 Documentação Técnica

- Documentação da arquitetura implementada
- Diagrama de banco de dados
- Documentação de APIs internas (se houver)
- Guia de deploy e configuração de ambiente
- Documentação de integração com endpoints externos

### 12.3 Ambientes

- Ambiente de desenvolvimento configurado
- Ambiente de staging/homologação
- Ambiente de produção
- Scripts de deploy automatizado

### 12.4 Testes

- Cobertura de testes unitários (mínimo 60%)
- Testes de integração dos fluxos principais
- Documentação de casos de teste manuais
- Relatório de testes de usabilidade realizados

### 12.5 Assets e Design

- Todos os assets visuais (ícones, imagens, logos)
- Guia de estilo implementado
- Componentes reutilizáveis documentados

---

## 13. Segurança

- HTTPS obrigatório
- Headers de segurança configurados
- Validação de inputs no backend
- Proteção contra CSRF
- Rate limiting implementado
- Senhas hasheadas com bcrypt ou similar
- Tokens JWT com expiração

---

## 14. Suporte Pós-Lançamento

### 14.1 Período de Garantia

Esperamos que a software house ofereça período de garantia para:
- Correção de bugs críticos
- Ajustes de funcionalidades entregues
- Suporte técnico para resolução de problemas

### 14.2 Documentação de Handover

- Documentação completa de código
- Vídeos de explicação da arquitetura
- Sessões de transferência de conhecimento
- Acesso a ambientes de desenvolvimento
- Credenciais e acessos necessários

---

## 15. Informações para Orçamento

### 15.1 O que Incluir na Proposta

**Orçamento Detalhado:**
- Custo por fase de desenvolvimento
- Custo por funcionalidade principal
- Custos de infraestrutura (setup inicial)
- Custos de terceiros (se houver)
- Impostos e taxas

**Cronograma Detalhado:**
- Timeline completo do projeto
- Marcos de entrega
- Dependências críticas
- Buffer para imprevistos

**Equipe Proposta:**
- Composição da equipe
- Experiência dos profissionais
- Alocação de horas por papel
- Disponibilidade

**Metodologia:**
- Processo de desenvolvimento
- Frequência de reuniões
- Ferramentas de gestão
- Processo de QA

**Premissas e Exclusões:**
- O que está incluído no orçamento
- O que está explicitamente excluído
- Condições para mudanças de escopo

### 15.2 Informações Adicionais Disponíveis

Mediante solicitação, podemos fornecer:
- **Telas de referência:** Forneceremos mockups/wireframes das principais telas que servirão como base conceitual para o produto. **IMPORTANTE: Estas telas são apenas referência inicial. A software house deverá aprimorar significativamente o design visual, a experiência do usuário e os detalhes de interface para o lançamento do produto final.** Esperamos evolução substancial da proposta visual apresentada.
- Schemas JSON completos dos bancos de dados
- Exemplos de respostas dos endpoints de IA
- Credenciais de teste para os endpoints
- Documentação completa da API de IA

---

## 16. Contatos e Dúvidas

Para esclarecimentos sobre este documento ou sobre o projeto, favor entrar em contato:

**Projeto:** Eu Vereador AI  
**Contato:** +5561996841987 

---

## 17. Anexos

### 17.1 Glossário

**DNA:** Conjunto estruturado de informações sobre perfil pessoal, político, ideológico e estratégico do vereador, utilizado para personalização do conteúdo gerado.

**Ato de Mandato:** Categoria de atividade legislativa ou parlamentar que o vereador deseja comunicar.

**Rascunho:** Formulário de ato de mandato parcialmente preenchido e salvo automaticamente para retomada posterior.

**Histórico:** Registro de conversas completas que permite retomada de contexto.

**MAU (Monthly Active Users):** Usuários ativos mensais, definidos como usuários únicos que geraram pelo menos um conteúdo no período de 30 dias.

**Churn:** Taxa de cancelamento de assinatura.

**MVP (Minimum Viable Product):** Versão mínima do produto com funcionalidades essenciais para validação da proposta de valor.

### 17.2 Referências Técnicas

**Schemas de Banco de Dados:**
Os schemas completos JSON para o banco de DNA serão fornecidos à software house selecionada, incluindo:
- autodiagnostico.schema.json (estrutura completa do DNA)
- auditoria.schema.json (campos de auditoria e conformidade)

**Documentação da API:**
Documentação completa dos endpoints de integração será fornecida, incluindo:
- Exemplos de requisições
- Exemplos de respostas
- Códigos de erro
- Rate limits
- Autenticação detalhada

---