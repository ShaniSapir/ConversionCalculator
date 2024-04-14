from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
PORT = os.getenv('PY_EURO_TO_SHEKEL_PORT')
if not PORT:
    raise RuntimeError('Missing port in .env')

app = Flask(__name__)

# Define a route for the GET request


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


@app.route('/', methods=['POST'])
def convert_euro_to_shekel():
    data = request.get_json()
    if not data:
        return jsonify({'result': 0}), 400

    value = str(data.get('value'))
    if value is None or not isfloat(value):
        return jsonify({'result': 0}), 400

    res = round(float(value) * 4.02, 2)
    return jsonify({'result': res}), 200


app.run(port=PORT)
