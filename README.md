# Sistema de Registro de Animais

Este projeto é um sistema de registro de animais desenvolvido em Python com FastAPI para o backend e SQLite como banco de dados. Ele permite que os usuários registrem características dos animais, como número de registro, sexo, idade e qualidade, e armazena essas informações no banco de dados.

## Visão Geral

### Este sistema permite que um usuário:

Cadastre um animal no banco de dados informando suas características.
Visualize todos os animais cadastrados.

## Instalação

Clone o repositório e entre na pasta do projeto:
```bash
git clone https://github.com/psurreaux/sistema-registro-animais.git
cd sistema-registro-animais
```

Instale as dependências:
```bash
pip install fastapi uvicorn
```

Crie o banco de dados e a tabela 'animais':
```bash
python setup_database.py
```

Inicie a aplicação:
```bash
uvicorn main:app --reload
```

## Como usar
Abra http://127.0.0.1:8000/docs em seu navegador para acessar a interface interativa da API.
Utilize os endpoints POST /animais/ para registrar um novo animal e GET /animais/ para visualizar todos os animais cadastrados.

## Endpoints
POST /animais/: Registra um novo animal
GET /animais/: Lista todos os animais


## Tecnologias Usadas

Python: Linguagem principal do projeto.
FastAPI: Framework para construção da API.
SQLite: Banco de dados leve e fácil de configurar.
Uvicorn: Servidor ASGI para rodar o FastAPI.