Prompt for Lovable.ai: Eu Vereador AI Frontend Generation

1. Application Overview and Target Audience

Generate the frontend interface for a web application named "Eu Vereador AI".

Concept: An AI-powered communication assistant for Brazilian city councilors (Vereadores). It helps them generate personalized communication content based on their activities and profile (the "DNA").
Target Audience: Users with low technical literacy. They primarily use smartphones.
Core Philosophy: Extreme simplicity and Mobile-First design. The interface must be intuitive, similar to WhatsApp in simplicity.
Language: The entire application interface must be in Brazilian Portuguese (pt-BR).

2. Design System and Principles

The design must strictly adhere to the following guidelines.

A. Core Principles:

1. Mobile-First: Optimize everything for smartphone screens. Desktop is a responsive adaptation.
2. Extreme Simplicity: One primary action per screen. Clear, linear flows. No technical jargon.
3. Accessibility: High contrast, large and legible fonts, and large touch targets (buttons/links minimum 44x44px).
4. Feedback: Provide constant feedback to the user (loading states, success messages, clear error states).

B. Visual Identity:

Color Palette:
Primary Green: #36be72 (Primary CTAs, highlights)
Support Green 1: #0e8a45 (Hover states, secondary elements)
Support Green 2: #015242 (Subtle backgrounds, borders, dark elements)
Text Black: #000b05 (Primary text, high hierarchy)
Background White: #f1f2f1 (Main backgrounds)

Typography: Montserrat (Clear, modern, professional, highly legible).

Style: Clean, professional, and accessible. Use rounded corners for buttons, cards, and inputs (approx 8px radius). Ensure generous white space. Icons must be simple and clear.

3. Application Flows and Screen Details

A. Authentication (Login & Signup)

