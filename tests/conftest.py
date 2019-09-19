"""
contains fixtures to be used in tests
"""
from os import path
from os.path import join, dirname
import json
import pytest
from src import create_app


@pytest.fixture(scope='module')
def test_client():
    """
    Yields a test_client to be used with each test
    """
    flask_app = create_app('testing')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def load_json_schema():
    """
    Reads the stored json schema file available at a given path
    """
    def _load_json_schema(filename):
        """ Loads the given schema file """
        relative_path = join('schemas', filename)
        absolute_path = join(dirname(__file__), relative_path)
        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())
    return _load_json_schema
    