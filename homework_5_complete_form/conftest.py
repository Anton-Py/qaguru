import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.timeout = 2.0
    driver_options = webdriver.FirefoxOptions()
    browser.config.driver_options = driver_options
    # driver_options.add_argument("--headless")
    browser.config.window_width = 1080
    browser.config.window_height = 1024

    yield

    browser.quit()