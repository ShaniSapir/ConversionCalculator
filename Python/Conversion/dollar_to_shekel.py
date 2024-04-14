from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Get environment variables
PORT = os.getenv('PY_DOLLAR_TO_SHEKEL_PORT')
CONFIGS_PATH = 'configs.json'
if not PORT:
    raise RuntimeError('Missing port in .env')


with open(CONFIGS_PATH, mode='r') as f:
    conversions: dict = json.load(f).get('conversions')

app = Flask(__name__)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


@app.route('/', methods=['POST'])
def convert_dollar_to_shekel():
    data = request.get_json()
    if not data:
        return jsonify({'results': 0}), 400

    value = str(data.get('value'))
    if value is None or not isfloat(value):
        return jsonify({'results': 0}), 400

    res = round(float(value) * conversions.get('dollar_shekel', 3.7), 2)
    return jsonify({'results': res}), 200


app.run(port=PORT)
