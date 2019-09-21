"""
contains fixtures to be used in tests
"""
import os
from os import path
from os.path import join, dirname
import json
import pytest
import logging
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from time import sleep
from src import create_app

logger = logging.getLogger(__name__)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """ create and set allure report directory to store test run result
    """
    if config.option.allure_report_dir is None:
        directory = join(os.getcwd(), 'tests/reports/')
        if not path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as error:
                logger.error(error)
                raise Exception('Unable to create report dir:%s' % error)
        config.option.allure_report_dir = directory
    else:
        logger.info('Report path already set!!!')

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
        if path.exists(absolute_path):
            with open(absolute_path) as schema_file:
                return json.loads(schema_file.read())
        else:
            logger.error('Invalid schema file path: %s' % absolute_path)
    return _load_json_schema

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    """
    Initiliaze driver for UI tests
    """
    if request.param == "chrome":
        #Remote WebDriver implementation for chrome
        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    if request.param == "firefox":
        #Remote WebDriver implementation for firefox
        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

    request.cls.driver = web_driver
    request.cls.explicit_wait_time = 10
    yield

    web_driver.close()
    web_driver.quit()

@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope='function', autouse=True)
def take_screeshot_on_test_fail(request):
    def test_result():
        if request.node.rep_setup.failed:
            print ("setting up a test failed!", request.node.nodeid)
            allure.attach(request.cls.driver.get_screenshot_as_png(), name=str(request.node.nodeid), attachment_type=AttachmentType.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                print ("executing test failed", request.node.nodeid)
                allure.attach(request.cls.driver.get_screenshot_as_png(), name=str(request.node.nodeid), attachment_type=AttachmentType.PNG)
    request.addfinalizer(test_result)
