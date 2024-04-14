from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import json
# Load environment variables from .env file
load_dotenv()

# Get environment variables
CONFIGS_PATH = 'configs.json'
PORT = os.getenv('PY_EURO_TO_SHEKEL_PORT')
if not PORT:
    raise RuntimeError('Missing port in .env')

with open(CONFIGS_PATH, mode='r') as f:
    conversions: dict = json.load(f).get('conversions')
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
        return jsonify({'results': 0}), 400

    value = str(data.get('value'))
    if value is None or not isfloat(value):
        return jsonify({'results': 0}), 400

    res = round(float(value) * conversions.get('euro_shekel', 4), 2)
    return jsonify({'results': res}), 200


app.run(port=PORT)
