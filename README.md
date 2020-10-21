[![Build Status](https://travis-ci.org/labhackercd/linguagem-simples-backend.svg?branch=master)](https://travis-ci.org/labhackercd/linguagem-simples-backend)
[![Coverage Status](https://coveralls.io/repos/github/labhackercd/linguagem-simples-backend/badge.svg?branch=master)](https://coveralls.io/github/labhackercd/linguagem-simples-backend?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/b9acb360efb6bc65f182/maintainability)](https://codeclimate.com/github/labhackercd/linguagem-simples-backend/maintainability)

# linguagem-simples

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/labhackercd/linguagem-simples-backend/">
    <img src="https://i.ibb.co/tYd2fq2/acompanhe.png" alt="acompanhe" border="0">
  </a>
</p>

## Sobre o projeto

<center><img src="https://media.giphy.com/media/GDzLnVXvO67Q0hTloy/giphy.gif"></center>

O projeto Linguagem Simples (posteriormente renomeado para Plenário Simples) é uma iniciativa do <a href="http://labhackercd.leg.br">Laboratório Hacker da Câmara dos Deputados</a> para tornar mais fácil a compreensão da rotina dos deputados e das discussões que acontecem no plenário da Câmara, por meio de uma linha do tempo que cobre os eventos que acontecem no plenário da câmara em tempo real. Este repositório contém o código **de back-end** da plataforma que permite aos jornalistas da Casa inserir novas atualizações na linha do tempo. Além disso, este é um projeto derivado dos levantamentos feitos durante o <a href="https://medium.com/labhacker/eu-tu-ela-ele-n%C3%B3s-planejamos-266deed2ddfb?source=collection_home---5------9-----------------------"> Nós do Lab </a>, respondendo aos desafios levantados pela sociedade para a gestão de transparência, participação e cidadania do legislativo brasileiro.

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

## Como verificar a integridade dos serviços 
- É possível verificar como estão os status do serviço que o projeto Linguagem simples depende no seguinte link:
  - http://localhost.com/health_system/?wt=key
* Lembrando que é preciso configurar na variável **WATCHMAN_TOKENS** do arquivo **settings.py** qual será o token necessário para acessar essa página
![](https://raw.githubusercontent.com/wiki/labhackercd/linguagem-simples/images/README/health_system.png)

**A API neste momento já vai estar rodando na porta 8000 do localhost.**

## Documentação 

Devido a arquitetura escolhida pela equipe (com front e backend desacoplados entre si), e por uma questão de organização, o desenvolvimento deste projeto utilizou a metodologia ágil Scrum, e os documentos gerados podem ser acessados na nossa <a href="https://github.com/labhackercd/linguagem-simples-backend/wiki"> Wiki </a>

<hr>

## About the project

<center><img src="https://media.giphy.com/media/GDzLnVXvO67Q0hTloy/giphy.gif"></center>

The Linguagem Simples (<i>Plain Language</i>) project (which was later rebranded to Plenário Simples (<i> Simple Plenary </i>) is an initiative of the <a href="http://labhackercd.leg.br">National Congress Of Brazil's Laboratório Hacker</a> (<i> Hacker Lab </i>) to make understanding of the day-to-day routine of the representatives and discussions of the brazilian legislative house more accessible to citizens by providing them with an easy-to-understand timeline of events happening in plenary's sessions. This repo contains **the back-end** code for the platform which allows in-house journalists to update the timeline with content (such as text, image, tweets and so on) that allow for citizens to have a better understanding of the law-making process. This project derives directly from the 
<a href="https://medium.com/labhacker/eu-tu-ela-ele-n%C3%B3s-planejamos-266deed2ddfb?source=collection_home---5------9-----------------------"> Nós do Lab </a> event, which engaged multiple sectors of the society to help us disrupt the work processes behind the Brazilian Legislative House with a focus on transparency, participation and citizenship.

## Pre-requisites

In order to run the project via Docker the following software packages need to be installed:
* [Docker](https://docs.docker.com/engine/install/) versão 19.03.6
* [Docker-Compose](https://docs.docker.com/compose/install/) versão 1.25.5

Should you need to change values for environment variables, the following are available in the **docker_compose.yml** file:

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

## How to run the project

1. Clone this repo
```bash
git clone https://github.com/labhackercd/linguagem-simples-backend.git
```
2. Enter the project's root directory
```bash
cd linguagem-simples-backend
```

3. Start up the docker instance
```bash
docker-compose up
```

4. To run the development version, run the following command
```bash
docker-compose up dev
```
**How to run tests.**

- run the following command when the Docker container is already up:
```bash
sudo docker-compose exec backend sh -c "cd src/ && pytest --cov-report term-missing --cov=apps"
``` 

## Documentation

Due to the decoupled architecture chosen by team (with separate repositories for back and front-end code) and to the use of the SCRUM agile methodology, the documentation of this project happened in our <a href="https://github.com/labhackercd/linguagem-simples-backend/wiki"> Wiki </a>

