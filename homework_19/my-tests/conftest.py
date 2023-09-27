from selenium.webdriver import Chrome
import pytest
from homework_17.pages.dashboard import Dashboard


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://kachorovska.com/')
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture()
def dashboard(driver):
    yield Dashboard(driver)