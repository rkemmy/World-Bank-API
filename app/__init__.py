import os

from flask import Flask
from instance.config import app_config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    return app