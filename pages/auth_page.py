from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей авторизации (/login)
class AuthPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    BUTTON_AUTH = (By.CLASS_NAME, "button")

    def add_email(self, text):
        self.wait_until_clickable(self.EMAIL).send_keys(text)

    def add_password(self, text):
        self.wait_until_clickable(self.PASSWORD).send_keys(text)

    def click_button_auth(self):
        self.wait_until_clickable(self.BUTTON_AUTH).click()
