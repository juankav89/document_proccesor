import pytest
from src.domain.helper import load_json
from src.application.writer import Writer


@pytest.fixture
def db_information():
    return load_json("test/_fixtures/full_data.json")


@pytest.fixture
def new_data():
    return load_json("test/_fixtures/new_data.json")


@pytest.fixture
def new_section():
    return load_json("test/_fixtures/new_section.json")


@pytest.fixture
def new_document():
    return load_json("test/_fixtures/new_document.json")


def create_assert_object(mocker, db_information):
    # mocker_obj = mocker.Mock() # only used if connect to third party system
    db_information.pop(1)  # remove another_document fixture data
    return Writer(db=db_information)


def test_post_new_data(mocker, new_data, db_information):
    assert_object = create_assert_object(mocker, db_information)
    body_data = {
      "path": "root_document.subtitle_2",
      "name": "my_new_section",
      "text": "Text for my new section"
    }
    assert "ok" == assert_object.add_document(body_data)
    print(db_information)
    print(new_data)
    assert db_information == new_data


def test_post_new_section(mocker, new_section, db_information):
    assert_object = create_assert_object(mocker, db_information)
    body_data = {
      "path": "root_document.feb",
      "name": "orange",
      "text": "my cool section"
    }
    assert "ok" == assert_object.add_document(body_data)
    assert db_information == new_section


def test_post_new_document(mocker, new_document, db_information):
    assert_object = create_assert_object(mocker, db_information)
    body_data = {
      "path": "another_document",
      "name": "one",
      "text": "text for one section"
    }
    assert "ok" == assert_object.add_document(body_data)
    assert db_information == new_document
