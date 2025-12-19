# Eleições Bluesky

Resultado da eleição no Brasil para Bluesky

Assista a live no [YouTube](https://www.youtube.com/live/8vmFdQvXerY)

Especificação `EA20 – Arquivo de resultado unificado` em [TSE](https://www.tse.jus.br/eleicoes/informacoes-tecnicas-sobre-a-divulgacao-de-resultados)

Arquivo de configuração de playground da API para [Insomnia](https://insomnia.rest/) em `Insomnia_2024-09-14.json`

## Instalação

Este projeto usa [Python](https://www.python.org) e [pip](https://pypi.org)

```bash
# apt install -y python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev
```

```bash
$ python3 -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

## Configuração

Em sua conta no [Bluesky](https://bsky.app/), crie uma senha de aplicativo em `https://bsky.app/settings/app-passwords`

Defina as variáveis do ambiente `BASE_URL`, 'LOGIN' e `PASSWORD`, veja o arquivo [env-sample](env-sample) em seguida renomeie o arquivo para `.env`

```bash
export BASE_URL="https://bsky.social"
export LOGIN=""
export PASSWORD=""
```

## Execução

Se você não receber mensagem, deu tudo certo!

```bash
$ source .env
$ python3 main.py
```
