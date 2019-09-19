"""
Contains functional test for api in app.py
"""
import json
from jsonschema import validate
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as st
from requests.utils import quote


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
    @settings(verbosity=Verbosity.verbose)
    @given(st.one_of(st.integers(), st.floats(allow_nan=False)))
    def test_format_money_valid_num(self, test_client, load_json_schema, number):
        """
        GIVEN a Flask application
        WHEN the '/format_money' page is requested (GET)
        THEN check the response is valid
        """
        data = {'number': quote(str(
            number), safe=b'+')}  # safe prevents urlencoding of + in case of long ints like 3e+16
        response = test_client.get('/format_money', query_string=data)
        body = json.loads(response.data)
        response_status_code = response.status_code
        assert response_status_code == 200, 'Expected response 200 but got %s' % response_status_code
        schema = load_json_schema('format_money_success.json')
        validate(body, schema)

    @settings(verbosity=Verbosity.verbose)
    @given(st.one_of(st.none(), st.text(u'abcdefghijklmnopqrstuvwxyz0123456789',
                                        min_size=1, max_size=25).filter(lambda s: not any([s.isdigit()]))))
    def test_format_money_invalid_num(self, test_client, load_json_schema, number):
        """
        GIVEN a Flask application
        WHEN the '/format_money' page is requested (GET) with invalid number
        THEN check the response is 400
        """
        data = {'number': quote(str(number), safe=b'+')}
        response = test_client.get('/format_money', query_string=data)
        body = json.loads(response.data)
        response_status_code = response.status_code
        assert response_status_code == 400, 'Expected response code 400 but got %s' % response_status_code
        schema = load_json_schema('format_money_fail.json')
        validate(body, schema)
