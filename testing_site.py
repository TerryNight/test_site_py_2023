from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,800")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

from selenium.webdriver.common.by import By

# Переменные
URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


def openURL (driver, URL):
    driver.get(URL)

def get_el (driver, locator):
    return driver.find_element(By.ID, locator)    

def el_click (driver, locator):
   el = get_el (driver, locator)
   el.click()

def el_send_keys (driver, locator, text):
    el_field = get_el (driver, locator)
    el_field.send_keys(text)

def authorisation (driver, login, password):
    el_send_keys (driver, 'user-name', LOGIN)
    el_send_keys (driver, 'password', PASSWORD)
    el_click (driver, 'login-button')


# 1. Запуск страницы
openURL (driver, URL)

# 2. Авторизация
authorisation (driver, login = LOGIN, password = PASSWORD)

driver.quit()