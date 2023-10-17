import re

from playwright.sync_api import Page, expect
from python_version_playwright.pages import home_page


class login_page:
    username = '管理员账户'
    password = '管理员密码'
    login_button = 'button[name="登录"]'
    right_username = 'hogwarts'
    right_password = 'test12345'

    def __init__(self, page: Page):
        self.username = page.get_by_placeholder(login_page.username)
        self.password = page.get_by_placeholder(login_page.password)
        self.login_button = page.get_by_role(login_page.login_button)
        self.right_username = login_page.right_username
        self.right_password = login_page.right_password

    def login(self, username, password):
        self.username.fill(username)
        self.password.click()
        self.password.fill(password)
        self.login_button.click()


def handle_dialog(alert, expect_message):
    alert.accept()


class login_page_function:
    pass
