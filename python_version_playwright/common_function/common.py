import pytest
from playwright.sync_api import Page


@pytest.fixture
def open_page(page: Page):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")


def test_login_success(open_page):
    # 使用open_page fixture打开登录页面
    # 在这里执行登录测试逻辑
    pass