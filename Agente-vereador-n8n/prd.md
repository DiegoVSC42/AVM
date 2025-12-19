# Product Requirements Document (PRD)

## Eu Vereador AI - Assistente de Comunicação para Vereadores

**Versão:** 1.0  
**Data:** 28 de outubro de 2025  
**Status:** MVP em Desenvolvimento

---

## 1. Visão Executiva

### 1.1 Contexto e Problema

Vereadores brasileiros enfrentam desafios significativos na comunicação com seus eleitores. A maioria dos vereadores municipais possui renda mensal de aproximadamente R$ 4.000,00, não dispõe de assessores de comunicação e muitas vezes não possui ensino médio completo. Essa combinação de recursos limitados e baixa escolaridade resulta em dificuldade para interpretar demandas, desenvolver ideias de comunicação e produzir conteúdo estratégico para prestação de contas e engajamento com a população.

Atualmente, a comunicação é realizada de forma não estruturada, sem planejamento estratégico e sem personalização adequada ao contexto político e geográfico de cada mandato. Essa deficiência compromete a transparência, a accountability e o relacionamento entre representantes e representados.

### 1.2 Proposta de Solução

Eu Vereador AI é uma plataforma de inteligência artificial que auxilia vereadores na produção de conteúdo de comunicação personalizado, estratégico e adequado ao contexto específico de cada mandato. A solução utiliza três agentes de IA especializados para gerar conteúdo para diversos canais (redes sociais, discursos, artigos, releases) baseado em informações estruturadas sobre o perfil político, ideológico e geográfico do vereador.

A personalização é alcançada através de um perfil detalhado chamado DNA, que captura desde informações básicas (nome, cidade, mandato) até aspectos estratégicos (ideologia, posicionamento em relação à gestão, bairros-alvo, temas prioritários). O sistema aprende continuamente com as preferências do usuário, refinando o estilo e o tom dos conteúdos gerados ao longo do tempo.

### 1.3 Proposta de Valor Única

O Eu Vereador AI diferencia-se por combinar três elementos fundamentais: personalização profunda baseada no contexto político e geográfico do mandato, aplicação de metodologia comprovada de comunicação política desenvolvida por Marcelo Vitorino (especialista com mais de 20 anos de experiência) e interface simplificada focada em mobile-first para atender usuários com baixa familiaridade tecnológica. A solução não é apenas um gerador de texto genérico, mas um assistente estratégico que compreende as nuances da comunicação legislativa municipal.

### 1.4 Validação Preliminar

Um protótipo do conceito foi testado como custom GPT com vereadores que participaram de curso promovido pela equipe. O protótipo registrou mais de 90 utilizações em menos de um mês, validando a demanda e o interesse pelo tipo de solução proposta. O feedback geral dos usuários foi positivo, embora tenha sido identificada como principal objeção a dificuldade de uso, o que reforça a necessidade de investimento em interface intuitiva e onboarding estruturado.

### 1.5 Visão de Longo Prazo

Em doze meses, o produto deve estar consolidado com base de usuários pagantes recorrentes entre vereadores, com baixo churn e alta satisfação. A plataforma terá dados suficientes de uso para refinamento contínuo dos algoritmos de personalização através do agente de contexto++.

Em vinte e quatro meses, o Eu Vereador AI expandirá seu público-alvo para incluir assessores parlamentares, agências de comunicação política de cidades do interior e consultores individuais. Adicionalmente, o produto evoluirá de assistente de produção de conteúdo para assessor de gabinete completo, oferecendo ferramentas premium como construção de biografias profissionais, resumos estratégicos para entrevistas, análise de discursos e alinhamento ideológico.

---

## 2. Objetivos de Negócio e Métricas de Sucesso

### 2.1 Objetivos do MVP

O MVP tem três objetivos principais que definirão seu sucesso:

**Objetivo 1: Validação de Adoção**  
Alcançar 100 usuários mensais ativos que utilizem regularmente a plataforma para geração de conteúdo. Este número representa uma base inicial suficiente para validação do modelo de negócio e coleta de feedback estruturado.

**Objetivo 2: Validação de Retenção**  
Manter baixo índice de churn, demonstrando que o produto entrega valor contínuo e se torna ferramenta recorrente na rotina de comunicação dos vereadores. A retenção valida que a solução resolve um problema real de forma sustentável.

**Objetivo 3: Validação de Interesse em Evolução**  
Identificar interesse manifestado pelos usuários nas ferramentas futuras (Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais). Este interesse valida o potencial de upsell para versões premium do produto.

### 2.2 Métricas Quantitativas Primárias

**Usuários Ativos Mensais (MAU):** Número de usuários únicos que geram pelo menos um conteúdo completo no período de 30 dias. Meta mínima: 100 MAU.

**Taxa de Retenção Mensal:** Percentual de usuários que retornam para usar o produto no mês seguinte após primeira utilização. Indicador crítico de product-market fit.

### 2.3 Métricas Quantitativas Secundárias

**Tempo até Primeiro Valor (Time to Value):** Tempo médio entre cadastro e geração do primeiro conteúdo completo. Meta: 15 minutos com preenchimento de DNA, 5 minutos sem preenchimento.

**Conteúdos Gerados por Usuário por Mês:** Frequência de uso da plataforma, indicando nível de engajamento e utilidade percebida.

**Taxa de Conclusão de DNA:** Percentual de usuários que completam o formulário de DNA. Importante para entender adoção da personalização.

**Taxa de Feedback de Preferência:** Percentual de vezes que usuários selecionam versão preferida entre as duas opções geradas. Alimenta o agente de contexto++.

**Cliques em Sugestões de Ferramentas Futuras:** Medição de interesse em funcionalidades premium ainda não implementadas.

### 2.4 Métricas Qualitativas

**Net Promoter Score (NPS):** Pesquisa trimestral para medir satisfação e propensão a recomendar o produto.

**Satisfação com Qualidade do Conteúdo:** Avaliação qualitativa através de entrevistas com usuários selecionados.

**Principais Casos de Uso:** Identificação através de análise de dados de quais atos de mandato e canais são mais utilizados.

### 2.5 Modelo de Monetização

O produto opera sob modelo de assinatura recorrente mensal no valor de R$ 297,00 por usuário. No mês de lançamento, será oferecida promoção com desconto a ser definido. O modelo de assinatura garante previsibilidade de receita e alinha incentivos para entrega contínua de valor ao usuário.

O sistema implementa limitador de custo operacional de R$ 60,00 por usuário por mês em chamadas de API para os modelos de IA. Este limitador serve primariamente como guardrail contra uso indevido (compartilhamento de conta entre múltiplos usuários), uma vez que o limite foi calculado para ser muito superior ao uso esperado de um usuário individual utilizando a ferramenta de forma adequada.

