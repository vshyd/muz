

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


print('Hello World')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/museum_db'


db = SQLAlchemy(app)