from App import app
from flask import render_template

@app.route('/index/<user>')
@app.route('/', defaults={'user':None})
def index(user):
    return render_template('index.html', user=user)

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')