### 2.6 Mercado Endereçável

O Brasil possui aproximadamente 60.000 vereadores em exercício. O mercado endereçável total representa esse universo completo, embora o foco estratégico inicial seja nos vereadores com menores recursos (que representam a maioria). Com penetração de mercado de apenas 1%, o produto alcançaria 600 usuários pagantes, gerando receita recorrente mensal de R$ 178.200,00.

---

## 3. Personas e Segmentação

### 3.1 Persona Primária - MVP

#### Vereador Municipal de Recursos Limitados

**Demografia:**  
Homem ou mulher, idade entre 35 e 55 anos, residente em cidade de pequeno ou médio porte no interior brasileiro. Renda mensal de aproximadamente R$ 4.000,00. Escolaridade até ensino médio incompleto ou completo. Muitas vezes exerce outra profissão paralelamente ao mandato.

**Contexto Profissional:**  
Primeiro mandato ou segundo mandato (reeleição). Não possui assessores de comunicação. Não possui equipe dedicada de apoio, contando no máximo com um ou dois colaboradores que não têm formação em comunicação. Gerencia suas redes sociais pessoalmente ou com ajuda de familiar ou pessoa de confiança.

**Dores e Necessidades:**  
Dificuldade em articular ideias e transformá-las em conteúdo estruturado. Não sabe como se posicionar estrategicamente nas redes sociais. Tem dificuldade de interpretar a relevância de suas ações legislativas para comunicar à população. Não consegue manter frequência e consistência na produção de conteúdo. Sente que precisa prestar contas mas não sabe como fazer isso de forma efetiva. Tem receio de cometer erros que possam prejudicar imagem ou mandato.

**Comportamento Digital:**  
Utiliza principalmente smartphone para acessar internet e redes sociais. Familiaridade básica com WhatsApp, Facebook e Instagram. Uso esporádico, não sistemático. Preferência por interfaces simples e diretas. Baixa tolerância para complexidade ou excesso de opções. Necessita de orientação clara sobre o que fazer em cada etapa.

**Objetivos com o Produto:**  
Conseguir produzir conteúdo de qualidade rapidamente. Entender como comunicar suas ações de forma estratégica. Manter presença regular nas redes sociais sem investir tempo excessivo. Sentir-se mais confiante em sua comunicação pública.

### 3.2 Personas Secundárias - Pós-MVP

**Assessor Parlamentar**  
Pessoa de confiança do vereador, geralmente sem formação em comunicação. Necessita de ferramenta que o auxilie a produzir conteúdo de qualidade sem conhecimento técnico especializado. Gerencia comunicação de um vereador em tempo integral.

**Agência de Comunicação Política**  
Pequena agência de cidade do interior com poucos profissionais experientes. Atende múltiplos clientes simultaneamente com orçamento limitado. Busca ferramenta para escalar produção mantendo qualidade e personalização.

**Consultor Individual**  
Profissional independente que presta consultoria de comunicação para um ou mais vereadores. Necessita de ferramenta que aumente sua produtividade e permita atender mais clientes.

*Nota: As personas secundárias terão suas necessidades específicas mapeadas em fase posterior ao MVP, mas a interface já será preparada para futura inclusão desses perfis de usuário.*

---

## 4. Arquitetura do Produto

### 4.1 Visão Geral da Arquitetura

O Eu Vereador AI opera através de arquitetura multi-agente orquestrada pela plataforma n8n. Três agentes especializados de inteligência artificial trabalham em conjunto para processar entradas do usuário, gerar conteúdo personalizado e aprender continuamente com feedback. A comunicação entre frontend, backend e agentes é gerenciada integralmente pelo n8n, que funciona como camada de orquestração e integração.

### 4.2 Agente de Guardrails

**Modelo:** GPT-4o mini  
**Função:** Primeiro ponto de contato com todas as entradas do usuário. Valida se a entrada respeita regras de segurança, ética e uso adequado da plataforma.

**Responsabilidades:**

- Bloquear tentativas de extração de instruções dos agentes ou documentos internos
- Impedir tentativas de engenharia reversa do sistema
- Bloquear acesso direto ao DNA do usuário ou estruturas de banco de dados
- Identificar e bloquear discurso de ódio, conteúdo discriminatório ou manifestações que violem termos de uso
- Prevenir uso para geração de conteúdo malicioso ou que possa causar dano

**Fluxo:** Toda mensagem do usuário passa primeiro pelo agente de Guardrails. Se a validação falha, o usuário recebe mensagem explicativa sobre a violação e o processamento é interrompido. Se a validação é bem-sucedida, a mensagem é encaminhada ao agente gerador de conteúdo.

### 4.3 Agente Gerador de Conteúdo

**Modelo:** Claude Sonnet 4.5  
**Função:** Núcleo do produto. Responsável pela geração de todo conteúdo solicitado pelo usuário.

**Entradas:**

1. DNA do usuário extraído do banco de dados
2. Contexto sobre o tipo de ato atual gerado pelo agente de contexto++
3. Respostas ao formulário específico sobre o ato de mandato
4. Canais selecionados para publicação
5. Metodologia de comunicação política de Marcelo Vitorino incorporada nas instruções do agente

**Processo:**

- Recebe inputs estruturados via prompt automatizado construído pelo n8n
- Analisa o contexto completo (DNA + preferências aprendidas + especificidades do ato)
- Gera duas versões distintas do mesmo conteúdo para cada canal selecionado
- Adapta tom, linguagem e estrutura conforme perfil do usuário e canal de destino
- Após apresentação do conteúdo, sugere outros tipos de atos de mandato relevantes ao contexto

**Saídas:**

- Duas versões de conteúdo para cada canal selecionado
- Sugestões de próximos atos de mandato a comunicar
- Adaptações de tom, foco ou estrutura mediante solicitação do usuário via interação contínua

### 4.4 Agente de Contexto++

**Modelo:** GPT-4o mini  
**Função:** Aprendizado contínuo das preferências do usuário para refinamento progressivo da personalização.

**Processo:**

1. Aguarda feedback do usuário sobre qual versão de conteúdo foi preferida
2. Recebe as duas versões geradas e a escolha do usuário
3. Analisa diferenças estruturais, estilísticas e de conteúdo entre as versões
4. Identifica padrões que motivaram a preferência
5. Gera registro estruturado no formato: "O [nome do vereador] prefere usar linguagem X à Y para ato de mandato Z"
6. Armazena preferência no banco de dados de contexto++, organizada por tipo de ato de mandato

**Evolução:**
O banco de contexto++ evolui organicamente. Para cada tipo de ato de mandato, há uma seção específica de preferências que é progressivamente enriquecida. Nas próximas gerações de conteúdo para aquele tipo de ato, o agente gerador consulta essas preferências acumuladas, resultando em conteúdo cada vez mais alinhado ao estilo e necessidades do usuário.

