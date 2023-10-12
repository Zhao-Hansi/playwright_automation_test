from playwright.sync_api import Page, expect
from python_version_playwright.pages import home_page


class product_list_page_locator:
    search_button = "#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4) > " \
                    "span "
    add_button = "#app > div > div.main-container > section > div > div.filter-container > button:nth-child(5) > span"
    product_id_input = "#app > div > div.main-container > section > div > div.filter-container > div:nth-child(1) > " \
                       "input"
    product_number_input = "#app > div > div.main-container > section > div > div.filter-container > div:nth-child(2) " \
                           "> input"
    product_name_input = "#app > div > div.main-container > section > div > div.filter-container > div:nth-child(3) > " \
                         "input "


def click_search_button(page: Page):
    page.locator(product_list_page_locator.search_button).click()


def search_product_by_id(page: Page, product_id):
    page.locator(product_list_page_locator.product_id_input).fill(product_id)
    click_search_button(page)


def search_product_by_name(page: Page, product_name):
    page.locator(product_list_page_locator.product_name_input).fill(product_name)
    click_search_button(page)


def search_product_by_number(page: Page, product_number):
    page.locator(product_list_page_locator.product_number_input).fill(product_number)
    click_search_button(page)

