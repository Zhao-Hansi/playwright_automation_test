from playwright.sync_api import Page, expect
import re


class home_page:
    def __init__(self, page: Page):
        self.user_amount = "#app > div > div.main-container > section > div > div > div:nth-child(1) > div > " \
                           "div.card-panel-description > div "
        self.products_amount = "#app > div > div.main-container > section > div > div > div:nth-child(2) > div > " \
                               "div.card-panel-description > div "
        self.orders_amount = "#app > div > div.main-container > section > div > div > div:nth-child(4) > div > " \
                             "div.card-panel-description > div "
        self.Merchandise_amount = "#app > div > div.main-container > section > div > div > div:nth-child(3) > div > " \
                                  "div.card-panel-description > div "
        self.enter_admin_page_button = "#app > div > div.sidebar-container.el-scrollbar > " \
                                       "div.scrollbar-wrapper.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > ul " \
                                       "> div:nth-child(2) > li > div > svg > use "
        self.enter_product_manage_page_button = "#app > div > div.sidebar-container.el-scrollbar > " \
                                                "div.scrollbar-wrapper.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > " \
                                                "div > ul > div:nth-child(3) > li > div > svg > use"
        self.product_list_index = "#tags-view-container > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > " \
                                  "div > span.tags-view-item.router-link-exact-active.router-link-active.active "
        self.user_amount = page.locator(self.user_amount)
        self.products_amount = page.locator(self.products_amount)
        self.orders_amount = page.locator(self.orders_amount)
        self.Merchandise_amount = page.locator(self.Merchandise_amount)
        self.enter_admin_page_button = page.locator(self.enter_admin_page_button)
        self.enter_product_manage_page_button = page.locator(self.enter_product_manage_page_button)
        self.product_list_index = page.locator(self.product_list_index)

    def go_to_admin_page(self):
        self.enter_admin_page_button.click()

    def go_to_product_manage_page(self):
        self.enter_product_manage_page_button.click()

    def go_to_product_list_page(self, page: Page):
        self.go_to_product_manage_page()
        page.locator("div").filter(has_text=re.compile(r"^商品列表$")).click()
        expect(self.product_list_index).to_be_visible()
