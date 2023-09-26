from playwright.sync_api import Page, expect


def test_for_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input[type=\"checkbox\"]").nth(0).check()
    page.locator("input[type=\"checkbox\"]").nth(1).uncheck()
    expect(page.locator("input[type=\"checkbox\"]").nth(0)).to_be_checked()
    expect(page.locator("input[type=\"checkbox\"]").nth(1)).not_to_be_checked()