# Passo a Passo ChatBot EVM

1 - Recebe a mensagem da pessoa interessada no curso
2 - Verifica se a mensagem foi enviada em horário comercial, se sim o fluxo continua, se não recebe a mensagem ja configurada
3 - Verifica se a mensagem foi feita por alguem do 2020 (para bloquear ou desbloquear um numero para o bot), caso não tenha sido Verifica se a pessoa está bloqueada, se estiver não responde
4 - Se a pessoa do numero com final 2020 mandar algo que não seja "desbloquear" ou "bloquear" o bot responde com uma mensagem padrão
5 - Verifica se a pessoa está no banco de dados, se estiver, extrai os dados dela (nome caso ela tenha informado e telefone)
6 - Verifica o tipo de midia, se for algo diferente de um texto, uma IA faz a descrição da mídia para que as outras IAs entendam como mensagem
7 - Uma IA analisa a mensagem da pessoa verificando se ela informou seu nome na mensagem
8 - Os dados da pessoa sao salvos no banco de dados
9 - Uma IA analisa a mensagem da pessoa e corrige a mensagem para que fique melhor adaptada para a IA humanizadora
10 - Outra IA verifica se a mensagem enviada é sobre o curso e também se é genérica, de forma a melhorar a resposta da IA humanizada e tambem evitar consultas desnecessárias a base de informações
11 - Caso a mensagem seja relacionada ao curso, uma IA busca na base de dados as informações mais relevantes para responder a dúvida da pessoa
12 - Utilizando a consulta na base de dados e a mensagem corrigida, uma IA analisa se é necessário um humano, isso se aplica para os seguintes casos
    - A consulta na base de dados não conseguiu encontrar uma resposta adequada
    - A pessoa quer se inscrever via nota de empenho
    - A pessoa compartilhou informações sensíveis (cartão de crédito, CPF, etc)
    - A pessoa está irritada/agressiva
    - A pessoa pediu para falar com um humano
    - A pessoa quer efetuar transferência de inscrição para outra pessoa
    - A pessoa precisa de algum arquivo para algo (como uma carta proposta para enviar para a camara)
    - A pessoa quer efetuar reembolso
    - A pessoa pediu para que liguem para ela
13 - Após a IA humanizada responder a pessoa, a mensagem passa por outra IA para adicionar informações como saudação, falar nome, perguntar nome(caso seja a primeira mensagem da pessoa), falar (oi,olá, etc) caso seja a primeira mensagem do dia.
14 - Se a IA não conseguir responder a pessoa, a mensagem é encaminhada para um humano via numero de final 2020 para humano de mesmo número passando a mensagem que ela nao conseguiu responder e o contato da pessoa que nao foi respondida, tambem é bloqueada automaticamente para nao responder essa pessoa novamente até ser desbloqueada
15 - Se a IA conseguir responder a pessoa, a mensagem é enviada para outra IA que fragmenta o texto em partes menores, esse texto fragmentado é enviado para o usuário como varias mensagens menores.
16 - Caso a pergunta nao possa ser respondida e seja fora de horário comercial, a IA diz que um humano entrará em contato em breve