### 4.5 Orquestração via n8n

A plataforma n8n é responsável por:

- Receber requisições do frontend
- Construir prompts automatizados com informações de múltiplas fontes (bancos de dados de DNA, contexto++, formulários)
- Gerenciar chamadas sequenciais aos agentes (Guardrails → Gerador → Contexto++)
- Processar respostas dos agentes
- Atualizar bancos de dados conforme necessário
- Retornar respostas formatadas ao frontend

---

## 5. Funcionalidades do Produto

### 5.1 Tipos de Conteúdo Produzidos

O agente gerador de conteúdo produz os seguintes formatos, adaptados ao canal e tipo de ato selecionados:

**Releases:** Textos informativos estruturados com citações diretas do vereador, formatados para envio à imprensa local e regional.

**Publicações para Redes Sociais:**

- Instagram: post único com texto e sugestão de imagem, carrossel com sequência de conteúdo, quiz interativo, stories ou sequência de stories
- Facebook: posts adaptados ao formato e público típico da plataforma
- LinkedIn: conteúdo com tom profissional adequado à rede

**Roteiros de Vídeo:** Scripts estruturados para vídeos curtos (Reels, TikTok) ou longos (YouTube), incluindo introdução, desenvolvimento e encerramento.

**Artigos:** Textos longos para mídia impressa (jornais locais) ou digital (blogs, sites), com estrutura jornalística ou opinativa.

**Discursos:** Redação completa de discursos para tribuna da câmara, eventos públicos, comissões legislativas ou cerimônias.

**Resumos Estratégicos:** Preparação para conversas em programas de rádio, entrevistas para imprensa ou participações em podcasts, incluindo principais pontos a abordar e antecipação de perguntas.

**Biografia:** Construção de biografia profissional estruturada para uso em materiais de comunicação.

### 5.2 Atos de Mandato Contemplados

A plataforma organiza a comunicação em torno de tipos específicos de atos legislativos e atividades parlamentares:

- **Votações:** Comunicação sobre posicionamento em votações de projetos de lei, emendas ou requerimentos
- **Mobilização Social:** Conteúdo para engajamento da comunidade em causas ou movimentos
- **Requerimento ao Executivo:** Comunicação sobre cobranças ou solicitações formais ao poder executivo municipal
- **Fiscalização:** Prestação de contas sobre atividades de fiscalização de órgãos, secretarias ou serviços públicos
- **Tribuna:** Posicionamentos públicos sobre temas relevantes
- **Leis:** Comunicação sobre proposição ou revogação de leis municipais
- **Atendimento de Gabinete:** Relato de atendimentos realizados e demandas da população
- **Orçamento:** Explicação sobre debates, propostas ou votações relacionadas ao orçamento municipal
- **Eventos, Reuniões, Viagens Oficiais:** Cobertura de participações institucionais
- **Prestação de Contas:** Relatórios periódicos sobre atividades e resultados do mandato
- **Emendas:** Comunicação sobre emendas apresentadas ao orçamento ou a projetos de lei

### 5.3 Canais de Comunicação Suportados

O sistema permite seleção múltipla de canais, gerando conteúdo adaptado para cada um:

- Post para Instagram ou Facebook
- Reels
- Stories
- TikTok
- Conteúdo para site institucional
- Roteiro para YouTube

*Nota: O MVP foca na geração de conteúdo textual e roteiros. Geração de imagens, vídeos ou edição de mídia estão fora do escopo inicial.*

---

## 6. Jornada do Usuário e Fluxos

### 6.1 Onboarding Inicial

**Objetivo:** Apresentar a plataforma, explicar conceitos principais e conduzir usuário até primeira geração de conteúdo de forma guiada.

**Etapas:**

1. Criação de conta (email, senha, dados básicos)
2. Aceite de termos de uso (conformidade LGPD, responsabilidade sobre conteúdo gerado, uso de IA)
3. Tutorial interativo explicando: conceito de DNA, processo de geração de conteúdo, papel dos atos de mandato e canais
4. Convite para preenchimento de DNA com explicação clara sobre benefícios da personalização
5. Direcionamento para geração do primeiro conteúdo com sugestão de ato de mandato simples

**Tempo Estimado:** 5 a 10 minutos antes do preenchimento de DNA.

### 6.2 Construção de DNA

**Objetivo:** Capturar informações estruturadas que permitam personalização profunda do conteúdo gerado.

**Formato:** Formulário modal apresentado em blocos progressivos. Cada bloco agrupa perguntas relacionadas e é salvo imediatamente no banco de dados ao ser concluído, permitindo retomada posterior.

**Blocos do DNA (baseado em autodiagnostico.schema.json e auditoria.schema.json):**

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

- Frequência de publicação semanal por rede (Instagram, Facebook, YouTube, WhatsApp, Email)
- Se planeja conteúdo semanalmente
- Se há integração entre canais

**Bloco 8 - Engajamento:**

- Percentual de comentários que responde
- Tempo médio de resposta a comentários (em horas)
- Se interage com outros perfis nas redes sociais

**Bloco 9 - Prestação de Contas e Transparência:**

- Prova de trabalho publicada (votações, requerimentos, fiscalizações, emendas, prestação de contas)
- Se prestação de contas é recorrente

**Bloco 10 - Recursos de Produção:**

- Biblioteca de mídia disponível (fotos de qualidade, vídeos b-roll, vinhetas)
- Base própria de contatos (número de contatos WhatsApp e Email)

**Bloco 11 - Padronização:**

- Se possui padrões visuais consistentes
- Se possui linguagem padronizada

**Bloco 12 - Conformidade:**

- Riscos jurídicos (opt-in para WhatsApp, opt-in para Email, se usa base comprada)
- Observações gerais

**Indicador de Progresso:** Percentual de conclusão visível durante todo o preenchimento.

**Características:**

- Preenchimento é opcional mas fortemente recomendado
- Pode ser feito parcialmente e retomado a qualquer momento
- Pode ser editado posteriormente através do perfil do usuário
- Cada salvamento de bloco atualiza imediatamente o banco de dados

### 6.3 Fluxo Principal - Geração de Conteúdo

**Passo 1: Tela Inicial**  
Usuário acessa tela principal da aplicação e seleciona botão "Iniciar Comunicação" (ou similar).

**Passo 2: Seleção de Ato de Mandato**  
Tela apresenta blocos visuais representando cada tipo de ato de mandato. Usuário seleciona um ato (exemplo: Prestação de Contas).

**Passo 3: Seleção de Canais**  
Tela apresenta blocos visuais representando cada tipo de canal de comunicação. Usuário pode selecionar múltiplos canais simultaneamente (exemplo: Post Instagram, Stories e Facebook).

