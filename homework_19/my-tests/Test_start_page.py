import time


def test_open_hero(base_page):
    time.sleep(5)
    base_page.open_hero_category()
    time.sleep(5)


def test_open_sign_in(base_page):
    time.sleep(5)
    base_page.open_sign_in_form()
    time.sleep(5)


def test_search_good(base_page):
    time.sleep(5)
    base_page.search('lego')
    time.sleep(5)


def test_open_toy(base_page):
    time.sleep(15)
    base_page.open_toy()
    time.sleep(5)


def test_buy_toy(base_page):
    time.sleep(15)
    base_page.buy_toy()
    time.sleep(5)


def add_some_cookies(base_page):
    time.sleep(15)
    base_page.a