from playwright.sync_api import Page, expect
import re
from python_for_playwright.test_data import login_page_locator as login_page
from python_for_playwright.pages import login_page
import pytest


def test_example(page: Page):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")
    page.get_by_placeholder(login_page.login_page.username).fill(login_page.login_page.right_username)
    page.get_by_placeholder(login_page.login_page.password).click()
    page.get_by_placeholder(login_page.login_page.password).fill(login_page.login_page.right_password)
    page.get_by_role(login_page.login_page.login_button).click()
    page.locator("div").filter(has_text=re.compile(r"^商场管理$")).click()
    page.get_by_role("link", name="行政区域").click()
    page.get_by_role("cell", name=" 北京市").locator("i").click()
    page.locator("#tags-view-container").get_by_text("首页").click()


@pytest.mark.parametrize("username,password", [("hogwarts", "test12345")])
def test_cases_for_login(page: Page, username, password):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")
    login_page.login(page, username, password)