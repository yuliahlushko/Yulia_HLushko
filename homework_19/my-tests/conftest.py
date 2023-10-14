from selenium.webdriver import Chrome
import pytest
from homework_19.pages.start_page import Start_page


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    driver.get('https://bi.ua/')

    yield Start_page(driver)


