from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config')

### Criar uma instância da classe recebendo o app
db = SQLAlchemy(app)
migrate = Migrate(app, db)

## Controlhe de execuções para passar na execução:
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from App.controllers import default
