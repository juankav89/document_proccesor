import json
from src.domain.decorators import (
    api_response_handler
)
from src.domain.helper import api_response
import pytest
import traceback


def test_exception_handler():
    response = {'message': True}

    @api_response_handler
    def inner(*args, **kwargs):
        return response
    expected = api_response(True, False)
    assert expected == inner()


def test_api_response_handler_without_structure():

    body = 'true'

    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': 'true'
    }

    @api_response_handler
    def inner(*args, **kwargs):
        return response

    assert body == inner()


def test_api_response_handler_with_structure():

    body = {
        "status": True
    }

    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': f'{body}'
    }

    @api_response_handler
    def inner(*args, **kwargs):
        return body
    assert body == inner()


def test_api_response_handler_exception():
    error_message = "Error Message"

    @api_response_handler
    def inner_function(*args, **kwargs):
        raise Exception(error_message)

    class Example:
        pass

    context = Example()
    event = {}

    body = 'Unexpected Exception, Error Message'
    expected = api_response(body, False)
    obtained = inner_function(*[event, context])
    assert expected.get("statusCode",False) == obtained[0].get("statusCode", False)
    assert expected.get("headers",False) == obtained[0].get("headers", False)
    assert isinstance(obtained[0].get("message"),str)
