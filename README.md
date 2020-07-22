[![Build Status](https://travis-ci.org/labhackercd/linguagem-simples-backend.svg?branch=master)](https://travis-ci.org/labhackercd/linguagem-simples-backend)

[![Coverage Status](https://coveralls.io/repos/github/labhackercd/linguagem-simples-backend/badge.svg?branch=master)](https://coveralls.io/github/labhackercd/linguagem-simples-backend?branch=master)

# linguagem-simples
Este repositório o projeto Linguagem Simples


# Como iniciar o projeto?

## Pré-requisitos
É necessário ter intalado os seguintes softwares:
* [Docker](https://docs.docker.com/engine/install/) versão 19.03.6
* [Docker-Compose](https://docs.docker.com/compose/install/) versão 1.25.5

Caso deseje alterar as variáveis de ambiente é necessário criar um arquivo com o nome .env na pasta em que se encontra o arquivo settings.py. É possível alterar as
seguintes variáveis:

```bash
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
HOST=
PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
PGDATA=
DATABASE_ENGINE=
```

## Comandos para executar o projeto
1. Clone o projeto
```bash
git clone https://github.com/labhackercd/linguagem-simples-backend.git
```
2. Entre dentro da pasta raiz do projeto
```bash
cd linguagem-simples-backend
```

3. Execute o comando para iniciar os containers 
```bash
sudo docker-compose up
```

**A API neste momento já vai estar rodando na porta 8000 do localhost.**