from homework_18.locators.dashboard_locators import Dashboard_Locators


class Shoes_locators(Dashboard_Locators):
    def __init__(self):
        super().__init__()
        self.good = ('xpath','//img[@alt="Лофери Cameron темно-коричневі шкіряні"][1]')
        self.ask_about_good = ('xpath', "//a[contains(text(),'Запитати про товар')]")