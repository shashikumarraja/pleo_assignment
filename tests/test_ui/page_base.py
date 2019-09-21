"""
Base Page to initialize page that will be called from all pages
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    This class is the parent class for all the pages in our application.
    It contains all common elements and functionalities available to all pages.
    """

    def click(self, by_locator):
        """
        this function performs click on web element whose locator is passed to it.
        """
        WebDriverWait(self.driver, self.explicit_wait_time).until(
            EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """
        this function performs text entry of the passed in text, in a web element whose locator is passed to it.
        """
        return WebDriverWait(self.driver, self.explicit_wait_time).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        """
        this function checks if the web element whose locator has been passed to it, is enabled or not and returns
        web element if it is enabled.
        """
        return WebDriverWait(self.driver, self.explicit_wait_time).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator):
        """
        this function checks if the web element whose locator has been passed to it, is visible or not and returns
        true or false depending upon its visibility.
        """
        element = WebDriverWait(self.driver, self.explicit_wait_time).until(
            EC.visibility_of_element_located(by_locator))
        return bool(element)
