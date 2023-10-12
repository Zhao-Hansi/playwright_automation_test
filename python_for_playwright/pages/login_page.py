import re

from playwright.sync_api import Page, expect


class login_page_locator:
    username = '管理员账户'
    password = '管理员密码'
    login_button = 'button[name="登录"]'
    right_username = 'hogwarts'
    right_password = 'test12345'


def login(page: Page, username, password):
    page.get_by_placeholder(login_page_locator.username).fill(username)
    page.get_by_placeholder(login_page_locator.password).click()
    page.get_by_placeholder(login_page_locator.password).fill(password)
    page.get_by_role(login_page_locator.login_button).click()
    expect(page.locator("div").filter(has_text=re.compile(r"^商场管理$"))).not_to_be_empty()


class login_page_function:
    pass