Description: Simple, clean mobile authentication screen.
Style Reference: Financial App UI Kit ([https://www.behance.net/gallery/185128703/Financial-App-UI-Kit?tracking_source=search_projects](https://www.behance.net/gallery/185128703/Financial-App-UI-Kit?tracking_source=search_projects)|onboarding+&l=108). Use the Eu Vereador AI color palette.
Fields: Email, Password.
Actions: Login (Entrar), Signup (Criar Conta), Forgot Password (Esqueci a senha). Signup must include a checkbox: "Concordo com os Termos de Uso e Política de Privacidade".

B. Onboarding Tutorial

Description: A 3-4 screen carousel/wizard shown after the first login.
Style Reference: POS AGENT BANKING FINTECH APP ([https://www.behance.net/gallery/235595739/POS-AGENT-BANKING-FINTECH-APP?tracking_source=search_projects%7Conboarding+ux](https://www.behance.net/gallery/235595739/POS-AGENT-BANKING-FINTECH-APP?tracking_source=search_projects%7Conboarding+ux)).
Screens:
1. Welcome: "Bem-vindo ao Eu Vereador AI, seu assistente de comunicação."
2. The "DNA": "Preencha seu DNA para receber conteúdo 100% personalizado ao seu mandato."
3. How it works: "Escolha o que fez -> Selecione onde publicar -> Receba o conteúdo pronto."
4. Let's Start: CTA "Construir DNA Agora" (Primary) and "Pular por enquanto" (Secondary).

C. Home Screen (Dashboard)

Description: The main hub. Action-oriented and clear.
Style Reference: AcDc portfolio website ([https://www.behance.net/gallery/231106213/AcDc-portfolio-website-for-a-craftsman-(electrician)?tracking_source=search_projects_views&l=4](https://www.behance.net/gallery/231106213/AcDc-portfolio-website-for-a-craftsman-(electrician)?tracking_source=search_projects_views&l=4)) (Focus on bold buttons, clear structure, and strong visual hierarchy).
Layout (Mobile):
1. Header: Logo ("Eu Vereador AI") center-aligned, Profile Icon (top right).
2. Primary Action: A large, full-width (minus padding) button at the top of the content area in Primary Green (#36be72): "Iniciar Comunicação".
3. DNA Block: A prominent card titled "Construir Biografia" (or "Seu DNA"). Shows a progress indicator (e.g., "40% Completo"). CTA button: "Completar/Editar DNA".
4. Rascunhos (Drafts): A section titled "Rascunhos". List items showing the Act type and date. (Include an empty state: "Você não possui rascunhos. Comece uma comunicação agora!").
5. Histórico (History): A section titled "Histórico". List items showing the Act type, channels used, and date. (Include an empty state: "Seu histórico de comunicações aparecerá aqui.").
6. Ferramentas Futuras (Placeholders): A section titled "Ferramentas". Display cards for future features (Bio, MiniBio, Alinhamento Ideológico, Resumo Estratégico, Análise de Discurso, Reescrita, Produção de Documentos Oficiais). Use icons and an "Em breve" label. Cards must be visually disabled (greyed out).

D. DNA Building (Profile Setup)

Description: A detailed, multi-step form wizard.
Style Reference: SaaS AI Product Dashboard Design (Form Filling) ([https://www.behance.net/gallery/193712057/SaaS-AI-Product-Dashboard-Design?tracking_source=search_projects%7Conboarding](https://www.behance.net/gallery/193712057/SaaS-AI-Product-Dashboard-Design?tracking_source=search_projects%7Conboarding)+).
Layout: A full-screen wizard (modal). It MUST be broken down into 12 steps (Blocks).
Steps:
1: Identificação Básica; 2: Perfil Pessoal; 3: Posicionamento Político; 4: Atuação Territorial; 5: Agenda Temática; 6: Estrutura e Canais; 7: Frequência e Planejamento; 8: Engajamento; 9: Prestação de Contas e Transparência; 10: Recursos de Produção; 11: Padronização; 12: Conformidade.
Features:
Clear progress bar at the top (e.g., "Passo 3 de 12" and percentage).
"Voltar" and "Avançar/Salvar Bloco" buttons at the bottom of each step.

E. Main Flow: Content Generation Wizard

This flow starts when the user clicks "Iniciar Comunicação".

Step 1: Selecionar Ato de Mandato (Select Legislative Act)
Layout: Full screen. Titled "O que você quer comunicar?". Display large, tappable cards or buttons (Use AcDc style).
Acts: Votações, Mobilização Social, Requerimento ao Executivo, Fiscalização, Tribuna, Leis, Atendimento de Gabinete, Orçamento, Eventos/Reuniões/Viagens, Prestação de Contas, Emendas. (User selects ONE).

Step 2: Selecionar Canais (Select Channels)
Layout: Full screen. Titled "Onde você vai publicar?". Checkbox list or multi-select toggle buttons.
Channels: Post Instagram/Facebook, Reels, Stories, TikTok, Site institucional, Roteiro YouTube. (User selects MULTIPLE).
CTA: "Avançar".

Step 3: Preencher Formulário Específico (Fill Specific Form)
Layout: A clean modal or full-screen form. Titled with the Act name (e.g., "Detalhes da Votação").
Fields (Example for Votações): "Qual o projeto votado?", "Qual foi seu voto? (A favor/Contra)", "Qual a sua justificativa principal?".
CTA: "Gerar Conteúdo".

Step 4: Geração (Loading State)
Layout: Full screen loading indicator. Must display dynamic, changing status messages (cycling through these):
"Analisando seu perfil e preferências..."
"Pensando na melhor forma de comunicar..."
"Gerando conteúdo personalizado..."
"Finalizando os detalhes..."

F. Main Flow: The Chat Interface (Results and Interaction)

Description: The screen where the AI presents the content and the user refines it.
Style Reference: Tania AI Assistant for Scientists ([https://www.behance.net/gallery/236591565/Tania-AI-Assistant-for-Scientists](https://www.behance.net/gallery/236591565/Tania-AI-Assistant-for-Scientists)) (Clean mobile chat UI, clear distinction between user input and AI response).
Layout: Standard chat interface.
AI Response Structure: The AI response must be structured.
1. A confirmation message (e.g., "Aqui estão as opções para [Ato X] nos canais [A, B, C].")
2. For EACH selected channel, present TWO distinct versions clearly labeled (e.g., "Instagram Post - Versão A" and "Instagram Post - Versão B").
3. Components for each version (in a card):
A text block containing the generated content.
"Copiar Conteúdo" (Copy) button.
"Preferir esta versão" (Prefer this version) button (e.g., Thumbs up icon). This is crucial for feedback.
4. After presenting the content, the AI should suggest next steps: e.g., "Gostaria de criar um [outro ato de mandato]?"

Interaction Area (Input):
At the bottom, a persistent input area.
MUST include: A text input field (Placeholder: "Peça um ajuste, ex: 'deixe mais curto'") AND a prominent Microphone icon button for Audio Recording input.
Send button.

G. Profile Area and Settings

Description: Accessed via the icon on the Home Screen Header.
Style Reference: Chat GPT Concept (Profile) ([https://www.behance.net/gallery/236562039/Chat-GPT?tracking_source=search_projects_comments](https://www.behance.net/gallery/236562039/Chat-GPT?tracking_source=search_projects_comments)|chat&l=24).
Layout: Simple list menu.
Options: Editar DNA, Meus Dados (Account Data), Assinatura (Subscription Management), Suporte (Help/Support - via WhatsApp), Termos de Uso, Sair (Logout).

H. Payments/Subscription Management

Description: Screen for managing the subscription.
Style Reference: Quantix (Payment interface) ([https://www.behance.net/gallery/236553871/Quantix-Crypto-Market-Analysis-Landing-Page](https://www.behance.net/gallery/236553871/Quantix-Crypto-Market-Analysis-Landing-Page)). Adapt to the green/black/white color palette.
Sections: Current Plan details (e.g., "Plano Mensal - R$ 297,00"), Payment History, Manage Payment Methods (Credit Card, PIX, Boleto), Cancel Subscription.

4. Desktop Adaptation

The application must be fully responsive.

Style References: Use Option 1: COGPT ([https://www.behance.net/gallery/236553163/AI-Chat-Design-COGPT?tracking_source=search_projects_comments%7Cchat](https://www.behance.net/gallery/236553163/AI-Chat-Design-COGPT?tracking_source=search_projects_comments%7Cchat)) for the general structure.
Layout Changes:
Implement a persistent left sidebar for main navigation (Início, Histórico, Rascunhos, DNA, Perfil).
The Home Screen content (DNA block, Future tools) should utilize a multi-column grid layout.
The Chat Interface should occupy the central area, potentially showing the History list in a panel alongside the chat (like COGPT reference).
Wizards (DNA, Content Generation) should be centered modals rather than full screen on desktop.

5. Public Landing Page (Pre-Login)

Description: A public-facing marketing website.
Style Reference: SaaS AI Chat Assistant Landing Page ([https://www.behance.net/gallery/235447125/SaaS-AI-Chat-Assistant-Landing-Page-UI-Design?tracking_source=search_projects_comments%7Cchat](https://www.behance.net/gallery/235447125/SaaS-AI-Chat-Assistant-Landing-Page-UI-Design?tracking_source=search_projects_comments%7Cchat)). Must use the defined visual identity (Montserrat, Green palette).
Sections:
Hero: Strong value proposition (e.g., "Comunicação política estratégica na palma da sua mão").
Problem/Solution: Addressing the communication challenges of councilors.
Key Features: (DNA Personalization, Strategic Methodology, Multi-channel content).
Pricing: Clear display of the plan (R$ 297,00/mês).
Footer: Links and contact.
Header CTA: "Login" and "Assinar Agora".