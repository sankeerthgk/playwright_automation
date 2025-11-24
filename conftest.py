import json
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import allure

from api.api_client import APIClient
from data.customer import Customer

IS_CI = os.getenv("CI") == "true"

# Load .env only when NOT in CI
if not IS_CI:
    load_dotenv()

# ----------------------------
# Environment selection
# ----------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default=os.getenv("ENV", "dev"),
        choices=["dev", "qa", "stage", "prod"],
        help="Select environment",
    )

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_urls(env):
    return {
        "ui": os.getenv(f"{env.upper()}_UI_URL"),
        "api": os.getenv(f"{env.upper()}_API_URL"),
    }

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
    }

# ----------------------------
# Playwright fixtures
# ----------------------------
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False if not IS_CI else True)
        yield browser
        browser.close()

@pytest.fixture()
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def created_customer(base_urls, credentials):
    file_path = 'data/customer_data.json'
    with open(file_path, "r") as f:
        data = json.load(f)
    Customer.FIRSTNAME = data["first_name"]
    Customer.LASTNAME = data["last_name"]
    Customer.ADDRESS_STREET = data["address_street"]
    Customer.ADDRESS_CITY = data["address_city"]
    Customer.ADDRESS_STATE = data["address_state"]
    Customer.ADDRESS_ZIP = data["address_zipcode"]
    Customer.PHONE_NUMBER = data["phone_number"]
    Customer.SSN = data["ssn"]
    api = APIClient(base_urls["api"])
    endpoint = "/customers/update/" + str(Customer.CUSTOMER_ID)
    params = {
        "firstName": Customer.FIRSTNAME,
        "lastName": Customer.LASTNAME,
        "street": Customer.ADDRESS_STREET,
        "city": Customer.ADDRESS_CITY,
        "state": Customer.ADDRESS_STATE,
        "zipCode": Customer.ADDRESS_ZIP,
        "phoneNumber": Customer.PHONE_NUMBER,
        "ssn": Customer.SSN,
        "username": credentials["username"],
        "password": credentials["password"]
    }
    response = api.post(endpoint, params=params)
    assert response.ok
    return Customer


# ----------------------------
# Screenshot on failure
# ----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
