import pytest
from time import sleep
from page_home import BasePage
from page_home import HomePage
import allure
from allure_commons.types import AttachmentType

# @pytest.mark.usefixtures('driver_init')
# class BaseTest:
#     pass

@pytest.mark.usefixtures('driver_init')
class TestHomePage:
    def test_open_url(self):
        url = "http://flask-app:5000/"
        self.driver.get(url)
        assert HomePage.is_url_matches(self, url)

    def test_page_title(self):
        assert HomePage.is_title_matches(self)

    def test_elements_visible(self):
        assert HomePage.submit_button_visible(self)
        assert HomePage.number_text_box_visible(self)

    def test_error_message(self):
        HomePage.click_submit_button(self)
        assert HomePage.error_message_displayed(self)
        text = HomePage.get_error_message(self)
        assert text == 'Error Message: Please enter a valid number'

    def test_success_message(self):
        HomePage.enter_number_in_text_box(self, 10)
        HomePage.click_submit_button(self)
        assert HomePage.success_message_displayed(self)
        text = HomePage.get_success_message(self)
        assert text == 'Formatted Number: 10.00'
