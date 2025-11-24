import time

from pages.accounts_overview_page import AccountsOverviewPage
from pages.base_page import BasePage

class AccountsDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locator objects stored as class attributes
        self.account_id = page.locator("#accountDetails #accountId")
        self.account_type = page.locator("#accountDetails #accountType")
        self.account_balance = page.locator("#accountDetails #balance")
        self.no_transactions_text = page.locator("#accountDetails #noTransactions")
        self.transaction_table = page.locator("#accountDetails #transactionTable")
        self.accounts_overview = page.get_by_role("link", name="Accounts Overview")
        self.transfer_funds = page.get_by_role("link", name="Transfer Funds")

    def get_account_id(self):
        return self.get_text(self.account_id)
    def get_account_type(self):
        return self.get_text(self.account_type)
    def get_account_balance(self):
        return self.get_text(self.account_balance)

    def is_transaction_table_visible(self):
        return self.is_element_visible(self.transaction_table)
    def is_no_transactions_text_visible(self):
        return self.is_element_visible(self.no_transactions_text)

    def click_on_account_overview(self):
        self.click(self.accounts_overview)

    def click_on_transfer_funds(self):
        self.click(self.transfer_funds)