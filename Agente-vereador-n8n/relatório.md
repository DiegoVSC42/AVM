# Relatório de conclusões

## Criação de agente Claude (GPT)

A Anthropic ainda não possui nenhum tipo de serviço próprio dedicado à criação de agentes, como os GPTs da OpenAI, porem, é possivel usar um modelo da Anthropic no N8N e chamá-lo em um GPT via API, porém o GPT passaria a ter custo de tokens.

## Hospedar os modelos nos nossos servidores

Nem toda empresa disponibiliza modelos de LLM para serem rodados localmente, a OpenAI é uma delas, a Anthropic(Claude) também. Outra questão sobre os modelos locais, é que eles são bastante pesados, então precisam de um servidor mais robusto, porém, não têm custo de tokens. O custo desse tipo de servidor está por volta de $1.671 /GPU contratada/hora.

Observações: De acordo com a política de privacidade da OpenAI e da Anthropic, os dados enviados para eles via API não são usados para treinamento dos modelos,ou seja, elas só guardam registros para saberem se o modelo delas está sendo usado para algo ilegal e para que o modelo possa raciocinar durantes os passos de uma tarefa. Existem servidores sem GPUs que podem hospedar LLMs tambem, são mais baratos, mas as LLMs que eles suportam não são tão robustas, servem apenas para tarefas simples.

## Uso do Manus para base de conhecimento

Na reunião foi sugerido o Manus para gerar dossiês para serem usados pelo sistema para dar melhor resposta para o cliente, porém até o momento, o Manus não possui API, então não seria possível utilizá-lo para esse fim no momento, mas a API deles está sendo desenvolvida e atualmente está em estado de beta fechado, em alguns meses deve ser disponibilzada para uso público.

## Consulta de bases de conhecimento

Atualmente o Gemini possui o melhor modelo para guardar/buscar dados em bases de conhecimento (RAG), poderia ser usado para colocar os documentos no banco de dados. Durante a reunião foi sugerido o uso do MySQL como banco de dados, porém, as LLMs usam um tipo de banco de dados diferente, chamado de banco de dados vetorial e o MySQL não serviria para esse caso, minha sugestão é utilizar o Supabase, ele basicamente é um PostgreSQL com recursos de bancos vetoriais e interface mais intuitiva.

## Observações sobre Custo de tokens

Criei um sistema simples que consigo comparar respostas de modelos diferentes que usam as mesmas instruções, fiz testes usando Claude,Gemini e ChatGPT, no geral o Claude foi bem melhor que os outros dois, porém ele tambem gastou mais tokens e o modelo é mais caro.

Custo Claude 4.5 Sonnet (estimado)
Qtd de mensagens	Custo total
1    mensagem	    $0,048
100  mensagens	    $4,800
1000 mensagens	    $48,00

Custo GPT 5 (estimado)
Qtd de mensagens	Custo total
1    mensagem	    $0,038
100  mensagens	    $3,00
1000 mensagens	    $30,00

## Sugestões de próximos passos

Pensei em desenvolver um sistema com 3 agentes, um agente de triagem, um agente de geração de conteúdo e um de analise factual

Agente de triagem: ele vai receber o texto do usuário e vai interpretar e definir qual o tipo de ato de mandato e qual o tipo de conteudo (post,reels,carrossel,etc), com esses dados ele vai encaminhar para campos com os textos das instrucoes de cada um, por exemplo, o usuário quer criar um carrossel de prestação de contas, esse agente vai pegar os dados do campo que contem instrucoes de carrossel e do campo que contem instrucoes de como deve ser uma prestação de contas, essas 2 instrucoes serão combinadas e utilizadas juntamente ao texto que o cliente mandou para enviar para o agente de geracao de conteudo como um prompt pronto. Dessa forma o agente sempre terá os dados certos de cada tipo de informação. Esse agente poderá usar um modelo simples e barato do GPT por exemplo, pois não precisará gerar nenhum tipo de texto, apenas organizar o fluxo do projeto. OBS.: Esse agente posteriormente pode ser excluido após implementação do sistemas de interação via botões, pois os dados do tipo de conteudo ja viriam dos botoes.

Agente de RAG: esse agente terá acesso aos dados dos documentos da empresa, (cursos,livros,etc), ele receberá a pergunta do usuário e buscará dados verificaveis sobre o assunto em questão, depois passar essas informações para o agente de geração de contaudo, ele também terá acesso ao json com as informações do usuário. Esse agente poderia utilizar o modelo de RAG do Gemini

Agente de geração de conteudo: Esse agente será o encarregado para gerar o conteudo completo de acordo com as instrucoes que estarão em seu prompt, como entrada ele vai receber a mensagem do usuario dizendo o tipo de conteudo que essa pessoa quer, as instrucoes corretas de como um conteudo desse tipo deve ser produzido, os fatos verificaveis vindos do RAG e o json com as informações do usuário para gerar uma resposta personalizada, dessa forma a chance de produzir um conteudo que não segue as instruções fica muito menor. Aqui entraria o modelo mais completo do Claude, para gerar o melhor tipo de conteúdo

Posteriormente pode ter um agente de checklists para verificar se os requisitos foram cumpridos de forma correta, essa agente poderia utilizar um modelo simples de GPT como o primeiro, para evitar custos desnecessários e também ter respostas mais rapidas.

## Observações sobre Modelos de  fallback (roda quando o outro dá problema)

Para o Agente de Claude poderia colocar um GPT como modelo de fallback
Para o Agente de RAG, poderia colocar um modelo Qwen como fallback (hoje em dia ele é considerado o segundo melhor)
Para o agente de triagem basicamente qualquer modelo conseguiria fazer fallback.