**Passo 4: Preenchimento de Formulário Específico**  
Sistema apresenta modal com formulário em blocos contendo perguntas específicas sobre o ato selecionado. As perguntas variam conforme o tipo de ato. Cada bloco é salvo como rascunho automaticamente, permitindo retomada posterior.

Exemplo de perguntas para ato de Prestação de Contas:

- Qual período está sendo reportado?
- Quais foram as principais ações realizadas?
- Houve algum resultado mensurável?
- Há algum ponto de destaque ou conquista específica?

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

Após seleção da versão preferida, feedback é enviado ao agente de contexto++.

**Passo 8: Sugestões**  
Sistema apresenta sugestões: "Gostaria de criar um [outro ato de mandato]?" e "Gostaria de publicar em [outro canal]?"

**Passo 9: Interação Contínua**  
Usuário pode interagir com o conteúdo gerado através de área de texto ou gravação de áudio:

- Solicitar ajustes de tom
- Pedir para trocar palavras específicas
- Solicitar foco maior em determinado tópico
- Pedir versão mais curta ou mais longa
- Solicitar adaptação para outro canal

Cada interação gera nova resposta do agente mantendo contexto da conversa.

### 6.4 Gestão de Rascunhos

Sempre que usuário está preenchendo formulário de ato de mandato e interrompe o processo antes de concluir, o sistema salva automaticamente como rascunho. Na tela inicial, área de rascunhos permite retomar o preenchimento exatamente de onde parou, com todas as informações já inseridas preservadas.

### 6.5 Gestão de Histórico

Sempre que conteúdo é efetivamente gerado, a conversa completa (entrada do usuário, formulário preenchido, conteúdo gerado, interações subsequentes) é salva no histórico. Na tela inicial, área de histórico permite retornar a qualquer conversa anterior e continuar interagindo com o agente a partir daquele contexto.

---

## 7. Interface e Design

### 7.1 Princípios de Design

**Mobile-First:** Todo o produto é concebido primariamente para uso em smartphone. A interface desktop é adaptação da versão mobile, não o contrário. Elementos de interface, tamanho de botões, espaçamento e navegação são otimizados para telas pequenas e interação touch.

**Simplicidade Extrema:** Considerando baixa familiaridade tecnológica do público-alvo, a interface evita complexidade. Uma ação principal por tela sempre que possível. Fluxos lineares e claros. Ausência de jargões técnicos.

**Feedback Constante:** Usuário sempre sabe em que etapa está, o que precisa fazer e o que está acontecendo. Indicadores de progresso visíveis. Mensagens claras durante processamento. Confirmações após ações importantes.

**Acessibilidade:** Fontes legíveis em tamanhos adequados. Contraste suficiente entre texto e fundo. Botões grandes o suficiente para toque preciso. Linguagem clara e direta.

### 7.2 Identidade Visual

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

### 7.3 Estrutura da Tela Inicial

**Header:**

- Nome da aplicação centralizado no topo: "Eu Vereador AI"

**Área de Perfil:**

- Botão de perfil (ícone de usuário) posicionado no canto superior
- Ao clicar, acesso a: visualização e edição de DNA, alteração de senha, dados da conta, logout

**Área de Ação Principal:**

- Botão destacado "Iniciar Comunicação" (ou nome similar)
- Redireciona para tela de seleção de atos de mandato

**Área de DNA:**

- Bloco dedicado "Construir Biografia" (ou nome similar)
- Indicador de percentual de conclusão do DNA
- Redireciona para formulário de DNA em modal

**Área de Ferramentas (Placeholder):**

- Bloco dedicado "Ferramentas"
- Botões para: Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais
- Visual indica que são funcionalidades futuras (ícones com indicação "Em breve" ou similar)
- Botões desabilitados mas visíveis para criar expectativa

**Área de Histórico:**

- Bloco com lista de conversas anteriores
- Ao clicar, retorna ao chat de onde parou com contexto preservado

**Área de Rascunhos:**

- Bloco com lista de formulários parcialmente preenchidos
- Ao clicar, retorna ao preenchimento com informações já inseridas preservadas

**Footer:**

- Links para suporte, termos de uso, política de privacidade

### 7.4 Navegação

Navegação simples e linear. Breadcrumbs ou indicação clara de onde usuário está no fluxo. Botão de voltar sempre visível. Menu hamburger para acesso a áreas secundárias (perfil, histórico, rascunhos, ferramentas).

### 7.5 Estados de Interface

**Loading:** Spinner ou skeleton screens durante carregamento. Mensagens contextuais sobre o que está acontecendo (especialmente durante geração de conteúdo).

**Empty States:** Mensagens amigáveis quando não há histórico, rascunhos ou DNA preenchido, com call-to-action claro para primeira ação.

**Error States:** Mensagens claras sobre erros, sem jargões técnicos, com sugestão de próximos passos.

---

## 8. Requisitos Técnicos

### 8.1 Stack Tecnológico

**Frontend:**

- Plataforma: Lovable para criação rápida de interface
- Foco: Mobile-first responsive design
- Linguagem: JavaScript/TypeScript conforme capacidades do Lovable

**Orquestração:**

- Plataforma: n8n
- Função: Gerenciar comunicação entre frontend, bancos de dados e agentes de IA

**Modelos de IA:**

- Agente Gerador de Conteúdo: Claude Sonnet 4.5 (Anthropic)
- Agente de Guardrails: GPT-4o mini (OpenAI)
- Agente de Contexto++: GPT-4o mini (OpenAI)

**Transcrição de Áudio:**

- Idioma: Português brasileiro
- Serviço: A definir (Whisper API, Google Speech-to-Text ou similar)

**Hosting:**

- Provedor: Digital Ocean
- Bancos de dados gerenciados na mesma infraestrutura

**Pagamento:**

- Integração terceirizada com gateway de pagamento para assinaturas recorrentes

### 8.2 Bancos de Dados

**Banco de DNA:**

- Armazena perfil completo do usuário estruturado conforme schemas fornecidos
- Permite atualizações incrementais (por bloco)
- Versionamento para histórico de mudanças

**Banco de Contexto++:**

- Armazena preferências aprendidas organizadas por tipo de ato de mandato
- Estrutura: cada usuário tem colunas dedicadas para cada tipo de ato (preferencias_votacoes, preferencias_fiscalizacao, preferencias_prestacao_contas, etc.)
- Cada coluna armazena texto com preferências específicas para aquele ato
- Evolui continuamente sem limite de tamanho

**Banco de Rascunhos:**

- Armazena formulários parcialmente preenchidos
- Inclui: user_id, ato_tipo, canais selecionados, respostas parciais, timestamp
- Permite retomada exata do ponto de parada

**Banco de Histórico:**

- Armazena conversas completas
- Inclui: user_id, ato_tipo, canais, formulário completo, conteúdo gerado, interações subsequentes
- Permite retomada de contexto para novas interações

