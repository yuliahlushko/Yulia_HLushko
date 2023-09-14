from homework_18.pages.dashboard import Dashboard
from homework_18.locators.shoes_locators import Shoes_locators


class Shoes(Dashboard):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Shoes_locators()

    def open_good(self):
        self.click_on_element(self.locator.good)

    def ask_about_good(self):
        self.click_on_element(self.locator.good)
        self.click_on_element(self.locator.ask_about_good)
