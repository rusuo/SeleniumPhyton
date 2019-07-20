from pages.BasePage import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Utils(BasePage):

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(element))