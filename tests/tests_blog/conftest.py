import pytest
from selenium.webdriver import Chrome

from constants import page_login
from functions import login_cookie


@pytest.fixture(autouse=True)
def browser():
    browser = Chrome()
    browser.maximize_window()
    browser.get(page_login)
    login_cookie(browser)
    yield browser
    browser.quit()


