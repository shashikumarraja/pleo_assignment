"""
Contains functional test for api in app.py
"""
import json
import pytest
import logging
from jsonschema import validate
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as st
from requests.utils import quote

logger = logging.getLogger(__name__)

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

    @pytest.mark.parametrize('input_num, formatted_num', [(123.456, '123.46'), (1234.56, '1 234.56'), (1, '1.00'), (0.56789, '0.57'), (-50004, '-50 004.00'), (0, '0.00')])
    def test_response_value(self, test_client, load_json_schema, input_num, formatted_num):
        """
        GIVEN a Flask application
        WHEN the '/format_money' page is requested (GET)
        THEN check the exact response
        """
        data = {'number': quote(str(
            input_num), safe=b'+')}  # safe prevents urlencoding of + in case of long ints like 3e+16
        response = test_client.get('/format_money', query_string=data)
        body = json.loads(response.data)
        result = body.get('formatted_number')
        response_status_code = response.status_code
        assert response_status_code == 200, 'Expected response 200 but got %s' % response_status_code
        schema = load_json_schema('format_money_success.json')
        validate(body, schema)
        assert formatted_num == result, "Expected %s, got %s" % (formatted_num, result)
