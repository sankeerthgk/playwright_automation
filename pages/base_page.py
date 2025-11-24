from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Generic actions
    def click(self, locator):
        locator.click()

    def fill(self, locator, value):
        locator.fill(value)

    def get_text(self, locator):
        return locator.inner_text()

    def is_element_visible(self, locator):
        return locator.is_visible()

    def goto(self, url: str):
        self.page.goto(url)

    def wait_for_element(self, locator, timeout=10):
        locator.wait_for(state="visible", timeout=timeout)

    def select_option_from_dropdown(self, locator, value):
        locator.select_option(value=value)
