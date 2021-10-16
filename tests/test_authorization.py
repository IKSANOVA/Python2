import email

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from constants import POSITIVE_LOGIN_CREDENTIALS, page_login
from functions import login_ui


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser):
        browser.get(page_login)
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        url = browser.current_url
        browser.get_cookie("session")
        assert url == "https://qastand.valhalla.pw/profile"
