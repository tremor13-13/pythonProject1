import time

import allure
import pytest

from pages.base_page import BasePage


@pytest.mark.usefixtures("driver")
@allure.epic("Accounts")
@allure.feature("login")
@allure.story("Pages")
class LoginPage(BasePage):
    _USER_NAME_FILED = "//input[@id='user-name']"
    _USER_PASSWORD = "//input[@id='password']"
    _BUTTON_LOGIN = "//input[@id='login-button']"

    def login(self):
        """Вспомогательный метод для авторизации"""
        self.driver.get("https://www.saucedemo.com")
        self.driver.find_element(*self._USER_NAME_FILED).send_keys("standard_user")
        self.driver.find_element(*self._USER_PASSWORD).send_keys("secret_sauce")
        self.driver.find_element(*self._BUTTON_LOGIN).click()
        time.sleep(2)
