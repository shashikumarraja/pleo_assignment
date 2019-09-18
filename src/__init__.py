from flask import Flask
from src.app import app
from instance.config import app_config

######################################
#### Application Factory Function ####
######################################

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    return app
    