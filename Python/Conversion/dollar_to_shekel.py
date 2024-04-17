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
app.debug=False

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


@app.route('/', methods=['POST'])
def convert_dollar_to_shekel():
    data = request.get_json()
    error = None
    if not data or not data.get('value'):
        error = "Missing value"

    if not error:
        value = str(data.get('value'))
        if not isfloat(value):
            error = 'Value not numeric'
    if error:
        return jsonify({'results': 0, 'error': error}), 400

    res = round(float(value) * conversions.get('dollar_shekel'), 2)
    return jsonify({'results': res}), 200


app.run(host="0.0.0.0", port=PORT)
