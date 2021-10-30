from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей создания/редактирования поста (/blog/editor/)
class PostModifyPage(BasePage):
    TITLE_FIELD = (By.ID, "title")
    TEXT_FIELD = (By.ID, "text")
    TAGS_FIELD = (By.ID, "tags")
    SUBMIT_BUTTON = (By.ID, "submit")
    EDIT_BUTTON = (By.ID, "edit")
    TITLE = (By.TAG_NAME, "h1")
    DELETE_BUTTON = (By.ID, "delete")
    CONFIRMED_BUTTON = (By.ID, "confirmedDelete")

    def add_title(self, title):
        self.wait_until_clickable(self.TITLE_FIELD).send_keys(title)

    def add_text(self, text):
        self.wait_until_clickable(self.TEXT_FIELD).send_keys(text)

    def add_tags(self, tags):
        self.wait_until_clickable(self.TAGS_FIELD).send_keys(tags)

    def click_submit_button(self):
        self.wait_until_clickable(self.SUBMIT_BUTTON).click()

    def click_edit_button(self):
        self.wait_until_clickable(self.EDIT_BUTTON).click()

    def click_title_button(self):
        self.wait_until_clickable(self.TITLE).click()

    def click_delete_button(self):
        self.wait_until_clickable(self.DELETE_BUTTON).click()

    def click_confirmed_button(self):
        self.wait_until_clickable(self.CONFIRMED_BUTTON).click()


