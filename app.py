import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from models import RequestParams
from query_builder import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = RequestParams().load(request.json)

    except ValidationError as error:
        return error.messages, 400

    result = build_query(
        cmd1=params['cmd1'],
        value1=params['value1'],
        cmd2=params['cmd2'],
        value2=params['value2']
    )

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=25000)
