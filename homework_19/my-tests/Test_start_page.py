import time

def test_open_hero(start_page):
    time.sleep(5)
    start_page.open_hero_category()

    time.sleep(5)


def test_open_sign_in(start_page):
    time.sleep(5)
    start_page.open_sign_in_form()
    time.sleep(5)


def test_search_good(start_page):
    time.sleep(5)
    start_page.search('lego')
    time.sleep(5)


def test_open_toy(start_page):
    time.sleep(15)
    start_page.open_toy()
    time.sleep(5)


def test_buy_toy(start_page):
    time.sleep(15)
    start_page.buy_toy()
    time.sleep(5)


def test_cookies_and_local_storage(start_page):
    start_page.cookies.add_cookie('doll', 'barbie')
    all_cookies= start_page.cookies.get_all_cookies()
    print(all_cookies)
    start_page.local_storage.set_item('any value', 'test value')
    start_page.local_storage.get_item('test value')



