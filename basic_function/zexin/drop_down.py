import time

from playwright.sync_api import Page, expect
import re


def test_drop_down(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("select#dropdown", "Option 1")
    page.select_option("select#dropdown", "Option 2")