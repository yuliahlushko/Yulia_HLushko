from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Homepage:
    def __init__(self,driver):
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