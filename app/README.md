## Executando o projeto em sua máquina (command line/terminal)

### 1° - Clone o repositório:
        - git clone https://github.com/DhBarboza/Lab-Eng-Software.git

### 2° - Navegue até a pasta `app`:
        - cd app

### 3° - Crie e inicialize seu ambiente virtual (virtualenv):
#### Instalando Pacote:
        - pip install virtualenv

#### Setup de configuração `MacOS/Linux`:
        - Criar:
            $ virtualenv -p python3 venv

        - Acessar:
            $ . venv/bin/activate

#### Setup de configuração `Windowns`:
        - Criar:
            > py -3 -m venv venv
            ou
            > python3 -m venv venv

        - Acessar:
            > venv\Scripts\activate
    
#### Ou siga documentação:
    - [Virtualenv](https://flask.palletsprojects.com/en/2.0.x/installation/)

### 4° - Instale as dependencias contidas no arquivo `requeriments.txt`:
        - > pip3 install -r requeriments.txt

### 5° - No arquivo `app.py` alterar a váriavel de ambiente de acordo com sua configurações:
#### ! - É importante que crie o a tabela antes de seguir os passos.

        - No arquivo está configurado assim:
            app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/recipe'

        - Mas altere de acordo com sua configurações.

        - Caso vá usar 'MySQL' configure de acordo:
            mysql://username:password@server/db
        
        - db => Nome da tabela que você criou (CREATE TABLE <nome_da_tabela>;)

    Para demais configurações acesse: 
        - [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)

### 6° - Para executar o projeto execute o comando a seguir na raiz da pasta `app`:
        - > python app.py

### 7° - Caso de algum erro:
- Verifique os passos anterios 
- Verifique sua váriavel de conexão com banco de dados
- Certifique-se que a conexão esteja correta e sem anormalidades

### 8° - Para mais detalhes sobre a Biblioteca acesse:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask&SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)





