import pytest

from pages.auth_page import AuthPage
from constants import POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS, Links
from pages.base_page import BasePage
from pages.blog_pages.main_pages import MainPage


@pytest.mark.usefixtures()
class TestAuthorization:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.auth_page = AuthPage(browser, url + Links.login)
        self.base_page = BasePage(browser, url + Links.blog)
        self.main_page = MainPage(browser, url + Links.blog)

    def test_login_positive(self):

        self.auth_page.open_page()
        self.auth_page.add_email(POSITIVE_LOGIN_CREDENTIALS["email"])
        self.auth_page.add_password(POSITIVE_LOGIN_CREDENTIALS["password"])
        self.auth_page.click_button_auth()

    @pytest.mark.parametrize("email, password",
                             NEGATIVE_LOGIN_CREDENTIALS,
                             ids=["empty email", "empty password", "invalid email", "unregistered user"])
    def test_login_negative(self, email, password):
        self.auth_page.open_page()
        self.auth_page.add_email(email)
        self.auth_page.add_password(password)
        self.auth_page.click_button_auth()

    @pytest.mark.usefixtures("login")
    def test_logout(self):
        self.base_page.open_page()
        self.base_page.click_button_exit()
        self.base_page.open_page()
        self.main_page.check_button_new()




