from flask import Flask
from .extensions import db
from .routes import main_bp

def create_app():
    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vshyd@localhost:5432/museum_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main_bp)

    return app
