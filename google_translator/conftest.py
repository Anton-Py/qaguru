import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 500
    browser.config.window_height = 1000
    yield
    browser.quit()