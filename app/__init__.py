from flask import Flask
from .models import db
from .config import Config
from .auth import auth_bp
from .routes import finance_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(finance_bp)

    return app
