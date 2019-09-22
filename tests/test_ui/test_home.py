"""
Contains tests for the Home Page
"""
from time import sleep
import pytest
import allure
from allure_commons.types import AttachmentType
from hypothesis import given, settings, Verbosity, example
import hypothesis.strategies as st
from page_home import BasePage
from page_home import HomePage



@pytest.mark.usefixtures('driver_init', 'take_screeshot_on_test_fail')
class TestHomePage:
    def test_open_url(self, app_url):
        self.driver.get(app_url)
        assert HomePage.is_url_matches(self, app_url)

    def test_page_title(self):
        assert HomePage.is_title_matches(self)

    def test_elements_visible(self):
        assert HomePage.submit_button_visible(self)
        assert HomePage.number_text_box_visible(self)

    @settings(verbosity=Verbosity.verbose)
    @given(st.one_of(st.none(), st.text(u'abcdefghijklmnopqrstuvwxyz0123456789',
                                        min_size=1, max_size=25).filter(lambda s: not any([s.isdigit()]))))
    def test_error_message(self, input_num):
        HomePage.enter_number_in_text_box(self, str(input_num))
        HomePage.click_submit_button(self)
        assert HomePage.error_message_displayed(self)
        text = HomePage.get_error_message(self)
        assert text == 'Error Message: Please enter a valid number'

    @settings(verbosity=Verbosity.verbose)
    @given(st.one_of(st.integers(), st.floats(allow_nan=False)))
    def test_success_message_property(self, input_num):
        HomePage.enter_number_in_text_box(self, str(input_num))
        HomePage.click_submit_button(self)
        assert HomePage.success_message_displayed(self)

    @pytest.mark.parametrize('input_num, formatted_num', [(123.456, '123.46'), (1234.56, '1 234.56'), (1, '1.00'), (0.56789, '0.57'), (-50004, '-50 004.00'), (0, '0.00')])
    def test_formatted_number_value(self, input_num, formatted_num):
        HomePage.enter_number_in_text_box(self, str(input_num))
        HomePage.click_submit_button(self)
        assert HomePage.success_message_displayed(self)
        text = HomePage.get_success_message(self)
        assert text == 'Formatted Number: %s' % formatted_num
