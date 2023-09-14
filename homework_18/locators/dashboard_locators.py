class Dashboard_Locators:
    def __init__(self):
        self.shoes = ('xpath', "//li[@data-category-id='71']")
        self.sign_in = ('xpath', '//a[contains(text(),"Увійти")]')
        self.search_button = ('xpath', "//input[@type='text'][@placeholder='Пошук']")
        self.search_field = ('xpath', "//input[@type='text'][@placeholder='Пошук']")


