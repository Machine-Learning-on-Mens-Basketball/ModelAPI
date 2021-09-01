from app.main.exceptions.invalid_team_exception import InvalidTeamException
from app.main.models.basic_model_response_DTO import BasicModelResponseDTO

class BasicModelService():

    def __init__(self):
        pass

    #Service for making a prediction
    def get_basic_model(self):
        model_response = BasicModelResponseDTO()
        # Need to actually get the model here and return it
        # For now, return fake json
        return {'message': 'yooo'}

        # new_prediction = PredictionModelDAO()
        # new_prediction.set_team1_name(team1)
        # new_prediction.set_team2_name(team2)
        # #Need to implement prediction models here...
        # #Returning fake results for now...
        # result_prediction = PredictionResponseDTO()
        # result_prediction.set_team1_name(team1)
        # result_prediction.set_team2_name(team2)
        # result_prediction.set_team1_percent("0%")
        # result_prediction.set_team2_percent("100%")
        # return result_prediction.generate_response()