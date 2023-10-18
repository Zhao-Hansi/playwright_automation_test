from playwright.sync_api import Page, expect
from python_version_playwright.pages import home_page


class product_list_page:
    def __init__(self, page: Page):
        self.search_button = "#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4) > " \
                             "span "
        self.add_button = "#app > div > div.main-container > section > div > div.filter-container > button:nth-child(5) > span"
        self.product_id_input = "#app > div > div.main-container > section > div > div.filter-container > div:nth-child(1) > " \
                                "input"
        self.product_number_input = "#app > div > div.main-container > section > div > div.filter-container > div:nth-child(2) " \
                                    "> input"
        self.product_name_input = "#app > div > div.main-container > section > div > div.filter-container > div:nth-child(3) > " \
                                  "input "
        self.no_search_result = "暂无数据"
        self.search_button = page.locator(self.search_button)
        self.add_button = page.locator(self.add_button)
        self.product_id_input = page.locator(self.product_id_input)
        self.product_name_input = page.locator(self.product_name_input)
        self.product_number_input = page.locator(self.product_number_input)

    def click_search_button(self):
        self.search_button.click()

    def search_product_by_id(self, product_id):
        self.product_id_input.fill(product_id)
        self.click_search_button()

    def search_product_by_name(self, product_name):
        self.product_name_input.fill(product_name)
        self.click_search_button()

    def search_product_by_number(self, product_number):
        self.product_number_input.fill(product_number)
        self.click_search_button()
