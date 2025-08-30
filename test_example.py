import time
import pytest
import allure
from allure_commons.types import Severity


@pytest.mark.usefixtures("driver")
@allure.epic("Accounts")
@allure.feature("login")
@allure.story("Pages")
class TestPages:

    def login(self):
        """Вспомогательный метод для авторизации"""
        self.driver.get("https://www.saucedemo.com")
        self.driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element("xpath", "//input[@id='login-button']").click()
        time.sleep(2)

    @pytest.mark.smoke
    @allure.title("login page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com/login", name="documentation")
    def test_open_login_page(self):
        self.login()
        print("ТЕСТ1 ПРОШЕЛ УДАЧНО")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Ошибка входа"

    @pytest.mark.regression
    @allure.title("Add inventory")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://confluence.com/books", name="documentation")
    def test_add_to_cart(self):
        self.login()
        self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(3)
        print("ТЕСТ2 ПРОШЕЛ УДАЧНО")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "ошибка входа"

    @pytest.mark.profile
    @allure.title("Open cart page")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://confluence.com/profile", name="documentation")
    def test_open_cart_page(self):
        self.login()
        # self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        # self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        print("ТЕСТ3 ПРОШЕЛ УДАЧНО")
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "ошибка входа"

    @pytest.mark.checkout
    @allure.title("Open checkout page")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://confluence.com/profile", name="documentation")
    def test_open_checkout_page(self):
        self.login()
        # self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        # self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
        self.driver.find_element("xpath", "//button[@id='checkout']").click()
        time.sleep(2)
        print("ТЕСТ4 ПРОШЕЛ УДАЧНО")
        expected_checkout_url = "https://www.saucedemo.com/checkout-step-one.html"
        assert self.driver.current_url == expected_checkout_url, \
            f"Ожидалась страница checkout ({expected_checkout_url}), но открыт {self.driver.current_url}"

    @pytest.mark.complete
    @allure.title("Complete checkout process")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com/profile", name="documentation")
    def test_complete_checkout(self):
        self.login()

        # Добавляем товары
        # self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        # self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)

        # Переходим в корзину
        self.driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
        time.sleep(1)

        # Начинаем checkout
        self.driver.find_element("xpath", "//button[@id='checkout']").click()
        time.sleep(1)

        # Заполняем информацию
        self.driver.find_element("xpath", "//input[@id='first-name']").send_keys("Alex")
        self.driver.find_element("xpath", "//input[@id='last-name']").send_keys("Frunzik")
        self.driver.find_element("xpath", "//input[@id='postal-code']").send_keys("234234")
        self.driver.find_element("xpath", "//input[@id='continue']").click()
        time.sleep(2)

        # Завершаем заказ
        self.driver.find_element("xpath", "//button[@id='finish']").click()
        time.sleep(2)

        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "ошибка завершения заказа"



# import time
# import pytest
# import allure
# from allure_commons.types import Severity
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @allure.epic("Accounts")
# @allure.feature("login")
# @allure.story("Pages")
# class TestPages:
#
#     def login(self, driver):
#         """Вспомогательный метод для авторизации"""
#         # Проверяем, не авторизованы ли мы уже
#         driver.get("https://www.saucedemo.com/inventory.html")
#         if "inventory.html" in driver.current_url:
#             print("авторизован")
#             return True
#
#         # Если не авторизованы - логинимся
#         driver.get("https://www.saucedemo.com")
#         driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
#         driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
#         driver.find_element("xpath", "//input[@id='login-button']").click()
#         time.sleep(2)
#         return "inventory.html" in driver.current_url
#
#     @pytest.mark.smoke
#     @allure.title("login page")
#     @allure.severity(Severity.NORMAL)
#     @allure.link(url="https://confluence.com/login", name="documentation")
#     def test_open_login_page(self, driver):  #  Добавляем driver как аргумент
#         # Просто проверяем что мы на странице инвентаря
#         # driver.get("https://www.saucedemo.com/inventory.html")
#
#         # ✅ Скриншот
#         allure.attach(
#             driver.get_screenshot_as_png(),
#             name="inventory_page",
#             attachment_type=allure.attachment_type.PNG
#         )
#
#         assert "inventory.html" in driver.current_url, "Ошибка входа"
#
#     @pytest.mark.regression
#     @allure.title("Add inventory")
#     @allure.severity(Severity.BLOCKER)
#     @allure.link(url="https://confluence.com/books", name="documentation")
#     def test_add_to_cart(self, driver):
#         # ✅ Проверяем что мы на нужной странице
#         if "inventory.html" not in driver.current_url:
#             driver.get("https://www.saucedemo.com/inventory.html")
#
#         # ✅ Явные ожидания вместо time.sleep()
#         add_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(("id", "add-to-cart-sauce-labs-bike-light"))
#         )
#         add_button.click()
#
#         # ✅ Проверяем что появился бейдж корзины
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(("class_name", "shopping_cart_badge"))
#         )
#
#     @pytest.mark.profile
#     @allure.title("Open cart page")
#     @allure.severity(Severity.BLOCKER)
#     @allure.link(url="https://confluence.com/profile", name="documentation")
#     def test_open_cart_page(self, driver):  # ✅ Добавляем driver как аргумент
#         driver.get("https://www.saucedemo.com/inventory.html")
#
#         # ✅ Добавляем товары если их еще нет
#         try:
#             driver.find_element("xpath", "//span[@class='shopping_cart_badge']")
#         except:
#             driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
#             driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
#             time.sleep(1)
#
#         # ✅ Переходим в корзину
#         driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
#         time.sleep(2)
#
#         # ✅ Скриншот корзины
#         allure.attach(
#             driver.get_screenshot_as_png(),
#             name="cart_page",
#             attachment_type=allure.attachment_type.PNG
#         )
#
#         assert driver.current_url == "https://www.saucedemo.com/cart.html", "Ошибка перехода в корзину"
#
#     @pytest.mark.checkout
#     @allure.title("Checkout process")
#     @allure.severity(Severity.BLOCKER)
#     @allure.link(url="https://confluence.com/profile", name="documentation")
#     def test_checkout_process(self, driver):  # ✅ Добавляем driver как аргумент
#         driver.get("https://www.saucedemo.com/cart.html")
#
#         # ✅ Начинаем checkout
#         driver.find_element("xpath", "//button[@id='checkout']").click()
#         time.sleep(1)
#
#         # ✅ Заполняем информацию
#         driver.find_element("xpath", "//input[@id='first-name']").send_keys("Alex")
#         driver.find_element("xpath", "//input[@id='last-name']").send_keys("Frunzik")
#         driver.find_element("xpath", "//input[@id='postal-code']").send_keys("234234")
#         driver.find_element("xpath", "//input[@id='continue']").click()
#         time.sleep(1)
#
#         # ✅ Завершаем заказ
#         driver.find_element("xpath", "//button[@id='finish']").click()
#         time.sleep(2)
#
#         # ✅ Скриншот завершения
#         allure.attach(
#             driver.get_screenshot_as_png(),
#             name="checkout_complete",
#             attachment_type=allure.attachment_type.PNG
#         )
#
#         assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Ошибка завершения заказа"


