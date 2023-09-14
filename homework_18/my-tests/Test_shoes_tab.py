import time


def test_open_particular_good(dashboard):
    dashboard.open_shoes()
    time.sleep(5)
    dashboard.open_good()
    time.sleep(5)


def test_ask_about_good_form_opened(dashboard):
    dashboard.open_shoes()
    time.sleep(5)
    dashboard.open_good()
    time.sleep(5)
    dashboard.ask_about_good()
    time.sleep(5)


