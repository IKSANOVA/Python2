from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей отображения поста (пример URL — /blog/page/1/test-post/ или /blog/page/1)
class PostPage(BasePage):
    POST_TEXT = (By.CSS_SELECTOR, ".container p+p")
    SUBMIT_BUTTON = (By.ID, "submit")

    def check_post_text(self, text):
        post_text = self.wait_until_visible(self.POST_TEXT)
        assert post_text.text == text, "Неверный текст"

    def click_submit_button(self):
        self.wait_until_clickable(self.SUBMIT_BUTTON).click()