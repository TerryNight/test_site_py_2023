from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Переменные
URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver ():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return driver

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

# 0. Получение драйвера
driver = get_driver()

# 1. Запуск страницы
openURL (driver, URL)

# 2. Авторизация
authorisation (driver, login = LOGIN, password = PASSWORD)

driver.quit()