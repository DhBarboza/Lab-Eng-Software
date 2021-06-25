# Configurações

## Requerimentos mínimos
- Python V3.6 ou Maior
- MySQL Database

## Inicialização do ambiente

### Clonar e atualizar repositório

- git clone https://github.com/DhBarboza/Lab-Eng-Software.git
- cd app-recipe


### Instalando virtualenv

- pip install virtualenv


### Inicializando ambiente virtual
#### Linux:

- virtualenv -p python3 enviromment
- . env/bin/activate

#### Windows:
- python3 -m venv env
- env/Scripts/activate

### Instalação das dependências
- pip install -r requirements.txt


### Configuração do banco de dados:
- !Configure as credenciais de acordo com seu ambiente de de banco de dados MySQL!
- Configure a conexão com o MySQL no arquivo `.env` cria-lo na raiz do projeto:

    - Database => Nome do banco de Dados
    - Host => localhost || 127.0.0.1
    - Port => Utilize a porta padrão
    - Username => Nome de usuário do server 
    - Password => A senha do seu servidor

#### Exemplo:
```
MYSQL_DATABASE=cook
MYSQL_HOST=localhost
MYSQL_PORT=3306 
MYSQL_USERNAME=root 
MYSQL_PASSWORD=
```
- Assista o vídeo de demonstração e se atente a parte de configuração de banco de dados:
[Sistema - Build & Configuração](https://www.youtube.com/watch?v=dvlTRBLXBfo)

### Criando as tabelas
- rode um seu terminal o seguinte comando:
  - python wsgi.py create_db

### Executando a aplicação:
- python wsgi.py


