import re

import pytest
from playwright.sync_api import Page, expect

from python_version_playwright.pages.home_page import home_page
from python_version_playwright.pages.login_page import login_page
from python_version_playwright.common_function.common import open_login_page, take_screenshot, pop_up_listen


@pytest.mark.flaky(reruns=1)
@pytest.mark.login
def test_example(page: Page):
    LoginPage = login_page(page)
    LoginPage.username.click()
    LoginPage.username.fill(LoginPage.right_username)
    LoginPage.password.click()
    LoginPage.password.fill(LoginPage.right_password)
    LoginPage.login_button.click()


@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize("username,password", [("hogwarts", "test12345")])
def test_cases_for_login(page: Page, username, password):
    LoginPage = login_page(page)
    HomePage = home_page(page)
    LoginPage.login(username, password)
    expect(page.locator("div").filter(has_text=re.compile(r"^商场管理$"))).not_to_be_empty()
    expect(HomePage.user_amount).to_be_visible()
    expect(HomePage.products_amount).to_be_visible()
    expect(HomePage.orders_amount).to_be_visible()
    expect(HomePage.Merchandise_amount).to_be_visible()


@pytest.mark.xfail(reason='the handle dialog function is not ready')
@pytest.mark.login
@pytest.mark.parametrize("username,password,expect_message", [("hogwarts1", "test12345", "用户帐号或密码不正确")])
def test_login_failed(open_login_page, take_screenshot, page: Page, username, password, expect_message):
    LoginPage = login_page(page)
    LoginPage.login(username, password)
    with page.expect_popup() as popup_info:
        page.get_by_role('button').click()
    popup = popup_info.value

    popup.wait_for_load_state()
    print(popup.title())
    # page.on("dialog", lambda dialog: print(dialog.message))
    # page.get_by_role("button").click()  # Will hang here
    # page.on("dialog", lambda dialog: expect(dialog.message().to_contain_text(expect_message)))
