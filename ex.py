from asyncio import timeout_at

import pytest
from selene import browser, have
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="function")
# def test_page_title_selene():
#     options = Options()
#     # options.add_argument("--headless")
#     browser.config.window_width = 500
#     browser.config.window_height = 1000
#     browser.config.driver_options = options
#
#     browser.open("https://playground.learnqa.ru/api/map")
#     # browser.element('p').should(have.text('Это тестовое API для наших курсов и вебинаров:'))
#     # browser.element('h1').should(have.text('LearnQA API'))

from selene import browser, have

def test_validate_after_5_seconds_selene():
    browser.open("https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php")
    browser.element("#colorChange").click()
    browser.element("visibleAfter").with_(timeout=browser.config.timeout * 2).should(have.text("Visible After 5 Seconds"))
