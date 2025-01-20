

from flask import current_app, g


def get_db():
    current_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/museum_db'


    return SQLAlchemy(app)