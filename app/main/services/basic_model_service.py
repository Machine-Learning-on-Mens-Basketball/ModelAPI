from app.main.exceptions.invalid_team_exception import InvalidTeamException
from app.main.models.basic_model_response_DTO import BasicModelResponseDTO

class BasicModelService():

    def __init__(self):
        pass

    #Service for making a prediction
    def basic_model_prediction(self, team1, team2):
        # Need to actually use model here and return results
        # Returning dummy prediction for now...
        if (team1 == None or team2 == None):
            raise InvalidTeamException()
        else:
            model_response = BasicModelResponseDTO()
            model_response.set_team1_name(team1)
            model_response.set_team2_name(team2)
            model_response.set_team1_percent('100%')
            model_response.set_team2_percent('0%')
            return model_response.generate_response()