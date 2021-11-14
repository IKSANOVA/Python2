from selenium.webdriver import Opera, Chrome, Remote

VALID_BROWSERS = {
   "chrome": Chrome,
   "opera": Opera,
   "remote": Remote
}

BROWSER_REMOTE_CAPABILITIES = {
      "browserName": "chrome",
      "version": "95.0",
      "enableVNC": True,
  }

SELENOID_URL = 'http://localhost:4444/wd/hub'


COMMAND_EXECUTOR = 'http://localhost:4444/wd/hub'


NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

# здесь должны быть креденшелзы, присланные преподавателем
POSITIVE_LOGIN_CREDENTIALS = {"email": "api_user_9@test.ru",
                              "password": "q9w9e9"}


class Links:
    base_url = {"prod": "https://qastand.valhalla.pw/",
                "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"
