import allure
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pytest
import time




class BasePage(metaclass=MetaLocator):

    _LOGO = "//a[contains(@class, 'navbar-brand')]"


    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self._PAGE_URL)

    def select_dropdown_option(self, locator, option_text=None, option_value=None, option_index=None):
        """
        Универсальный метод для работы с выпадающими списками
        """
        element = self.driver.find_element(*locator)

        select = Select(element)
        if option_text:
            print(f"Попытка выбрать по тексту: '{option_text}'")
            select.select_by_visible_text(option_text)
        elif option_value:
            select.select_by_value(option_value)
        elif option_index is not None:
            select.select_by_index(option_index)
        else:
            raise ValueError("Не указан параметр для выбора")

        selected = select.first_selected_option.text
        return selected
@pytest.mark.usefixtures("driver")
@allure.epic("Accounts")
@allure.feature("login")
@allure.story("Pages")
class LoginPage:

    _USER_NAME_FILED = "//input[@id='user-name']"
    _USER_PASSWORD = "//input[@id='password']"
    _BUTTON_LOGIN ="//input[@id='login-button']"
    def login(self):
        """Вспомогательный метод для авторизации"""
        self.driver.get("https://www.saucedemo.com")
        self.driver.find_element(*self._USER_NAME_FILED ).send_keys("standard_user")
        self.driver.find_element(*self._USER_PASSWORD).send_keys("secret_sauce")
        self.driver.find_element(*self._BUTTON_LOGIN).click()
        time.sleep(2)

