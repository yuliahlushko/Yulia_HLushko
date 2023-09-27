from homework_19.pages.homepage import Homepage
from homework_19.locators.base_page_locators import Base_page_Locators


class Base_page(Homepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Base_page_Locators()

    def open_hero_category(self):
        self.click_on_element(self.locators.hero)


    def open_sign_in_form(self):
        self.click_on_element(self.locators.sign_in)

    def search(self, message):
        self.click_on_element(self.locators.search)
        self.send_keys_into_field(self.locators.search, message)
        self.press_enter(self.locators.search)


    def open_toy(self):
        self.click_on_element(self.locators.toy)


    def buy_toy(self):
        self.click_on_element(self.locators.toy)
        self.click_on_element(self.locators.buy)





'''    driver.add_cookie({'name':'car', 'value':'red'})
    print(f'cookie:{driver.get_cookie("car")}')'''