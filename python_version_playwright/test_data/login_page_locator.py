# import sys
#
#
# class login_page:
#     username = '管理员账户'
#     password = '管理员密码'
#     login_button = 'button[name="登录"]'
#     right_username = 'hogwarts'
#     right_password = 'test12345'
#
#
# print(sys.path)
import time
from time import sleep

from playwright.sync_api import sync_playwright


class TestDemo():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_click(self):
        self.page.goto("http://www.baidu.com")

        self.page.click('id=s-top-loginbtn')
        self.page.pause()

        with self.context.expect_page() as new_page_info:
            self.page.click('"立即注册"')  # Opens a new tab
        register_page = new_page_info.value

        register_page.wait_for_load_state()
        print(register_page.title())
        # 注册用户名密码
        register_page.fill("id=TANGRAM__PSP_4__userName", "username")
        register_page.fill("id=TANGRAM__PSP_4__phone", "12345678")
        register_page.close()
        sleep(2)

        # 登录用户名密码
        self.page.fill("id=TANGRAM__PSP_11__userName", "username")
        self.page.fill("id=TANGRAM__PSP_11__password", "pwd")
        sleep(2)


def test_alert():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sahitest.com/demo/confirmTest.htm")
    page.pause()
    page.locator('body > form > input[type=button]:nth-child(1)').click()
    page.on("dialog", lambda dialog: print(dialog.message()))
    page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: dialog.dismiss())
    time.sleep(5000)

