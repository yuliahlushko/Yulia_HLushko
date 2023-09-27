class Base_page_Locators:
    def __init__(self):
        self.hero = ('xpath', "//a[@class='hNavA'][1]")
        self.sign_in = ('xpath', "//div[@class='ico i-hu']")
        self.search = ('xpath', "//input[@type='text'][@placeholder='Що ви шукаєте?']")
        self.toy = ('xpath', '//img[@src="/assets/thumbnails/2e/2ef61e40a72a1c5b1f547e41fde0eced.jpg"]')
        self.buy = ('xpath', "//a[@class='btn48 fS20 btnB addPTBj']")


