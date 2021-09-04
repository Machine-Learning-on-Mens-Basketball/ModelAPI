from flask import request, current_app as app
from flask_restful import Resource, request

from app.main.services.basic_model_service import BasicModelService

#Prediction endpoint
class BasicModelController(Resource):
    def __init__(self):
        pass

    #Make a prediction
    def get(self):
        team1 = request.args.get('team1')
        team2 = request.args.get('team2')
        model = BasicModelService()
        return model.basic_model_prediction(team1, team2)