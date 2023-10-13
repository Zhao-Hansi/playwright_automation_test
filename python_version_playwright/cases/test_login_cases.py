from playwright.sync_api import Page, expect
import re
from python_version_playwright.pages import login_page
import pytest


def test_example(page: Page):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")
    page.get_by_placeholder(login_page.login_page_locator.username).fill(login_page.login_page_locator.right_username)
    page.get_by_placeholder(login_page.login_page_locator.password).click()
    page.get_by_placeholder(login_page.login_page_locator.password).fill(login_page.login_page_locator.right_password)
    page.get_by_role(login_page.login_page_locator.login_button).click()
    page.locator("div").filter(has_text=re.compile(r"^商场管理$")).click()
    page.get_by_role("link", name="行政区域").click()
    page.get_by_role("cell", name=" 北京市").locator("i").click()
    page.locator("#tags-view-container").get_by_text("首页").click()


@pytest.mark.parametrize("username,password", [("hogwarts", "test12345")])
def test_cases_for_login(page: Page, username, password):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")
    login_page.login(page, username, password)