NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                              "password": "!QAZ2wsx"}

page_login = "https://qastand.valhalla.pw/login"
page_blog = "https://qastand.valhalla.pw/blog/author/2/"


class Links:
    base_url = "https://qastand.valhalla.pw/"
    login = base_url + "login"
    profile = base_url + "profile"
    blog = base_url + "blog"


SESSION_COOKIE = {"name": 'session',
                  "value": '.eJwlzjEOwjAMRuG7ZGbI79hN3MtUcmwL1pROiLtTif096fuUI1ecz7K_1xWPcry87MXJYsTcIIQ2h5EGTCAT7NA'
                           '-muVmLl6pE3MN60jUqdInFDyamDQHRzZKakhKjNpUddyXdGUWdmEdd8zgTrOKwKhap6xcbsh1xvprpHx_OG4syg'
                           '.YWqCMg.L--C-U8_k9BoHAWPTIkpCoa1M4I'}
