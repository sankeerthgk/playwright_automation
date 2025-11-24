import time

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locator objects stored as class attributes
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("div.login input.button")
        self.error_heading = page.get_by_role("heading", name="Error!")
        self.credentials_error_text = page.locator("#rightPanel p.error")

    def is_error_visible(self):
        return self.is_element_visible(self.error_heading)

    def get_credentials_error_text(self):
        return self.get_text(self.credentials_error_text)

    def goto_login(self, url: str):
        self.goto(url)

    def login(self, username: str, password: str):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)


