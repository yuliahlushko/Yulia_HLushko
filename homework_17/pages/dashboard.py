from homework_17.pages.homepage import Homepage


class Dashboard(Homepage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_shoes(self):
        locator = ('xpath', "//li[@data-category-id='71']")
        self.click_on_element(locator)

    def open_good(self):
        locator = ('xpath','//img[@alt="Лофери Cameron темно-коричневі шкіряні"][1]')
        self.click_on_element(locator)

    def open_sign_in_form(self):
        locator = ('xpath', '//a[contains(text(),"Увійти")]')
        self.click_on_element(locator)

    def open_search(self):
        locator=('xpath', "//li[@class='d-flex header-main_search_li']")
        self.click_on_element(locator)

    def search_good(self, message):
        locator = ('xpath', "//input[@type='text'][@placeholder='Пошук']")
        self.click_on_element(locator)
        self.send_keys_into_field(locator, message)
        self.press_enter(locator)

    def ask_about_good (self):
        locator = ('xpath', '//img[@alt="Лофери Cameron темно-коричневі шкіряні"][1]')
        self.click_on_element(locator)
        locator2 = ('xpath', "//a[contains(text(),'Запитати про товар')]")
        self.click_on_element(locator2)