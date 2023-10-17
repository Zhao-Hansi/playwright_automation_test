import re

import pytest
from playwright.sync_api import Page, expect

from python_version_playwright.pages import home_page
from python_version_playwright.pages.login_page import login_page
from python_version_playwright.common_function.common import open_login_page, take_screenshot


@pytest.mark.flaky(reruns=1)
@pytest.mark.login
def test_example(page: Page):
    LoginPage = login_page(page)
    LoginPage.username.click()
    LoginPage.username.fill(LoginPage.right_username)
    LoginPage.password.click()
    LoginPage.password.fill(LoginPage.right_password)
    LoginPage.login_button.click()
    page.locator("div").filter(has_text=re.compile(r"^商场管理$")).click()
    page.get_by_role("link", name="行政区域").click()
    page.get_by_role("cell", name=" 北京市").locator("i").click()
    page.locator("#tags-view-container").get_by_text("首12页").click()


@pytest.mark.login
@pytest.mark.parametrize("username,password", [("hogwarts", "test12345")])
def test_cases_for_login(page: Page, username, password):
    LoginPage = login_page(page)
    LoginPage.login(username, password)
    expect(page.locator("div").filter(has_text=re.compile(r"^商场管理$"))).not_to_be_empty()
    expect(page.locator(home_page.HomePage_locator.user_amount)).to_be_visible()
    expect(page.locator(home_page.HomePage_locator.products_amount)).to_be_visible()
    expect(page.locator(home_page.HomePage_locator.orders_amount)).to_be_visible()
    expect(page.locator(home_page.HomePage_locator.Merchandise_amount)).to_be_visible()


@pytest.mark.debug
@pytest.mark.parametrize("username,password,expect_message", [("hogwarts1", "test12345", "用户帐号或密码不正确")])
def test_login_failed(open_login_page, take_screenshot, page: Page, username, password, expect_message):
    page.pause()
    LoginPage = login_page(page)
    LoginPage.login(username, password)
    LoginPage.handle_dialog(page)


