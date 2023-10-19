import playwright
import pytest
from playwright.sync_api import Page


@pytest.fixture(scope='function', autouse=True)
def open_login_page(page: Page):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")
    page.set_default_timeout(3000)


def test_login_success(open_login_page):
    pass


@pytest.fixture(scope='function', autouse=True)
def take_screenshot(request, page):
    yield
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = f"../screenshots/{test_name}.png"
        page.screenshot(path=screenshot_path, full_page=True)


@pytest.fixture
def record_video(page: Page):
    pass


def pop_up_listen(page: Page):
    with page.expect_popup() as popup_info:
        page.click('button[name="登录"]')
    popup = popup_info.value

    popup.wait_for_load_state()
    print(popup.title())
    return popup.title()
