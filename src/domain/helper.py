import json


def load_json(file_name=str):
    """Class to load files"""
    f = open(file_name)
    data = json.load(f)
    f.close()
    return data


def api_response(body, as_json=False):
    """Format api response into cases without valid response"""
    return {
        "message": json.dumps(body) if as_json else body,
    }