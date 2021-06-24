from Src import app
from flask import Flask, render_template, request, redirect, url_for
from Src.models.tables import Receitas, Ingredientes
from Src import db

@app.route("/", methods=['GET'])
def index():
    receitasdb = Receitas.query.all()
    return render_template('index.html', receitasdb=receitasdb)

@app.route("/ingredients", methods=['GET'])
def ingredients():
    ingredientsdb = Ingredientes.query.all()
    return render_template('ingredients.html', ingredientsdb=ingredientsdb)

@app.route("/add-ingredient", methods=['GET', 'POST'])
def add_ingredients():
    if request.method == 'POST':
        ingredientsdb = Ingredientes(request.form['ingrediente_name'])
        db.session.add(ingredientsdb)
        db.session.commit()
        return redirect(url_for('ingredients'))
    return render_template('add-ingredient.html')
