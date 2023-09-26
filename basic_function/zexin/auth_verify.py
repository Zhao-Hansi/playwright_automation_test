from playwright.sync_api import Page, expect
import re


def test_auth_verify(page: Page):
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Username").type("admin")
    page.get_by_text("Password").type("admin")
    page.get_by_text("Sign in").click()
    expect(page.get_by_text("Congratulations! You must have the proper credentials.")).to_be_visible()


def test_auth_no_verify(page: Page):
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("cancel").click()
    expect(page.get_by_text("Not authorized")).to_be_visible()
