import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import wait_until_clickable, wait_until_not_present, PARAMETER_FOR_TEST, wait_until_present


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self):
        with Chrome() as browser:
            browser.maximize_window()
            browser.get('https://qastand.valhalla.pw/login')
            wait_until_clickable(browser, (By.NAME, 'email')).send_keys("qa_test@test.ru")
            wait_until_clickable(browser, (By.NAME, 'password')).send_keys("!QAZ2wsx")
            wait_until_clickable(browser, (By.CSS_SELECTOR, '[type=checkbox]')).click()
            wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
            url = browser.current_url
            browser.get_cookie("session")
            assert url == "https://qastand.valhalla.pw/profile"

    @pytest.mark.parametrize("email,password", PARAMETER_FOR_TEST, ids=["test1", "test2", "test3", "test4"])
    def test_login_negatives(self, email, password):
        with Chrome() as browser:
            browser.maximize_window()
            browser.get('https://qastand.valhalla.pw/login')
            wait_until_clickable(browser, (By.NAME, 'email')).send_keys(email)
            wait_until_clickable(browser, (By.NAME, 'password')).send_keys(password)
            wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
            assert wait_until_present(browser, (By.CLASS_NAME, 'is-danger'))

    # @pytest.mark.parametrize("email", PARAMETER_FOR_TEST_EMAIL)
    # @pytest.mark.parametrize("password", PARAMETER_FOR_TEST_PASS)
    # def test_login_negatives(self, email, password):
    #     with Chrome() as browser:
    #         browser.maximize_window()
    #         browser.get('https://qastand.valhalla.pw/login')
    #         wait_until_clickable(browser, (By.NAME, 'email')).send_keys(email)
    #         wait_until_clickable(browser, (By.NAME, 'password')).send_keys(password)
    #         wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
    #         assert wait_until_not_present(browser, (By.CLASS_NAME, 'is-danger'))
