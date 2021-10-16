import email

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from constants import NEGATIVE_LOGIN_CREDENTIALS, POSITIVE_LOGIN_CREDENTIALS, page_login
from functions import wait_until_clickable, wait_until_present, login_ui


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser):
        browser.get(page_login)
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        url = browser.current_url
        browser.get_cookie("session")
        assert url == "https://qastand.valhalla.pw/profile"
