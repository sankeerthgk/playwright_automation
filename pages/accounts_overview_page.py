from pages.base_page import BasePage

class AccountsOverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locator objects stored as class attributes
        self.welcome_text = page.locator("#leftPanel p.smallText")
        self.account_table = page.locator("table#accountTable")
        self.first_account = page.locator("#accountTable tr td a")


    def get_welcome_text(self):
        return self.get_text(self.welcome_text)

    def is_account_table_visible(self):
        return self.is_element_visible(self.account_table)

    def click_on_first_account(self):
        self.click(self.first_account.nth(0))
        self.page.wait_for_load_state("networkidle")

    def click_on_last_account(self):
        self.click(self.first_account.nth(-1))
        self.page.wait_for_load_state("networkidle")

    def click_on_last_but_one_account(self):
        self.click(self.first_account.nth(-2))
        self.page.wait_for_load_state("networkidle")
