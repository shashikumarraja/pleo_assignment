import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from utils import clean_string, format_num


class TestGeneric:
    @pytest.mark.parametrize('function_name', [clean_string, format_num])
    def test_function_is_callable(self, function_name):
        assert callable(function_name)


class TestCleanString:
    pass


class TestFormatNum:
    pass