**Banco de Usuários:**

- Dados de cadastro, autenticação, assinatura, uso de API (para controle de limite de custo)

### 8.3 Performance

**Tempo de Resposta:**

- Navegação entre telas: instantânea (< 300ms)
- Carregamento de histórico/rascunhos: < 2 segundos
- Geração de conteúdo: 1 a 3 minutos (com feedback contínuo ao usuário)
- Transcrição de áudio: < 10 segundos para áudios de até 2 minutos

**Disponibilidade:**

- Uptime esperado: 99% (aproximadamente 7 horas de downtime aceitável por mês para manutenções planejadas)
- Janela de manutenção: Madrugadas de horário brasileiro

### 8.4 Escalabilidade

Sistema deve suportar crescimento gradual de base de usuários. Inicialmente projetado para até 500 usuários simultâneos. Uso de serviços gerenciados (bancos de dados, APIs de IA) facilita escalabilidade horizontal.

### 8.5 Segurança e Privacidade

**Autenticação:** Sistema de login com email e senha. Tokens de sessão com expiração.

**Armazenamento de Dados:** Todos os dados armazenados em servidores próprios na Digital Ocean. Conformidade com LGPD: dados coletados apenas para funcionalidade do produto, usuário pode visualizar e editar DNA a qualquer momento, dados não são compartilhados com terceiros.

**Criptografia:** Dados sensíveis em repouso devem ser criptografados. Comunicação entre frontend e backend via HTTPS.

**Controle de Acesso:** Cada usuário acessa apenas seus próprios dados. Isolamento por user_id em todas as queries de banco de dados.

**Backup:** Backups automáticos diários dos bancos de dados com retenção de 30 dias.

### 8.6 Limitações e Guardrails Técnicos

**Limite de Custo:** Sistema monitora custos de API por usuário. Ao aproximar-se de R$ 60,00 no mês, aviso é enviado ao usuário. Ao atingir limite, geração de novo conteúdo é bloqueada até próximo ciclo de cobrança.

**Limite de Áudio:** Áudios para transcrição limitados a 5 minutos de duração.

**Limite de Interações:** Para evitar abuso, máximo de 50 interações por conversa. Após limite, usuário deve iniciar nova geração de conteúdo.

**Validação de Guardrails:** Implementada em nível de agente, não contornável por frontend.

---

## 9. Casos de Uso Detalhados

### 9.1 Caso de Uso: Prestação de Contas Mensal

**Ator:** Vereador João, primeiro mandato, atua em bairros periféricos, foco em saúde pública.

**Contexto:** Final de mês, João precisa comunicar suas atividades aos eleitores.

**Fluxo:**

1. João acessa aplicação no smartphone
2. Clica em "Iniciar Comunicação"
3. Seleciona ato "Prestação de Contas"
4. Seleciona canais: Post Instagram, Post Facebook, Stories
5. Preenche formulário respondendo:
   - Período: Outubro de 2025
   - Principais ações: Fiscalizou UBS do Jardim Primavera, protocolou requerimento sobre falta de medicamentos, participou de reunião com secretário de saúde
   - Resultados: Secretaria comprometeu-se a regularizar estoque de medicamentos em 15 dias
   - Destaque: Conseguiu compromisso formal após pressão
6. Sistema confirma e inicia geração
7. Após 2 minutos, apresenta duas versões para cada canal
8. João lê ambas versões do post Instagram, prefere a versão B (mais direta e menos formal)
9. João seleciona versão B, sistema registra feedback
10. João copia conteúdo e cola em seu Instagram
11. Sistema sugere: "Que tal comunicar também sobre sua fiscalização?"
12. João decide não continuar no momento, fecha aplicação
13. Sistema salva conversa em histórico para futura retomada

**Resultado:** João conseguiu comunicar suas atividades de forma estruturada em menos de 10 minutos. Conteúdo foi personalizado para seu perfil (linguagem direta, foco em saúde, atuação em bairro específico).

### 9.2 Caso de Uso: Posicionamento Urgente sobre Votação

**Ator:** Vereadora Maria, reeleição, posicionamento de oposição, ideologia social.

**Contexto:** Hoje haverá votação polêmica sobre aumento de IPTU. Maria precisa comunicar sua posição rapidamente antes da sessão.

**Fluxo:**

1. Maria acessa aplicação
2. Entra em "Iniciar Comunicação"
3. Seleciona ato "Votações"
4. Seleciona canais: Stories, Post Facebook (precisa de alcance rápido)
5. Preenche formulário:
   - Projeto: Aumento de IPTU em 15%
   - Seu voto: Contra
   - Justificativa: Aumento excessivo que prejudica famílias em momento de dificuldade econômica
   - Proposta alternativa: Redução de despesas administrativas antes de aumentar impostos
6. Sistema gera conteúdo
7. Maria revisa e percebe que está muito técnico
8. Usa área de interação com áudio: grava "quero uma linguagem mais popular, que qualquer pessoa entenda"
9. Sistema regenera em 40 segundos
10. Maria aprova, copia e publica imediatamente

**Resultado:** Em menos de 7 minutos, Maria conseguiu comunicar posicionamento claro e alinhado com sua ideologia, em linguagem acessível, atendendo necessidade urgente.

### 9.3 Caso de Uso: Usuário Sem DNA Preenchido

**Ator:** Vereador Carlos, novo usuário, ainda não preencheu DNA.

**Contexto:** Carlos quer testar ferramenta rapidamente.

**Fluxo:**

1. Carlos cria conta
2. Sistema sugere preenchimento de DNA, mas oferece opção "Fazer depois"
3. Carlos escolhe fazer depois
4. Inicia geração de conteúdo sobre fiscalização de obra pública
5. Sistema gera conteúdo baseado apenas nas informações do formulário específico e metodologia padrão de Marcelo Vitorino
6. Conteúdo é genérico mas funcional
7. Após copiar, sistema mostra mensagem: "Preencha seu DNA para conteúdo ainda mais personalizado ao seu mandato"
8. Carlos percebe valor e decide preencher DNA posteriormente

**Resultado:** Produto entrega valor mesmo sem DNA completo, validando utilidade imediata, mas incentiva preenchimento para experiência superior.

---

## 10. Requisitos Não-Funcionais

### 10.1 Usabilidade

**Intuitividade:** Usuário com baixa familiaridade tecnológica deve conseguir gerar primeiro conteúdo sem assistência externa em até 15 minutos após onboarding.

**Acessibilidade:** Interface segue diretrizes WCAG 2.1 nível AA. Contraste mínimo de 4.5:1 para textos. Botões com área mínima de toque de 44x44 pixels.

**Linguagem:** Toda interface em português brasileiro. Ausência de anglicismos ou jargões técnicos. Linguagem clara e direta.

