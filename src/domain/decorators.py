import functools
from src.domain.helper import api_response

import traceback


def api_response_handler(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        # Do something with your request here
        status_code = 200
        try:
            body = f(*args, **kwargs)
            if type(body) is dict and "statusCode" in body.keys():
                status_code = body.get("statusCode")
            if type(body) is dict and "body" in body.keys():
                body = body.get("body")
            if status_code == 200:
                return body
        except Exception as err:
            print(traceback.format_exc())
            status_code = 500
            body = f"Unexpected {type(err).__name__}, {err}"
        return api_response(body, isinstance(body, (dict, list))), status_code

    return decorated_function
