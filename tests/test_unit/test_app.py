"""
Unit tests for app.py module
"""
import json
import pytest
import requests
import flask
# from flask_testing import TestCase
from src.app import app, render_homepage, format_money


class TestGeneric:
    @pytest.mark.parametrize('function_name', [render_homepage, render_homepage])
    def test_function_is_callable(self, function_name):
        assert callable(function_name)

    def test_all_valid_routes(self):
        # Get a new MapAdapter instance
        adapter = app.url_map.bind('')
        assert adapter.match('/', method='GET') == ('render_homepage', {})
        assert adapter.match('/format_money', method='GET') == ('format_money', {})

    def test_valid_routes_with_invalid_method(self):
        #Raising exception is the criteria to pass this test.
        adapter = app.url_map.bind('')
        with pytest.raises(Exception):
            adapter.match('/', method='POST')
            adapter.match('/format_money', method='POST')

    def test_invalid_routes(self):
        adapter = app.url_map.bind('')
        with pytest.raises(Exception):
            adapter.match('/abc', method='GET')


class TestRenderHomePage:
    def test_home_page_route(self):
        with app.test_request_context('/'):
            assert flask.request.path == '/'


class TestFormatMoney:
    def test_format_money_route(self):
        with app.test_request_context('/format_money?number=10'):
            assert flask.request.path == '/format_money'
            assert flask.request.args['number'] == '10'