### 10.2 Confiabilidade

**Consistência:** Mesmo input deve gerar outputs de qualidade equivalente. Variação entre as duas versões geradas, mas ambas devem atender requisitos de qualidade.

**Recuperação de Erros:** Sistema não perde dados do usuário. Salvamento automático de rascunhos. Possibilidade de retomada após erros de conexão ou fechamento acidental.

### 10.3 Manutenibilidade

**Modularidade:** Agentes são independentes. Mudança em um agente não afeta os demais. Prompts de agentes são configuráveis sem necessidade de alteração de código.

**Monitoramento:** Logs de erros, tempo de resposta de APIs, uso de recursos. Alertas automáticos para falhas críticas.

### 10.4 Conformidade Legal

**LGPD:** Conformidade total com Lei Geral de Proteção de Dados. Consentimento explícito na criação de conta. Possibilidade de visualização, edição e exclusão de dados pessoais a qualquer momento.

**Termos de Uso:** Documento detalhando que conteúdo é gerado por IA, responsabilidade do conteúdo é exclusivamente do usuário, dados são armazenados para personalização do serviço.

**Responsabilidade:** Sistema não se responsabiliza por uso inadequado, conteúdo factualmente incorreto ou consequências do uso de conteúdo gerado.

---

## 11. Riscos e Mitigações

### 11.1 Risco: Dificuldade de Uso

**Descrição:** Público-alvo tem baixa familiaridade tecnológica. Produto pode ser considerado complicado mesmo com esforços de simplificação.

**Probabilidade:** Média-Alta  
**Impacto:** Alto (diretamente afeta adoção e retenção)

**Mitigação:**

- Investimento significativo em onboarding estruturado com tutorial interativo
- Testes de usabilidade com representantes do público-alvo antes do lançamento
- Sistema de suporte acessível (WhatsApp, vídeos tutoriais)
- Feedback contínuo constante na interface
- Iteração rápida baseada em pontos de fricção identificados

### 11.2 Risco: Uso Indevido (Compartilhamento de Conta)

**Descrição:** Usuário pode compartilhar login com múltiplas pessoas (outros vereadores, assessores) para diluir custo de assinatura.

**Probabilidade:** Média  
**Impacto:** Alto (afeta modelo de negócio e custos operacionais)

**Mitigação:**

- Implementação de limite de custo de R$ 60,00 por mês em APIs por usuário (muito superior ao uso individual normal)
- Monitoramento de padrões de uso anormais (múltiplos acessos simultâneos, diferentes localizações geográficas, volumes excessivos)
- Termos de uso explícitos proibindo compartilhamento
- Detecção automática e bloqueio temporário de contas com uso suspeito para investigação

### 11.3 Risco: Conteúdo Factualmente Incorreto ou Problemático

**Descrição:** IA pode gerar conteúdo com informações incorretas, posicionamentos contraditórios ao perfil do usuário ou linguagem inadequada.

**Probabilidade:** Baixa-Média  
**Impacto:** Alto (afeta reputação do produto e do usuário)

**Mitigação:**

- Agente de Guardrails filtra conteúdo problemático antes de apresentação
- Disclaimers claros de que usuário deve revisar conteúdo antes de publicar
- Termos de uso estabelecem que responsabilidade é exclusiva do usuário
- Coleta de feedback sobre problemas encontrados para refinamento contínuo de prompts
- Metodologia de comunicação de especialista incorporada nos prompts reduz margem para erros estratégicos

### 11.4 Risco: Aumento de Custos de API

**Descrição:** OpenAI ou Anthropic podem aumentar preços de acesso às APIs, afetando margem do produto.

**Probabilidade:** Média  
**Impacto:** Alto (afeta viabilidade econômica)

**Mitigação:**

- Limite de custo por usuário já implementado reduz exposição
- Margem de segurança entre valor de assinatura (R\ $ 297) e custo máximo por usuário (R$ 60)
- Possibilidade de migração para modelos alternativos (LLaMA, Mistral em self-hosting)
- Cláusula em termos de uso permite reajuste de preço de assinatura com aviso prévio

### 11.5 Risco: Baixa Adoção Inicial

**Descrição:** Dificuldade em alcançar 100 usuários ativos mensais devido a desconhecimento do produto, desconfiança em IA ou preferência por métodos tradicionais.

**Probabilidade:** Média  
**Impacto:** Alto (afeta validação de negócio e continuidade do projeto)

**Mitigação:**

- Aproveitamento de base de vereadores que já participaram de curso promovido pela equipe
- Demonstrações práticas e cases de uso para convencimento
- Período de trial gratuito ou desconto promocional significativo no primeiro mês
- Parcerias com associações de vereadores ou entidades representativas
- Marketing de conteúdo demonstrando valor (vídeos, tutoriais, cases de sucesso)

### 11.6 Risco: Problemas Regulatórios

**Descrição:** Futura regulamentação sobre uso de IA em comunicação política pode impor restrições ou requisitos adicionais.

**Probabilidade:** Baixa-Média  
**Impacto:** Médio (pode exigir adaptações do produto)

**Mitigação:**

- Transparência total: termos de uso deixam claro que conteúdo é gerado por IA
- Acompanhamento de discussões regulatórias no Brasil e adaptação proativa
- Disclaimers visíveis sobre uso de IA
- Possibilidade de adicionar marcação automática em conteúdos indicando geração por IA se regulamentação exigir

---

## 12. Roadmap e Priorização

### 12.1 Definição de MVP

O MVP (Minimum Viable Product) inclui exclusivamente funcionalidades essenciais para validação da proposta de valor central: permitir que vereadores gerem conteúdo de comunicação personalizado de forma rápida e estruturada.

**Incluído no MVP:**

- Sistema de cadastro e autenticação
- Termos de uso com conformidade LGPD
- Onboarding básico com tutorial interativo
- Formulário de DNA completo em blocos com salvamento progressivo
- Indicador de progresso de preenchimento de DNA
- Fluxo completo de geração de conteúdo (seleção de ato, canais, preenchimento de formulário, geração)
- Arquitetura de três agentes (Guardrails, Gerador de Conteúdo, Contexto++)
- Apresentação de duas versões de conteúdo
- Sistema de feedback de preferência
- Interação contínua via texto e áudio
- Área de histórico
- Área de rascunhos
- Perfil do usuário com visualização e edição de DNA
- Sistema de limite de custo com aviso ao usuário
- Interface mobile-first conforme identidade visual especificada
- Todos os atos de mandato listados
- Todos os canais de comunicação listados

**Placeholders no MVP (visíveis mas não funcionais):**

- Ferramentas extras: Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais
- Seleção de público-alvo (assessores, agências, consultores) visível na interface mas sem diferenciação de funcionalidades

**Explicitamente fora do MVP:**

