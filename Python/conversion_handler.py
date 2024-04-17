import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

LOCALHOST = 'http://127.0.0.1:%s'


def create_payload(value):
    return {'value': value}


class Converter:
    ports = {'py_dollar_shekel': os.getenv('PY_DOLLAR_TO_SHEKEL_PORT'),
             'py_euro_shekel': os.getenv('PY_EURO_TO_SHEKEL_PORT'),
             'default_handler': os.getenv('JS_HANDLER_PORT')}

    @classmethod
    def general_conversion(cls, conversion, value):
        payload = create_payload(value)
        try:
            url = LOCALHOST % cls.ports["py_" + conversion]
            req = requests.post(url, json=payload)
        except:
            req = None

        request_failed = req is None or not req.ok
        if request_failed:
            try:
                url = (LOCALHOST %
                       cls.ports['default_handler']) + "/" + conversion
                new_req = requests.post(url, json=payload)
                if new_req:
                    req = new_req
            except:
                pass
            request_failed = req is None or not req.ok
            if request_failed:
                return req.json().get('error', 'Error') if req is not None else 'Server not found'
        return req.json().get('results')

    @classmethod
    def dollar_to_shekel(cls, value):
        return cls.general_conversion('dollar_shekel', value)

    @classmethod
    def euro_to_shekel(cls, value):
        return cls.general_conversion('euro_shekel', value)

    @classmethod
    def pound_to_shekel(cls, value):
        return cls.general_conversion('pound_shekel', value)

    @classmethod
    def yen_to_shekel(cls, value):
        return cls.general_conversion('yen_shekel', value)

    @classmethod
    def rupee_to_shekel(cls, value):
        return cls.general_conversion('rupee_shekel', value)

    @classmethod
    def wan_to_shekel(cls, value):
        return cls.general_conversion('wan_shekel', value)

