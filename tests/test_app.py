import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import render_homepage, format_money


class TestGeneric:
    @pytest.mark.parametrize('function_name', [render_homepage, render_homepage])
    def test_function_is_callable(self, function_name):
        assert callable(function_name)


class TestRenderHomePage:
    pass


class TestFormatMoney:
    pass
