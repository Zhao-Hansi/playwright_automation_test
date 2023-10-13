from playwright.sync_api import Page, expect
from python_version_playwright.pages import product_list_page
from python_version_playwright.pages import login_page
from python_version_playwright.pages import home_page


def test_search_product_by_id(page: Page):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")
    login_page.login(page, login_page.login_page_locator.right_username, login_page.login_page_locator.right_password)
    home_page.go_to_product_list_page(page)
    product_list_page.search_product_by_id(page, "1")
    expect(page.get_by_text("暂无数据")).to_be_visible()

