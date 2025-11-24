import pytest
from api.api_client import APIClient
from data.customer import Customer


@pytest.mark.api
def test_get_customer_accounts(base_urls, created_customer):

    api = APIClient(base_urls["api"])
    endpoint = f"/customers/{Customer.CUSTOMER_ID}/accounts"
    print("endpoint: " + endpoint)
    response = api.get(endpoint)
    assert response.status_code == 400

def test_account_details(base_urls, credentials):

    api = APIClient(base_urls["api"])
    response = api.get("/accounts/13899")
    assert response.status_code == 200
    assert response.json()["id"] == 13899
    assert response.json()["type"] == 'CHECKING'
    assert response.json()["balance"] == 100.00

def test_customer_details(base_urls, credentials):

    api = APIClient(base_urls["api"])
    response = api.get("/customers/12878")
    assert response.status_code == 200
    assert response.json()["id"] == 12878

def test_deposit_funds(base_urls, credentials):

    api = APIClient(base_urls["api"])
    endpoint = "/deposit"
    params = {
        "accountId": "13677",
        "amount": "100"
    }
    response = api.post(endpoint, params=params)
    assert response.status_code == 200
    assert response.content == b'Successfully deposited $100 to account #13677'