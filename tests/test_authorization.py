import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from constants import POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS, Links
from functions import login_ui, wait_until_clickable, wait_until_present


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser, url):
        browser.get(url + Links.login)
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        wait_for_url_to_be(browser, url + Links.profile)
        assert browser.get_cookie("session"), "Не проставилась кука"
        assert url == "https://qastand.valhalla.pw/profile"

    @pytest.mark.parametrize("email,password", NEGATIVE_LOGIN_CREDENTIALS, ids=["test1", "test2", "test3", "test4"])
    def test_login_negatives(self, browser, url, email, password):
        browser.get(url + Links.login)
        login(browser, email, password)
        wait_for_url_to_be(browser, url + Links.login)
