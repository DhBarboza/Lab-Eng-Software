from App import db

# Construindo as tabelas do Banco
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    ## Definir que os Campos sejam obrigatórios:
    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    ## Definir como a informação vai aparecer:
    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__ = 'posts'
