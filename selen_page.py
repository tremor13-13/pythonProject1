import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

#  костыль от Махортова для обхода АЛЕРТа
from selenium.webdriver.chrome.options import Options
# ну и сами настройки костыля, что бы убрать уведомления
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=3)
driver.get("https://www.saucedemo.com")

#  проверка что мы на том сайте на котором нужно быть
assert driver.title == "Swag Labs", f"было заточено что заголовок будет 'Swag Labs', но выдало {driver.title}"

#  ПРЯМОЙ ВВОД
#  обнаруживаем элемент для взаимодействия и сразу отправляем текст или команду
#  driver.find_element("xpath", "").send_keys()

#    ВВОД ЧЕРЕЗ ПЕРЕМЕННУЮ
#    сохраняем в переменную и потом через переменную
#    взаимодействуем с объектом(кнопка, поле ввода чекбокс и т.д.)

#   делаем поиск элементов с ОЖИДАНИЕМ ЗАГРУЗКИ
time.sleep(2)
#   находим элемент
login_user = driver.find_element("xpath", "//input[@id='user-name']")
#   ждем что бы он загрузился или появился
wait.until(EC.element_to_be_clickable(login_user))
#   очищаем поле для ввода имени юзера пустое
login_user.clear()
#  отправляем необходимую информацию в найденный локатор
login_user.send_keys("standard_user")

time.sleep(2)

# повторяем тоже самое для ввода пароля
password_user = driver.find_element("xpath", "//input[@id='password']")
wait.until(EC.element_to_be_clickable(password_user))
password_user.clear()
password_user.send_keys("secret_sauce")
time.sleep(2)
# находим кнопку Логин
login_button = driver.find_element("xpath", "//input[@id='login-button']")
wait.until(EC.element_to_be_clickable(login_button))
# нажимаем на кнопку Логин
login_button.click()
#  проверка следующей страницы с ПРОДУКТАМИ !!!
#  что открылась именно то что нужно
expected_url = "https://www.saucedemo.com/inventory.html"
assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, но открыт {driver.current_url}"
# добавляем покупки в корзину
time.sleep(2)
# добавляем товары в корзину

add_products1 = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
wait.until(EC.element_to_be_clickable(add_products1))
add_products1.click()

time.sleep(2)

add_products2 = driver.find_element("xpath","//button[@id='add-to-cart-sauce-labs-backpack']")
wait.until(EC.element_to_be_clickable(add_products2))
add_products2.click()

# проваливаемся в корзину и проверяем что мы тама!
time.sleep(2)

basket_button = driver.find_element("xpath", "//a[@class='shopping_cart_link']")
basket_button.click()
expected_cart_url = "https://www.saucedemo.com/cart.html"
assert driver.current_url == expected_cart_url, \
    f"Ожидалась страница корзины ({expected_cart_url}), но открыт {driver.current_url}"
time.sleep(2)
# проваливаемся в checkout т.е. отправляем товар по адресу!


checkout_button = driver.find_element("xpath", "//button[@id='checkout']")
checkout_button.click()
time.sleep(2)
# проверяем что провалились
expected_checkout_url = "https://www.saucedemo.com/checkout-step-one.html"
assert driver.current_url == expected_checkout_url, \
    f"Ожидалась страница checkout ({expected_checkout_url}), но открыт {driver.current_url}"

#  заполнение Checkout: Your Information
chec_fist_name = driver.find_element("xpath", "//input[@id='first-name']")
chec_fist_name.send_keys("Alex")

chec_last_name = driver.find_element("xpath", "//input[@id='last-name']")
chec_last_name.send_keys("Frunzik")

chec_zip_code = driver.find_element("xpath", "//input[@id='postal-code']")
chec_zip_code.send_keys("234234")

chec_continue = driver.find_element("xpath", "//input[@id='continue']")
chec_continue.click()
time.sleep(2)
# finish
finish_button = driver.find_element("xpath", "//button[@id='finish']")
finish_button.click()

time.sleep(2)

back_home_button = driver.find_element("xpath", "//button[@id='back-to-products']")
back_home_button.click()

time.sleep(2)