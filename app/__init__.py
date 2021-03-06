from flask import Flask
from flask_cors import CORS
from .config import config
from .models import db


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .controllers.main import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
