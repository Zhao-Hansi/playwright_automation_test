import re
import time

from playwright.sync_api import Page, expect


def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    page.locator("#column-a").drag_to(page.locator("#column-b"))
    time.sleep(3)