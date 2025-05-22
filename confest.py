import pytest
from selene import browser

@pytest.fixture(scope='session')
def setting_browser():
    print("open")
    browser.config.window_width = 800
    browser.config.window_height = 600
    yield
    browser.quit()