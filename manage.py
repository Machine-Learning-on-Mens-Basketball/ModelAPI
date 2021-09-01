import os
from flask import Flask
from flask_restful import Api, Resource
from app.main.controllers.basic_model_controller import BasicModelController

app = Flask(__name__)
api = Api(app)

api.add_resource(BasicModelController, '/basicModel')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)