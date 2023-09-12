import time


def test_open_shoes(dashboard):
    time.sleep(5)
    dashboard.open_shoes()
    time.sleep(5)


def test_open_particular_good(dashboard):
    dashboard.open_shoes()
    time.sleep(5)
    dashboard.open_good()
    time.sleep(5)


def test_open_sign_in(dashboard):
    time.sleep(5)
    dashboard.open_sign_in_form()
    time.sleep(5)


def test_search_good(dashboard):
    time.sleep(5)
    dashboard.open_search()
    time.sleep(5)
    dashboard.search_good('чоботи')
    time.sleep(5)


def test_ask_about_good_form_opened(dashboard):
    dashboard.open_shoes()
    time.sleep(5)
    dashboard.open_good()
    time.sleep(5)
    dashboard.ask_about_good()
    time.sleep(5)