from playwright.sync_api import Page, expect
import re


class HomePage_locator:
    user_amount = "#app > div > div.main-container > section > div > div > div:nth-child(1) > div > " \
                  "div.card-panel-description > div "
    products_amount = "#app > div > div.main-container > section > div > div > div:nth-child(2) > div > " \
                      "div.card-panel-description > div "
    orders_amount = "#app > div > div.main-container > section > div > div > div:nth-child(4) > div > " \
                    "div.card-panel-description > div "
    Merchandise_amount = "#app > div > div.main-container > section > div > div > div:nth-child(3) > div > " \
                         "div.card-panel-description > div "
    enter_admin_page_button = "#app > div > div.sidebar-container.el-scrollbar > " \
                              "div.scrollbar-wrapper.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > ul " \
                              "> div:nth-child(2) > li > div > svg > use "
    enter_product_manage_page_button = "#app > div > div.sidebar-container.el-scrollbar > " \
                                       "div.scrollbar-wrapper.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > " \
                                       "div > ul > div:nth-child(3) > li > div > svg > use"
    product_list_index = "#tags-view-container > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > " \
                         "div > span.tags-view-item.router-link-exact-active.router-link-active.active "


def go_to_admin_page(page: Page):
    page.locator(HomePage_locator.enter_admin_page_button).click()


def go_to_product_manage_page(page: Page):
    page.locator(HomePage_locator.enter_product_manage_page_button).click()


def go_to_product_list_page(page: Page):
    go_to_product_manage_page(page)
    page.locator("div").filter(has_text=re.compile(r"^商品列表$")).click()
    expect(page.locator(HomePage_locator.product_list_index)).to_be_visible()
    