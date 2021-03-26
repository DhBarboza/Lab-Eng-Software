from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

### Passando configuração de Banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
### Criar uma instância da classe recebendo o app
db = SQLAlchemy(app)

from App.controllers import default
