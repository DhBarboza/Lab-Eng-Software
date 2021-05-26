from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector
from App.controllers import default
from App.models.tables import Receitas

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    receitas = Receitas.query.all()
    return render_template('index.html', receitas=receitas)



