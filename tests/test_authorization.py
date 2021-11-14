import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from constants import POSITIVE_LOGIN_CREDENTIALS, page_login, NEGATIVE_LOGIN_CREDENTIALS
from functions import login_ui, wait_until_clickable, wait_until_present


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser):
        browser.get(page_login)
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        url = browser.current_url
        browser.get_cookie("session")
        assert browser.get_cookie("session"), "Неверная session"
        assert url == "https://qastand.valhalla.pw/profile"

    @pytest.mark.parametrize("email,password", NEGATIVE_LOGIN_CREDENTIALS, ids=["test1", "test2", "test3", "test4"])
    def test_login_negatives(self, email, password):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/login')
            wait_until_clickable(browser, (By.NAME, 'email')).send_keys(email)
            wait_until_clickable(browser, (By.NAME, 'password')).send_keys(password)
            wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
            assert wait_until_present(browser, (By.CLASS_NAME, 'is-danger'))
