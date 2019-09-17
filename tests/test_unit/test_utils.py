"""
Unit tests for utils module
"""
import inspect
import pytest
from hypothesis import given, settings, Verbosity, example
import hypothesis.strategies as st
from src.utils import clean_string, format_num


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
        if number:
            #only non-zero cases go inside
            assert isinstance(format_num(number, [(',', ' ')]), str)
        else:
            assert format_num(number, [(',', ' ')]) is None

    @settings(verbosity=Verbosity.verbose)
    @given(st.floats())
    def test_output_type_with_float_input(self, number):
        if number:
            assert isinstance(format_num(number, [(',', ' ')]), str)
        else:
            assert format_num(number, [(',', ' ')]) is None

    def test_no_rule_corner_case(self):
        assert format_num(123.45, [])  is None

    def test_no_number_no_rule_corner_case_1(self):
        assert format_num('', [])  is None

    def test_no_number_no_rule_corner_case_2(self):
        assert format_num('', [()])  is None

    def test_no_number_corner_case(self):
        assert format_num('', [(',', ' ')])  is None

