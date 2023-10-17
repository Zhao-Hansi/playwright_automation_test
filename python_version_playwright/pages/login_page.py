import re

from playwright.sync_api import Page, expect
from python_version_playwright.pages import home_page


class login_page:

    def __init__(self, page: Page):
        self.username = '管理员账户'
        self.password = '管理员密码'
        self.login_button = 'button[name="登录"]'
        self.right_username = 'hogwarts'
        self.right_password = 'test12345'
        self.username = page.get_by_placeholder(self.username)
        self.password = page.get_by_placeholder(self.password)
        self.login_button = page.get_by_role(self.login_button)
        self.right_username = self.right_username
        self.right_password = self.right_password

    def login(self, username, password):
        self.username.fill(username)
        self.password.click()
        self.password.fill(password)
        self.login_button.click()

    def handle_dialog(self, alert, expect_message):
        alert.accept(expect_message)


class login_page_function:
    pass
