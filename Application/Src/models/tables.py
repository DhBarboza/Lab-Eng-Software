from Src import db

class Ingredientes(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    ingrediente_name = db.Column(db.String(1000))

    def __init__(self, ingrediente_name):
        self.ingrediente_name = ingrediente_name

class Receitas(db.Model):
    __tablename__ = "receitas"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    receita = db.Column(db.String(150))
    ingrediente_id = db.Column(db.Integer, db.ForeignKey("ingredientes.id")) 

    ingrediente = db.relationship("Ingredientes", foreign_keys=ingrediente_id)

    def __init__(self, receita, ingredientes):
        self.receita = receita
        self.ingrediente_id = ingrediente_id

