from flask import jsonify, make_response, Flask
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


def success_response(*args, **kwargs):
    success_message = 'OK'
    response = {
        'message': success_message
    }
    if kwargs:
        response.update({key: kwargs[key] for key in kwargs})
    return make_response(jsonify(response))

def error_response(error=None):
    error_message = 'Something went wrong'
    response = {'success': False, 'message': error if error else error_message}
    return make_response(jsonify(response))


class CustomValidationError(HTTPException):
    status_code = 400
    default_message = 'Not found'
    debug: tuple = None

    def __init__(self, msg=None, code=None):
        response = {
            'success': False,
            'code': code if code else self.status_code,
            'message': msg if msg else self.default_message
        }
        if msg is not None:
            response = jsonify(response)
        super().__init__(response=response)


@app.errorhandler(CustomValidationError)
def handle_custom_validation_error(error):
    response = jsonify(error.description)
    response.status_code = error.code
    return response