from playwright.sync_api import Page, expect
from python_version_playwright.pages import product_list_page
from python_version_playwright.pages import login_page
from python_version_playwright.pages import home_page
from python_version_playwright.common_function.common import open_page


def test_search_product_by_id(take_screenshot, open_page, page: Page):
    login_page.login(page, login_page.login_page_locator.right_username, login_page.login_page_locator.right_password)
    home_page.go_to_product_list_page(page)
    product_list_page.search_product_by_id(page, "1")
    expect(page.get_by_text(product_list_page.product_list_page_locator.no_search_result)).to_be_visible()

