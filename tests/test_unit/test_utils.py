"""
Unit tests for utils module
"""
import inspect
import pytest
from hypothesis import given, settings, Verbosity, example
import hypothesis.strategies as st
from src.utils import clean_string, format_num
from naughty_string_validator import get_naughty_string_list


class TestGeneric:
    @pytest.mark.parametrize('function_name', [clean_string, format_num])
    def test_function_is_callable(self, function_name):
        assert callable(function_name)


class TestCleanString:
    def test_number_of_args(self):
        arg_count = len(inspect.getfullargspec(clean_string)[0])
        assert arg_count == 1


class TestFormatNum:
    def test_number_of_args(self):
        arg_count = len(inspect.getfullargspec(format_num)[0])
        assert arg_count == 2

    @settings(verbosity=Verbosity.verbose)
    @given(st.integers())
    def test_output_type_with_int_input(self, number):
        assert isinstance(format_num(number, [(',', ' ')]), str)

    @settings(verbosity=Verbosity.verbose)
    @given(st.floats())
    def test_output_type_with_float_input(self, number):
        assert isinstance(format_num(number, [(',', ' ')]), str)

    def test_no_rule_corner_case(self):
        assert format_num(123.45, [])  is None

    def test_no_number_no_rule_corner_case_1(self):
        assert format_num('', [])  is None

    def test_no_number_no_rule_corner_case_2(self):
        assert format_num('', [()])  is None

    def test_no_number_corner_case(self):
        assert format_num('', [(',', ' ')])  is None

    @pytest.mark.parametrize('number', list(filter(lambda x: not (isinstance(x, float) and  isinstance(x, int) and x.isdigit()), get_naughty_string_list())))
    def test_all_naughty_string_case(self, number):
        assert format_num(number, [(',', ' ')])  is None

    @pytest.mark.parametrize('input_num, formatted_num', [(123.456, '123.46'), (1234.56, '1 234.56'), (1, '1.00'), (0.56789, '0.57'), (-50004, '-50 004.00'), (0, '0.00')])
    def test_positive_cases(self, input_num, formatted_num):
        assert format_num(input_num, [(',', ' ')]) == formatted_num