- Lei orgânica e regimento interno
- Funcionalidades completas das ferramentas extras
- Diferenciação de experiência por tipo de público (assessores, agências, consultores)
- Integração direta com plataformas de redes sociais para publicação automática
- Geração de imagens, vídeos ou outros formatos além de texto
- Sistema de colaboração ou múltiplos usuários por conta

### 12.2 Cronograma Estimado para MVP

**Definição pendente.** Não há data-alvo específica para lançamento neste momento. Desenvolvimento será conduzido por uma pessoa dedicada a agentes e telas no Lovable. Interface com usuário final e sistema de pagamento serão terceirizados.

### 12.3 Primeira Onda Pós-MVP

Após validação do MVP com base em métricas de adoção, retenção e feedback dos usuários, primeira expansão priorizará:

**Implementação de Ferramentas Premium:**

- Bio profissional estruturada
- MiniBio para diferentes contextos
- Quiz de alinhamento ideológico
- Resumo estratégico para entrevistas e programas
- Análise e reescrita de discursos existentes
- Produção de documentos oficiais (ofícios, requerimentos formais, etc.)

Essas ferramentas serão oferecidas em tier premium de assinatura (preço superior aos R$ 297 base), posicionando o produto como assessor de gabinete completo.

### 12.4 Segunda Onda Pós-MVP

**Expansão de Públicos:**

- Adaptação de fluxos e linguagem para assessores parlamentares
- Funcionalidades específicas para agências (gestão de múltiplos clientes, white-label parcial)
- Ferramentas para consultores individuais

**Integrações:**

- Consulta automatizada a regimento interno e lei orgânica do município (via RAG)
- Possível integração com plataformas de publicação

### 12.5 Critérios de Passagem entre Fases

**MVP → Primeira Onda:**

- Alcançar 100 usuários mensais ativos sustentados por pelo menos 2 meses consecutivos
- Taxa de retenção mensal acima de 60%
- NPS acima de 40
- Interesse manifestado por pelo menos 30% dos usuários em ferramentas premium

**Primeira Onda → Segunda Onda:**

- Base de usuários pagantes estável acima de 300
- Receita recorrente mensal sustentável
- Taxa de conversão para tier premium acima de 15%

---

## 13. Métricas e KPIs Consolidados

### 13.1 Métricas de Adoção

- **Novos Cadastros/Mês:** Meta inicial 50+ no primeiro mês, crescimento de 20% mês a mês
- **Taxa de Conclusão de Onboarding:** % de usuários que completam tutorial e geram primeiro conteúdo. Meta: acima de 70%
- **Taxa de Preenchimento de DNA:** % de novos usuários que preenchem ao menos 50% do DNA. Meta: acima de 60%
- **Usuários Ativos Mensais (MAU):** Meta: 100 MAU até final do sexto mês

### 13.2 Métricas de Engajamento

- **Conteúdos Gerados por Usuário/Mês:** Indica frequência de uso. Benchmark: 4-8 conteúdos/mês
- **Taxa de Retorno (D7, D30):** % de usuários que retornam em 7 e 30 dias após primeiro uso
- **Interações por Conteúdo:** Número médio de ajustes solicitados após geração inicial
- **Uso de Áudio vs. Texto:** % de interações feitas via gravação de áudio

### 13.3 Métricas de Retenção

- **Taxa de Retenção Mensal:** % de usuários do mês anterior que continuam ativos no mês atual. Meta: acima de 60%
- **Churn Mensal:** % de usuários que cancelam assinatura. Meta: abaixo de 10%
- **Lifetime Value (LTV):** Receita média por usuário ao longo de sua vida como cliente

### 13.4 Métricas de Qualidade

- **NPS (Net Promoter Score):** Pesquisa trimestral. Meta: acima de 40
- **Taxa de Feedback Positivo:** % de vezes que usuário seleciona versão preferida (indica engajamento com funcionalidade de aprendizado)
- **Tickets de Suporte por Usuário:** Indica problemas de usabilidade ou bugs. Meta: abaixo de 0.5 tickets/usuário/mês

### 13.5 Métricas Operacionais

- **Tempo Médio de Geração de Conteúdo:** Meta: entre 1-3 minutos
- **Custo Médio de API por Usuário/Mês:** Monitoramento para garantir que permanece bem abaixo de R$ 60
- **Taxa de Erro de APIs:** % de chamadas a modelos de IA que falham. Meta: abaixo de 1%
- **Uptime do Sistema:** Meta: 99%

### 13.6 Métricas de Receita

- **MRR (Monthly Recurring Revenue):** Receita recorrente mensal
- **ARPU (Average Revenue Per User):** Receita média por usuário
- **CAC (Customer Acquisition Cost):** Custo para adquirir novo cliente pagante
- **LTV/CAC Ratio:** Relação entre valor do tempo de vida do cliente e custo de aquisição. Meta: acima de 3

---

## 14. Dependências e Integrações

### 14.1 Dependências Externas Críticas

**APIs de Modelos de IA:**

- Anthropic Claude API (Sonnet 4.5)
- OpenAI GPT API (GPT-4o mini)
- Disponibilidade e estabilidade dessas APIs são críticas para funcionamento do produto

**Serviço de Transcrição:**

- API de speech-to-text (Whisper, Google ou similar)
- Necessário para funcionalidade de entrada por áudio

**Gateway de Pagamento:**

- Integração terceirizada para gestão de assinaturas recorrentes
- Precisa suportar cobranças mensais automáticas, gestão de cartões, boletos e PIX

**Plataforma de Hosting:**

- Digital Ocean
- Serviços gerenciados de banco de dados e infraestrutura

### 14.2 Integrações Planejadas

**Fase MVP:**

- n8n para orquestração de agentes
- Lovable para frontend
- APIs de IA mencionadas
- Gateway de pagamento

**Pós-MVP (Futuro):**

- Consulta a bases de dados de legislação municipal (RAG para regimento interno e lei orgânica)
- Possível integração com APIs de redes sociais para publicação direta

### 14.3 Riscos de Dependência

Dependência de APIs externas representa risco. Mitigações incluem implementação de retry logic para chamadas de API, fallback para modelos alternativos em caso de indisponibilidade prolongada e comunicação transparente com usuários durante interrupções.

---

## 15. Questões Éticas e Conformidade

### 15.1 Transparência sobre Uso de IA

O produto deixa absolutamente claro em múltiplos pontos que conteúdo é gerado por inteligência artificial:

- Termos de uso explicitam que ferramenta utiliza IA generativa
- Nome do produto ("Eu Vereador AI") comunica natureza tecnológica
- Avisos em pontos relevantes da interface indicam que conteúdo é sugestão gerada por IA e deve ser revisado

### 15.2 Responsabilidade sobre Conteúdo

