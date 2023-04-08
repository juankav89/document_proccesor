import pytest
from requests.exceptions import RequestException

from src.domain.helper import load_json
from src.application.reader import Reader


@pytest.fixture
def db_information():
    return load_json("test/_fixtures/full_data.json")


@pytest.fixture
def root_document():
    return load_json("test/_fixtures/root_document.json")


@pytest.fixture
def specific_data():
    return load_json("test/_fixtures/subtitle_2_data.json")


def create_assert_object(mocker, db_information):
    # mocker_obj = mocker.Mock() # only used if connect to third party system
    return Reader(db=db_information)


def test_get_root_document(mocker, root_document, db_information):
    assert_object = create_assert_object(mocker, db_information)
    query_params = {'section': 'root_document'}
    assert assert_object.get_document(query_params) == root_document


def test_get_specific_data(mocker, db_information, specific_data):
    assert_object = create_assert_object(mocker, db_information)
    query_params = {'section': 'root_document.subtitle_2'}
    assert assert_object.get_document(query_params) == specific_data


def test_get_error_not_data(mocker, db_information):
    assert_object = create_assert_object(mocker, db_information)
    query_params = {'section': 'not_exist_data.subtitle_1'}
    __assert_value = "'not_exist_data' does not exist"
    assert assert_object.get_document(query_params)["body"] == __assert_value
