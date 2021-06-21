from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder="template")
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Src.controllers import engine