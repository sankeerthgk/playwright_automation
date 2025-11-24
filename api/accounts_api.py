import requests


class AccountsAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_account(self, account_id):
        return requests.get(f"{self.base_url}/api/accounts/{account_id}")
