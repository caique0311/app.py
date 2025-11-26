# Architecture.md

## 1. Visão Geral

Este projeto é uma API em Flask que recebe perguntas via requisição POST
e envia essas perguntas para o modelo Gemini 1.5 Flash, retornando a
resposta gerada ao cliente.

## 2. Estrutura do Projeto

    /chat.ia
     ├── app.py            # API principal Flask
     ├── teste_env.py      # Script para testar leitura de variáveis do .env
     ├── .env              # Armazena GEMINI_API_KEY

## 3. Tecnologias Utilizadas

-   Python
-   Flask
-   dotenv
-   Requests
-   Google Gemini API

## 4. Variáveis de Ambiente

O arquivo `.env` contém:

    GEMINI_API_KEY=AIzaSyCLxMT--3X6EAfMKCb0mGtH9ZLsJGEq3JI

## 5. Fluxo da Aplicação

1.  O Flask inicia o servidor na porta 8080.
2.  O `.env` é carregado.
3.  A chave GEMINI_API_KEY é obtida.
4.  O usuário faz POST em `/ask`.
5.  O servidor monta o payload para Gemini.
6.  Envia a requisição para a Google API.
7.  Recebe a resposta e devolve em JSON.
8.  Em caso de falha, retorna mensagens de erro tratadas.

## 6. Componentes Principais

### app.py

-   Carrega `.env`
-   Valida a chave
-   Define rotas
-   Envia pergunta ao Gemini
-   Retorna JSON com a resposta

### teste_env.py

-   Testa se o `.env` está sendo carregado

### .env

-   Guarda a chave da API

## 7. Endpoints

### GET /

Retorna texto simples indicando que a API está online.

### POST /ask

Body JSON:

    { "question": "sua pergunta" }

Retorno:

    { "answer": "resposta gerada pelo Gemini" }

## 8. Como Rodar

    pip install flask python-dotenv requests
    python app.py
