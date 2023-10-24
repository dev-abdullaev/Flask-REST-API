"""
This module contains utility functions and custom error handling for the application.
"""

from flask import jsonify, make_response, Flask
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


def success_response(**kwargs):
    """
    Generates a success response with optional additional data.

    Args:
        *args: Additional positional arguments (not used).
        **kwargs: Additional keyword arguments for custom response data.

    Returns:
        Response: JSON response containing success message and optional additional data.
    """

    success_message = 'OK'
    response = {
        'message': success_message
    }
    if kwargs:
        for key, value in kwargs.items():
            response.update({key: value})
    return make_response(jsonify(response))

def error_response(error=None):
    """
    Generates an error response with an optional error message.

    Args:
        error (str, optional): Custom error message. Defaults to None.

    Returns:
        Response: JSON response containing error message.
    """

    error_message = 'Something went wrong'
    response = {
        'success': False, 
        'message': error if error else error_message
    }
    return make_response(jsonify(response))


class CustomValidationError(HTTPException):
    """
    Custom exception class for validation errors.

    Attributes:
        status_code (int): HTTP status code for the error.
        default_message (str): Default error message.
        debug (tuple): Debug information (not used).
    """

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
    """
    Custom error handler for handling instances of CustomValidationError.

    Args:
        error (CustomValidationError): The CustomValidationError instance raised in the application.

    Returns:
        Response: A JSON response containing the error description and status code.
    """
    response = jsonify(error.description)
    response.status_code = error.code
    return response