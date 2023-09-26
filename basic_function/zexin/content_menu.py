from playwright.sync_api import Page, expect


def handle_dialog(dialog):
    """监听后处理"""
    print(dialog.message)
    dialog.dismiss()


def test_content_menu(page: Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page.locator("#hot-spot").click(button="right")
    page.wait_for_timeout(3000)
    page.on("dialog", handle_dialog)