from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def test_check_search_field_is_empty():
    driver=Chrome()
    driver.get("https://context.reverso.net/")
    time.sleep(5)
    input_filed_locator = '//*[@id="entry"]'
    input_field = driver.find_element(By.XPATH, input_filed_locator)
    current_value = input_field.get_attribute("value")
    assert current_value is None or current_value.strip() == ""


def test_clear_search_field():
    driver = Chrome()
    driver.get('https://context.reverso.net/')
    time.sleep(5)
    search_field_locator = '//*[@id="entry"]'
    element = driver.find_element(by = 'xpath', value = search_field_locator)
    element.send_keys('dog')
    time.sleep(5)
    clear_button_locator = '//div/button[2]'
    clear_button = driver.find_element(by='xpath', value=clear_button_locator)
    clear_button.click()
    time.sleep(5)
    current_value1 = element.get_attribute("value")
    assert current_value1 is None or current_value1.strip() == ""


def test_choose_language():
    driver = Chrome()
    driver.get('https://context.reverso.net/')
    time.sleep(5)
    language_field_locator = '//*[@id="interface-lang-menu"]'
    language = driver.find_element(by='xpath', value=language_field_locator)
    language.click()
    time.sleep(5)
    select_language_locator = '/html/body/header/div/div[2]/div[2]/div[2]/a[16]'
    select_language = driver.find_element(by='xpath', value=select_language_locator)
    select_language.click()
    time.sleep(5)
    some_text_locator = '//h1[text()="Перекладайте та вивчайте мільйони слів і виразів"]'
    some_text = driver.find_element(by='xpath', value=some_text_locator)
    assert some_text.text == "Перекладайте та вивчайте мільйони слів і виразів"


def test_abble_to_use_visible_keyboard():
    driver = Chrome()
    driver.get('https://context.reverso.net/')
    time.sleep(5)
    keyboard_field_locator = '//div/section[2]/div[1]/div[1]/div/span'
    keyboard = driver.find_element(by='xpath', value=keyboard_field_locator)
    keyboard.click()
    time.sleep(5)
    letter1_locator = '//div/table[2]/tbody/tr/td[9]'
    letter1 = driver.find_element(by='xpath', value=letter1_locator)
    letter1.click()
    time.sleep(2)
    letter2_locator = '//div/table[3]/tbody/tr/td[5]'
    letter2 = driver.find_element(by='xpath', value=letter2_locator)
    letter2.click()
    search_field_locator = '//*[@id="entry"]'
    search_field = driver.find_element(by='xpath', value=search_field_locator)
    time.sleep(5)
    assert search_field.get_attribute("value") == 'if'


def test_user_is_able_to_choose_translate_language():
    driver = Chrome()
    driver.get('https://context.reverso.net/')
    time.sleep(5)
    language_selector_locator = '//*[@id="src-selector"]'
    language_selector=driver.find_element(by='xpath', value=language_selector_locator)
    language_selector.click()
    time.sleep(5)
    translate_from_language_locator = '//div[1]/span[11]'
    translate_from_language = driver.find_element(by='xpath', value = translate_from_language_locator)
    translate_from_language.click()
    time.sleep(5)
    data_value_locator = "//div[@id='src-selector']/span[2]"
    data_value = driver.find_element(by='xpath', value=data_value_locator)
    time.sleep(5)
    assert data_value.text == 'Polish'

