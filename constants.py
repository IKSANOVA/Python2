from webbrowser import Chrome, Opera

NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                              "password": "!QAZ2wsx"}


class Links:
    url = {"prod": "https://qastand.valhalla.pw/",
           "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"


VALID_BROWSER = {
    "chrome": Chrome,
    "opera": Opera

}
