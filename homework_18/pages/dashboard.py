from homework_18.pages.homepage import Homepage
from homework_18.locators.dashboard_locators import Dashboard_Locators

class Dashboard(Homepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Dashboard_Locators()

    def open_shoes(self):
        self.click_on_element(self.locators.shoes)

    def open_sign_in_form(self):
        self.click_on_element(self.locators.sign_in)

    def open_search(self):
        self.click_on_element(self.locators.search_button)

    def search_good(self, message):
        locator = ('xpath', "//input[@type='text'][@placeholder='Пошук']")
        self.click_on_element(self.locators.search_field)
        self.send_keys_into_field(self.locators.search_field, message)
        self.press_enter(self.locators.search_field)
