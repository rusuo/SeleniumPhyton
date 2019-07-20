from time import sleep
import unittest
from selenium import webdriver
import json

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utils.Utils import Utils


class LoginTests(unittest.TestCase):
    """Selenium tests for Hudl login functionality"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.hudl.com/login")

    def get_users(self):
        with open('../testData/users.json') as f:
            return json.load(f)

    def test_successful_login(self):
        users = self.get_users()
        login_page = LoginPage(self.driver)
        login_page.login(users[0]["validEmail"], users[0]["validPassword"])

        home_page = HomePage(self.driver)
        assert home_page.is_avatar_displayed()

    def test_no_details_login(self):
        login_page = LoginPage(self.driver)
        login_page.login('', '')

        utils = Utils(self.driver)
        utils.wait_for_element(login_page.errorMessage)
        # animation still not finished, tried to solve it but couldn't, so added a small extra sleep even if not ideal
        sleep(1)
        assert 'We didn\'t recognize that email and/or password.' in login_page.get_error_message_text()

    def test_no_password_login(self):
        users = self.get_users()
        login_page = LoginPage(self.driver)
        login_page.login(users[0]["validEmail"], '')

        utils = Utils(self.driver)
        utils.wait_for_element(login_page.errorMessage)
        # animation still not finished, tried to solve it but couldn't, so added a small extra sleep even if not ideal
        sleep(1)
        assert 'We didn\'t recognize that email and/or password.' in login_page.get_error_message_text()

    def test_no_email_login(self):
        users = self.get_users()
        login_page = LoginPage(self.driver)
        login_page.login('', users[0]["validPassword"])

        utils = Utils(self.driver)
        utils.wait_for_element(login_page.errorMessage)
        # animation still not finished, tried to solve it but couldn't, so added a small extra sleep even if not ideal
        sleep(1)
        assert 'We didn\'t recognize that email and/or password.' in login_page.get_error_message_text()

    def test_wrong_details_login(self):
        users = self.get_users()
        login_page = LoginPage(self.driver)
        login_page.login(users[1]["invalidEmail"], users[1]["invalidPassword"])

        utils = Utils(self.driver)
        utils.wait_for_element(login_page.errorMessage)
        # animation still not finished, tried to solve it but couldn't, so added a small extra sleep even if not ideal
        sleep(1)
        assert 'We didn\'t recognize that email and/or password.' in login_page.get_error_message_text()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()