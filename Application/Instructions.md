## Instalar virtualenv:
- pip install virtualenv 

## Criar um ambiente virtual:
virtualenv -p python3 <nome_ambiente_virtual>
- Exemplo: virtualenv -p python3 environment

## Ativar ambiente virtual:
- environment/Scripts/activate

## instalar Flask:
- pip install flask

## instalar SQLAlchemy:
- pip install flask-sqlalchemy

## Verificar os pacotes instalados:
- pip freeze

## Executar a aplicação:
- python app.py

## Instalar Migrate:
- pip install flask-migrate

## Migrações:
- Criar pasta de Migrações com uma subpasta de versão:
    `flask db init`

- Detecta as mudanças do modelo com uma configuração de lógica de upgrade e downgrade:
    `flask db migrate`

- Aplicar as alterações do modelo que você implementou:
    `flask db upgrade``

- se algo der errado, você pode usar este comando para cancelar a aplicação das alterações feitas em seu arquivo de modelo:
    `flask db downgrade`


