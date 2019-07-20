from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    email = (By.ID, 'email')
    password = (By.ID, 'password')
    loginButton = (By.ID, 'logIn')
    errorMessage = (By.CLASS_NAME, 'login-error-container')

    def set_email(self, email):
        email_textfield = self.driver.find_element(*LoginPage.email)
        email_textfield.send_keys(email)

    def set_password(self, password):
        password_textfield = self.driver.find_element(*LoginPage.password)
        password_textfield.send_keys(password)

    def click_submit(self):
        submit_button = self.driver.find_element(*LoginPage.loginButton)
        submit_button.click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_submit()

    def get_error_message_text(self):
        message = self.driver.find_element(*LoginPage.errorMessage)
        return message.text
