
import pytest

from src.domain.helper import load_json
from src.application.reader import Reader


@pytest.fixture
def db_information():
    return load_json("test/_fixtures/root_document.json")

@pytest.fixture
def specific_data():
    return load_json("test/_fixtures/subtitle_2_data.json")


def create_assert_object(mocker, db_information):
    mocker_obj = mocker.Mock()
    return Reader(db=db_information)


def test_return_all_data(mocker, db_information):
    assert_object = create_assert_object(mocker, db_information)
    query_params = {'section': 'root_document'}
    assert assert_object.get_document(query_params) == db_information


# def test_return_specific_data(mocker, db_information, specific_data):
#     assert_object = create_assert_object(mocker, db_information)
#     query_params = {'section': 'root_document.subtitle_2'}
#     assert assert_object.get_document(query_params) == specific_data
