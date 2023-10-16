import pytest
from playwright.sync_api import Page


@pytest.fixture
def open_login_page(page: Page):
    page.goto("https://litemall.hogwarts.ceshiren.com/#/login")


def test_login_success(open_login_page):
    pass


@pytest.fixture(scope='function')
def take_screenshot(request, page):
    yield
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = f"python_version_playwright/screenshots/{test_name}.png"
        page.screenshot(path=screenshot_path, full_page=True)


@pytest.fixture
def record_video(page: Page):
    pass
