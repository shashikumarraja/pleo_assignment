from locators import HomePageLocators
from page_base import BasePage


class HomePage(BasePage):
    """Home page action methods come here """

    def is_title_matches(self):
        """Verifies that the title appears in page title"""
        return "Format Number" in self.driver.title

    def is_url_matches(self, url):
        return url in self.driver.current_url

    def number_text_box_visible(self):
        return BasePage.is_visible(self, HomePageLocators.NUMBER_INPUT_BOX)

    def submit_button_visible(self):
        return BasePage.is_visible(self, HomePageLocators.SUBMIT_BUTTON)

    def enter_number_in_text_box(self, number):
        element = self.driver.find_element(*HomePageLocators.NUMBER_INPUT_BOX)
        element.clear()
        return BasePage.enter_text(self, HomePageLocators.NUMBER_INPUT_BOX, number)

    def clear_text_box(self):
        element = self.driver.find_element(*HomePageLocators.NUMBER_INPUT_BOX)
        element.clear()
        
    def click_submit_button(self):
        element = self.driver.find_element(*HomePageLocators.SUBMIT_BUTTON)
        return element.click()

    def success_message_displayed(self):
        return BasePage.is_visible(self, HomePageLocators.SUCCESS_MESSAGE)

    def get_success_message(self):
        element = self.driver.find_element(*HomePageLocators.SUCCESS_MESSAGE)
        return element.text

    def get_error_message(self):
        element = self.driver.find_element(*HomePageLocators.ERROR_MESSAGE)
        return element.text

    def error_message_displayed(self):
        return BasePage.is_visible(self, HomePageLocators.ERROR_MESSAGE)
