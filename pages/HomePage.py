from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    AVATAR = (By.CLASS_NAME, 'uni-avatar__content-container')

    def is_avatar_displayed(self):
        avatar = self.driver.find_element(*HomePage.AVATAR)
        return avatar.is_displayed()
