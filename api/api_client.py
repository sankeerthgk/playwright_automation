import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, params=None, json=None, headers=None):
        if headers is None:
            headers = {"Accept": "application/xml"}
        return requests.post(f"{self.base_url}{endpoint}", params=params, json=json, headers=headers)

    def get(self, endpoint, params=None, headers=None):
        if headers is None:
            headers = {"Accept": "application/json"}
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)