Termos de uso estabelecem claramente que responsabilidade sobre uso, publicação e consequências de conteúdo gerado é exclusivamente do usuário. Plataforma fornece ferramenta de auxílio, mas não se responsabiliza por:

- Informações factualmente incorretas
- Posicionamentos políticos específicos
- Consequências legais ou reputacionais do uso de conteúdo
- Violações de direitos de terceiros

Usuário assume total responsabilidade ao aceitar termos de uso na criação da conta.

### 15.3 Conformidade com LGPD

Plataforma opera em total conformidade com Lei Geral de Proteção de Dados:

**Consentimento:** Usuário consente explicitamente com coleta e uso de dados ao aceitar termos de uso.

**Finalidade:** Dados são coletados exclusivamente para funcionalidade do produto (personalização de conteúdo gerado).

**Acesso:** Usuário pode visualizar e editar seus dados (DNA) a qualquer momento através do perfil.

**Exclusão:** Usuário pode solicitar exclusão completa de seus dados, embora isso implique encerramento da conta.

**Não Compartilhamento:** Dados não são compartilhados com terceiros além dos prestadores de serviço essenciais (hosting, APIs de IA) que estão sob acordo de confidencialidade.

**Segurança:** Dados sensíveis são criptografados em repouso e transmissão ocorre via HTTPS.

### 15.4 Prevenção de Uso Malicioso

Agente de Guardrails implementa camada de proteção contra:

- Discurso de ódio ou discriminação
- Conteúdo que promova violência
- Tentativas de manipulação ou desinformação deliberada
- Uso para finalidades não relacionadas a comunicação legislativa legítima

Sistema bloqueia e registra tentativas de uso inadequado, podendo resultar em suspensão de conta em casos graves.

---

## 16. Suporte e Documentação

### 16.1 Canais de Suporte

**Durante MVP:** Suporte via WhatsApp e email. Tempo de resposta esperado de até 24 horas em dias úteis.

**Pós-MVP:** Expansão para incluir central de ajuda com artigos e vídeos tutoriais, possível implementação de chatbot para dúvidas básicas.

### 16.2 Documentação para Usuários

- Vídeos curtos (1-3 minutos) explicando funcionalidades principais
- Guia escrito passo-a-passo disponível na plataforma
- FAQ com perguntas mais comuns identificadas durante beta

### 16.3 Onboarding Contínuo

Além do onboarding inicial, sistema apresenta dicas contextuais durante uso (tooltips, hints) para ajudar usuário a descobrir funcionalidades progressivamente sem sobrecarga inicial.

---

## 17. Critérios de Aceitação do MVP

O MVP será considerado pronto para lançamento quando atender aos seguintes critérios:

### 17.1 Funcionalidades Implementadas

- [ ] Sistema de cadastro e autenticação funcional
- [ ] Termos de uso com aceite obrigatório
- [ ] Onboarding com tutorial interativo completo
- [ ] Formulário de DNA em blocos com todos os campos conforme schemas fornecidos
- [ ] Indicador de progresso de DNA funcionando corretamente
- [ ] Salvamento progressivo de blocos de DNA no banco de dados
- [ ] Fluxo completo de geração de conteúdo para todos os atos de mandato listados
- [ ] Seleção múltipla de canais funcionando
- [ ] Formulários específicos por tipo de ato implementados
- [ ] Integração com os três agentes via n8n
- [ ] Geração de duas versões de conteúdo
- [ ] Botão de copiar funcionando em cada versão
- [ ] Sistema de feedback de preferência registrando no banco de contexto++
- [ ] Interação contínua via texto funcionando
- [ ] Entrada por áudio com transcrição funcionando
- [ ] Histórico salvando conversas completas e permitindo retomada
- [ ] Rascunhos salvando formulários parciais e permitindo retomada
- [ ] Área de perfil com visualização e edição de DNA
- [ ] Sistema de limite de custo monitorando e avisando usuário
- [ ] Interface mobile-first responsiva em todas as telas
- [ ] Identidade visual aplicada consistentemente

### 17.2 Qualidade e Performance

- [ ] Tempo médio de geração de conteúdo entre 1-3 minutos
- [ ] Taxa de erro de APIs abaixo de 5% em testes
- [ ] Interface responsiva em dispositivos móveis (iPhone, Android)
- [ ] Navegação intuitiva validada com pelo menos 5 usuários representativos do público-alvo

### 17.3 Testes Realizados

- [ ] Testes funcionais de todos os fluxos principais
- [ ] Testes de usabilidade com representantes do público-alvo
- [ ] Testes de segurança básicos (tentativas de acesso não autorizado)
- [ ] Testes de carga com simulação de pelo menos 50 usuários simultâneos
- [ ] Validação de conformidade LGPD

### 17.4 Documentação

- [ ] Termos de uso redigidos e revisados juridicamente
- [ ] Política de privacidade completa
- [ ] Documentação técnica de arquitetura para manutenção futura
- [ ] Vídeos tutoriais de funcionalidades principais produzidos

---

## 18. Glossário

**DNA:** Conjunto estruturado de informações sobre perfil pessoal, político, ideológico e estratégico do vereador, utilizado para personalização do conteúdo gerado.

**Ato de Mandato:** Categoria de atividade legislativa ou parlamentar que o vereador deseja comunicar (exemplos: votações, fiscalização, prestação de contas).

**Agente:** Modelo de IA especializado em função específica dentro da arquitetura do produto.

**Contexto++:** Sistema de aprendizado contínuo que captura preferências do usuário ao longo do tempo para refinamento da personalização.

**Rascunho:** Formulário de ato de mandato parcialmente preenchido e salvo automaticamente para retomada posterior.

**Histórico:** Registro de conversas completas (incluindo entradas, conteúdo gerado e interações) que permite retomada de contexto.

**Guardrails:** Regras e validações que impedem uso inadequado, malicioso ou que viole termos de uso.

**MAU (Monthly Active Users):** Usuários ativos mensais, definidos como usuários únicos que geraram pelo menos um conteúdo no período de 30 dias.

**Churn:** Taxa de cancelamento de assinatura, representando percentual de usuários que deixam de usar o produto.

**MVP (Minimum Viable Product):** Versão mínima do produto com funcionalidades essenciais para validação da proposta de valor.

**n8n:** Plataforma de automação e orquestração que gerencia comunicação entre frontend, bancos de dados e agentes de IA.

---

## 19. Anexos

### 19.1 Schemas de Banco de Dados

*Schemas JSON fornecidos (autodiagnostico.schema.json e auditoria.schema.json) devem ser anexados a este documento como referência técnica para implementação do banco de DNA.*

### 19.2 Referências

**Metodologia de Comunicação:** Marcelo Vitorino, especialista em comunicação política com mais de 20 anos de experiência. Metodologia incorporada nas instruções do agente gerador de conteúdo.
