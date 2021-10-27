import pytest
from selenium.webdriver.common.by import By
from webbrowser import UnixBrowser

from constants import Links
from functions import wait_until_clickable, wait_until_present, login_ui


@pytest.mark.smoke
class TestBlogClass:

    def test_blog_positive(self, browser: UnixBrowser):
        browser.open_new(url + Links.blog)
        wait_until_clickable(browser, (By.CSS_SELECTOR, "[href = '/blog/page/1/test-post/']")).click()
        element = wait_until_clickable(browser, (By.CSS_SELECTOR, "p:nth-child(5)")).text
        assert element == 'Hello world!'

