from flask import jsonify
from marshmallow import ValidationError

from biblioteca_virtual.run import app


@app.errorhandler(ValidationError)
def handle_invalid_schema(error: ValidationError):
    errorMsgs = error.normalized_messages()
    return jsonify(errorMsgs), 400