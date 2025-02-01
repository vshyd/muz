from flask import Flask, session
from .extensions import db
from .blueprints.main import main_bp
from .blueprints.admin import admin_bp
from .blueprints.auth import auth_bp
from dotenv import load_dotenv
import os 


def create_app():
    app = Flask(__name__)
    load_dotenv()
    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'dev'

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)

    @app.context_processor
    def inject_user():
        user = None
        if 'user_id' in session:
            user = {
                'id': session['user_id'],
                'username': session['username']
            }
        return {'current_user': user}

    return app
