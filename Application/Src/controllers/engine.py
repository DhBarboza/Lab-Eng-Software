from Src import app
from flask import Flask, render_template, request, redirect, url_for
from Src.models.tables import Receitas, Ingredientes

@app.route("/", methods=['GET'])
def index():
    database = Receitas.query.all()
    return render_template('index.html', database=database)