"""
Contains functional test for api in app.py
"""
import json
from jsonschema import validate
from hypothesis import given, settings, Verbosity, example
import hypothesis.strategies as st

class TestHomePage:
    def test_home_page(self, test_client):
        """
        GIVEN a Flask application
        WHEN the '/' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Number' in response.data


class TestFormatMoney:
    def test_format_money_valid_num(self, test_client, load_json_schema):
        """
        GIVEN a Flask application
        WHEN the '/format_money' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get('/format_money?number=10')
        body = json.loads(response.data)
        original_number = body.get('original_number')
        formatted_number = body.get('formatted_number')
        response_status_code = response.status_code
        assert response_status_code == 200, 'Expected response 200 but got %s' % response_status_code
        schema = load_json_schema('format_money_success.json')
        validate(body, schema)
        assert original_number == 10
        assert formatted_number == "10.00"

    @settings(verbosity=Verbosity.verbose)
    @given(st.one_of(st.none(), st.text(min_size=1)))
    def test_format_money_invalid_num(self, test_client, load_json_schema, number):
        """
        GIVEN a Flask application
        WHEN the '/format_money' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get('/format_money?number=%s' % number)
        body = json.loads(response.data)
        response_status_code = response.status_code
        assert response_status_code == 400, 'Expected response code 400 but got %s' % response_status_code
        schema = load_json_schema('format_money_fail.json')
        validate(body, schema)
