from flask import request, current_app as app
from flask_restful import Resource, request

from app.main.services.basic_model_service import BasicModelService

#Prediction endpoint
class BasicModelController(Resource):
    def __init__(self):
        pass

    #Make a prediction
    def get(self):
        model = BasicModelService()
        return model.get_basic_model()