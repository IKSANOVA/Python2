import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from api.blog_api import BlogApi
from conftest import url
from constants import Links
from functions import wait_until_clickable, wait_until_visible, element_is_present


@pytest.fixture()
def delete_user_posts(url):
    yield
    delete_user_posts(url)


@pytest.fixture()
def create_post_for_test(url, faker):
    api = BlogApi(url)
    title = faker.text(10)
    text = faker.text(100)
    api.create.post(title=title, text=text, tags=[faker.text(5)])
    return title, text


@pytest.mark.usefixtures("delete_user_posts")
class TestBlogOpen:

    def test_open_post(self, browser, create_post_for_test):
        title, text = create_post_for_test
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.XPATH, f'//h1[text()="{title}"]')).click()
        post_text = wait_until_clickable(browser, (By.CSS_SELECTOR, ".container p+p"))
        assert post_text.text == text, "Неверный текст"


@pytest.mark.usefixtures("delete_user_posts")
class TestsBlogModify:
    def test_create_post(self, browser, url, faker):
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.ID, "new")).click()
        title = faker.text(10)
        wait_until_clickable(browser, (By.ID, "title")).send_keys(title)
        wait_until_clickable(browser, (By.ID, "text")).send_keys(faker.text(100))
        wait_until_clickable(browser, (By.ID, "tags")).send_keys(faker.text(5))
        wait_until_clickable(browser, (By.ID, "submit")).click()

        assert "Blog posted successfully!" in wait_until_visible(browser, (By.ID, "alert_div")).text, \
            "Не отобразилось сообщение об успехе"
        assert wait_until_visible(browser, (By.TAG_NAME, "h1")).text == title, "Пост не опубликовался"

    def test_change_title(self, browser, url, create_post_for_test):
        title, _ = create_post_for_test
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.XPATH, f'//h1[text()="{title}"]')).click()
        wait_until_clickable(browser, (By.ID, "edit")).click()
        wait_until_clickable(browser, (By.ID, "title")).send_keys(Keys.BACKSPACE)
        wait_until_clickable(browser, (By.ID, "submit")).click()

        assert wait_until_visible(browser, (By.TAG_NAME, "h1")).text == title[:-1], "Пост не изменен"

    def test_delete_title(self, browser, url, create_post_for_test):
        title, _ = create_post_for_test
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.XPATH, f'//h1[text()="{title}"]')).click()
        wait_until_clickable(browser, (By.ID, "delete")).click()
        wait_until_clickable(browser, (By.ID, "confirmedDelete")).click()

        assert "Blog posted successfully!" in wait_until_visible(browser, (By.ID, "alert_div")).text, \
            "Не отобразилось сообщение об успехе"
        assert not element_is_present(browser, (By.XPATH, f'//h1[text()="{title}"]'), 1), "Пост не удален"