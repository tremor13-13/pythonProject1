import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    """Регистрируем кастомные маркеры чтобы избежать warnings"""
    config.addinivalue_line(
        "markers", "checkout: маркер для тестов checkout процесса"
    )
    config.addinivalue_line(
        "markers", "complete: маркер для завершенных тестов"
    )


@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver

    yield driver
    driver.quit()







# from selenium.webdriver.support import expected_conditions as EC
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # import allure
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# @pytest.fixture(scope="session")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.maximize_window()  # ✅ Добавляем максимизацию окна
#
#     # Логинимся
#     driver.get("https://www.saucedemo.com")
#     driver.find_element("id", "user-name").send_keys("standard_user")  # ✅ Лучше использовать id
#     driver.find_element("id", "password").send_keys("secret_sauce")
#     driver.find_element("id", "login-button").click()
#
#     # Ждем и проверяем успешность логина
#     WebDriverWait(driver, 10).until(
#         EC.url_contains("inventory.html")
#     )
#
#     yield driver
#     driver.quit()


#
# @pytest.fixture(scope="session")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#
#     # ✅ Один раз логинимся в начале сессии
#     driver.get("https://www.saucedemo.com")
#     driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
#     driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
#     driver.find_element("xpath", "//input[@id='login-button']").click()
#
#     # ✅ Проверяем что залогинились
#     assert "inventory.html" in driver.current_url, "Ошибка авторизации"
#
#     yield driver
#
#     #  Закрываем драйвер только в конце всех тестов
#     driver.quit()
#
#
# # ✅ Функция для скриншотов
# def pytest_runtest_makereport(item, call):
#     if call.when == "call":
#         try:
#             # Получаем драйвер из фикстур
#             if hasattr(item, 'funcargs') and 'driver' in item.funcargs:
#                 driver = item.funcargs['driver']
#                 screenshot = driver.get_screenshot_as_png()
#                 status = "passed" if call.excinfo is None else "failed"
#                 allure.attach(
#                     screenshot,
#                     name=f"screenshot_{item.name}_{status}",
#                     attachment_type=allure.attachment_type.PNG
#                 )
#         except Exception as e:
#             print(f"❌ Ошибка создания скриншота: {e}")







# import os
# import shutil
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(autouse=True)
# def driver(request):
#     chrome_options = Options()
#     chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
#     driver = webdriver.Chrome(options=chrome_options)
#     request.cls.driver = driver
#     yield
#     driver.quit()



