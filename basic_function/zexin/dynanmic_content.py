from playwright.sync_api import Page, expect


def test_dynamic_content(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_content")
    expect(page.locator("#content > div > h3")).to_have_text("Dynamic Content")
    page.locator("#content > div > p:nth-child(3) > a").click()
