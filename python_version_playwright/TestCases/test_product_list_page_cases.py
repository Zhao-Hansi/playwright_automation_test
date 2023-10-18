import pytest
from playwright.sync_api import Page, expect
from python_version_playwright.pages.product_list_page import product_list_page
from python_version_playwright.pages.login_page import login_page
from python_version_playwright.pages.home_page import home_page
from python_version_playwright.common_function.common import open_login_page, take_screenshot


@pytest.mark.product
def test_search_product_by_id(page: Page):
    LoginPage = login_page(page)
    HomePage = home_page(page)
    ProductListPage = product_list_page(page)
    LoginPage.login(LoginPage.right_username, LoginPage.right_password)
    home_page.go_to_product_list_page(HomePage, page)
    ProductListPage.search_product_by_id("1")
    expect(page.get_by_text(ProductListPage.no_search_result)).to_be_visible()

