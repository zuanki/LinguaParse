from flask import Flask
from app.api.routes import register_routes
from app.models.base import db
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    print(app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    register_routes(app)
    return app
