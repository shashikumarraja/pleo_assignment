"""
Contains page locators of all the pages in their speicifc class
"""
from selenium.webdriver.common.by import By

class HomePageLocators:
    """A class for home page locators. All home page locators should come here"""
    NUMBER_INPUT_BOX = (By.ID, 'input_num')
    SUBMIT_BUTTON = (By.ID, 'submit')
    SUCCESS_MESSAGE = (By.ID, 'success_message')
    ERROR_MESSAGE = (By.ID, 'error_message')
    