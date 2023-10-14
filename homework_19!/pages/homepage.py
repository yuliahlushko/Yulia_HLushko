from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class Homepage:
    def __init__(self, driver):
        self._driver = driver
        self.__webdriver_wait = WebDriverWait(self._driver,10)

    def wait_until_element_appears(self, locator):
        return self.__webdriver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator):
        self.wait_until_element_appears(locator).click()

    def send_keys_into_field(self, locator, message):
        self.wait_until_element_appears(locator).send_keys(message)

    def press_enter(self, locator):
        self.wait_until_element_appears(locator).send_keys(Keys.ENTER)


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def add_cookie(self, name, value):
        cookie = {
            'name': name,
            'value': value,
        }
        self.driver.add_cookie(cookie)

    def get_all_cookies(self):
        return self.driver.get_cookies()


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set_item(self, key, value):
        self.driver.execute_script(f"localStorage.setItem('{key}', '{value}')")

    def get_item(self, key):
        return self.driver.execute_script(f"return localStorage.getItem('{key}')")