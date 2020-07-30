[![Build Status](https://travis-ci.org/labhackercd/linguagem-simples-backend.svg?branch=master)](https://travis-ci.org/labhackercd/linguagem-simples-backend)
[![Coverage Status](https://coveralls.io/repos/github/labhackercd/linguagem-simples-backend/badge.svg?branch=master)](https://coveralls.io/github/labhackercd/linguagem-simples-backend?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/b9acb360efb6bc65f182/maintainability)](https://codeclimate.com/github/labhackercd/linguagem-simples-backend/maintainability)


# Linguagem Simples Backend
Este repositório contém o código referente ao backend da aplicação Linguagem Simples. Para mais informações sobre a ferramenta acesse a nossa wiki. Para ter acesso a toda [documentação](https://github.com/labhackercd/linguagem-simples-backend/wiki) que explica questões de negócio bem como questões técnicas do projeto.


# Como iniciar o projeto?

## Pré-requisitos
É necessário ter intalado os seguintes softwares:
* [Docker](https://docs.docker.com/engine/install/) versão 19.03.6
* [Docker-Compose](https://docs.docker.com/compose/install/) versão 1.25.5

Caso deseje alterar as variáveis de ambiente é necessário alterar as variáveis que estão no **docker_compose.yml**. É possível alterar as
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

## Como rodar os testes do projeto
- Com os contaires(Passo 3) já em execução rode o comando:
```bash
sudo docker-compose exec backend sh -c "cd src/ && pytest --cov-report term-missing --cov=apps"
```

**A API neste momento já vai estar rodando na porta 8000 do localhost.**