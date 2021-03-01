import pytest


@pytest.fixture()
def path_to_input_file():
    return 'tests/fixtures/test_input_file.txt'


@pytest.fixture()
def path_to_directory():
    return 'tests/fixtures/test_input_file.txt'


@pytest.fixture()
def correct_output():
    return 'tests/fixtures/correct_output.txt'
