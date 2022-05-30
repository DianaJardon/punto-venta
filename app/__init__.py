"""
    The following script contains the set-up and creation for the app
    - database object
    - login object

"""
# absolute imports
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# relative imports
from config import config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(type_config):
    app = Flask(__name__)
    app.config.from_object(config[type_config])
    config[type_config].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "Debes iniciar sesion para acceder a este sitio"
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)
    from app import models
    from .auth import auth as auth_blueprint
    from .inventory import inventory as inventory_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(inventory_blueprint)
    return app
