from flask import current_app as app
from flask import jsonify, Flask
from app.main.exceptions.model_exception import ModelException

app = Flask(__name__)
with app.app_context():
    class InvalidTeamException(ModelException):
        @app.errorhandler(ModelException)
        def handle_invalid_team_exception(self):
            with app.app_context():
                error = 1
                message = "The team(s) provided were not valid"
                app.logger.warn("error: " + error + " message: " + message)
                data = {
                            'error': error,
                            'message': message
                        }
                return (data, 400)
                    