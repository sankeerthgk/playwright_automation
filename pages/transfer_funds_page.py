import time

from pages.accounts_overview_page import AccountsOverviewPage
from pages.base_page import BasePage

class TransferFundsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locator objects stored as class attributes
        self.from_account = page.locator("#transferForm #fromAccountId")
        self.to_account = page.locator("#transferForm #toAccountId")
        self.amount = page.locator('#transferForm #amount')
        self.transfer_button = page.get_by_role("button", name="Transfer")
        self.transfer_result = page.locator("#showResult h1")
        self.result_amount = page.locator("#showResult span#amountResult")
        self.accounts_overview = page.get_by_role("link", name="Accounts Overview")

    def select_from_account(self, value):
        self.select_option_from_dropdown(self.from_account, value)
    def select_to_account(self, value):
        self.select_option_from_dropdown(self.to_account, value)
    def enter_amount(self, value):
        self.fill(self.amount, value)
    def click_transfer_button(self):
        self.click(self.transfer_button)
        self.page.wait_for_load_state("networkidle")
    def get_transfer_result(self):
        return self.get_text(self.transfer_result)
    def get_transfer_result_amount(self):
        return self.get_text(self.result_amount)
    def click_on_account_overview(self):
        self.click(self.accounts_overview)
