import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_remove_and_add_button(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.get_by_text("Add Element").click()
    expect(page.get_by_text("Delete")).to_be_visible()
    page.get_by_text("Delete").click()
    expect(page.get_by_text("Delete")).not_to_be_visible()