#
#
#
#
# import time
#
# import pytest
# import allure
# from allure_commons.types import Severity
#
# @pytest.mark.usefixtures("driver")
# @allure.epic("Accounts")
# @allure.feature("login")
# @allure.story("Pages")
# class TestPages:
#
#     def login(self):
#         """Вспомогательный метод для авторизации"""
#         self.driver.get("https://www.saucedemo.com")
#         self.driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
#         self.driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
#         self.driver.find_element("xpath", "//input[@id='login-button']").click()
#         time.sleep(2)
#
#     @pytest.mark.smoke
#     @allure.title("login page")
#     @allure.severity(Severity.NORMAL)
#     @allure.link(url="https://confluence.com/login", name="documetation")
#     def test_open_login_page(self):
#         self.login()
#         assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Ошибка входа"
#
#
#     @pytest.mark.regression
#     @allure.title("Add imventory")
#     @allure.severity(Severity.BLOCKER)
#     @allure.link(url="https://confluence.com/books", name="documetation")
#     def test_open_books_page(self):
#         self.login()
#         self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
#         self.driver.find_element("xpath","//button[@id='add-to-cart-sauce-labs-backpack']").click()
#         time.sleep(3)
#         assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "ошибка входа"
#
#     @pytest.mark.profile
#     @allure.title("Open cart page")
#     @allure.severity(Severity.BLOCKER)
#     @allure.link(url="https://confluence.com/profile", name="documetation")
#     def test_open_profile_page(self):
#         self.login()
#         self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
#         self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
#         self.driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
#         time.sleep(3)
#         assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "ошибка входа"
#
#     @pytest.mark.profile
#     @allure.title("Open checkout page")
#     @allure.severity(Severity.BLOCKER)
#     @allure.link(url="https://confluence.com/profile", name="documetation")
#     def test_open_profile_page(self):
#         self.login()
#         self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
#         self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']").click()
#         self.driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
#         self.driver.find_element("xpath", "//button[@id='checkout']").click()
#         expected_checkout_url = "https://www.saucedemo.com/checkout-step-one.html"
#         assert self.driver.current_url == expected_checkout_url, \
#             f"Ожидалась страница checkout ({expected_checkout_url}), но открыт {self.driver.current_url}"
#
#     @pytest.mark.profile
#     @allure.title("Open checkout page")
#     @allure.severity(Severity.NORMAL)
#     @allure.link(url="https://confluence.com/profile", name="documetation")
#     def test_open_profile_page(self):
#         self.login()
#         self.driver.find_element("xpath", "//input[@id='first-name']").send_keys("Alex")
#         self.driver.find_element("xpath", "//input[@id='last-name']").send_keys("Frunzik")
#         self.driver.find_element("xpath", "//input[@id='postal-code']").send_keys("234234")
#         self.driver.find_element("xpath", "//input[@id='continue']").click()
#         time.sleep(3)
#         self.driver.find_element("xpath", "//button[@id='finish']").click()
#         time.sleep(3)
#         assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "ошибка входа"