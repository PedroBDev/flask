from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'#configurando e criando caminho do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #desablitando checagem(aumentar a produção)   
app.config['SECRET_KEY'] = 'UASASJADKQPWD921-DASJ!!!DHADÇLFKJ3'

db= SQLAlchemy(app)#criando banco de dados
migrate=Migrate(app, db)#configurand migrate(utilizado para realizar as modificações no db)

from app.routes import homepage
from app.models import Contato