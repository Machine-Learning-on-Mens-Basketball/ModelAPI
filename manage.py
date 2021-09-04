import os
import logging
from flask import Flask
from flask_restful import Api, Resource
from logging import Formatter
from logging.handlers import RotatingFileHandler
from app.main.controllers.basic_model_controller import BasicModelController

app = Flask(__name__)
api = Api(app)

api.add_resource(BasicModelController, '/predictBasicModel')
api.init_app(app)

if __name__ == '__main__':
    # formatter = logging.Formatter(
    #     "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    # handler = RotatingFileHandler('app/main/logs/modelAPI.log', maxBytes=10000, backupCount=1)
    # handler.setLevel(logging.DEBUG)
    # app.logger.addHandler(handler)
    # handler.setFormatter(formatter)
    # app.logger.addHandler()
    app.run(port=7000, debug=True)