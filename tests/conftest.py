"""
contains fixtures to be used in tests
"""
from os import path
from os.path import join, dirname
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
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

#Fixture for Firefox
@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    """
    Initiliaze driver for UI tests
    """
    if request.param == "chrome":
        #Local webdriver implementation
        #web_driver = webdriver.Chrome()
        #Remote WebDriver implementation
        web_driver = webdriver.Remote(command_executor='http://0.0.0.0:4444/wd/hub',
                                      desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    if request.param == "firefox":
     #Local webdriver implementation
        #web_driver = webdriver.Firefox()
        #Remote WebDriver implementation
        web_driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})
    request.cls.driver = web_driver
    yield
    web_driver.close()
