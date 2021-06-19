from Src import db

class Receitas(db.Model):
    __tablename__ = "receitas"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    receita = db.Column(db.String(150))
    ingrediente_id = db.Column(db.Integer, db.ForeignKey("ingredientes.id")) 

    ingrediente = db.relationship("Ingredientes", foreign_keys=ingrediente_id)

    def __init__(self, receita, ingredientes):
        self.receita = receita
        self.ingrediente_id = ingrediente_id

class Ingredientes(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)

    def __init__(self, title, ingrediente_id):
        self.title = title