
from pages.account_details_page import AccountsDetailsPage
from pages.accounts_overview_page import AccountsOverviewPage
from pages.login_page import LoginPage
from pages.transfer_funds_page import TransferFundsPage


def test_login_ui_valid_credentials(page, base_urls, credentials, created_customer):
    login_to_app(base_urls["ui"], credentials, page)
    accounts_overview = AccountsOverviewPage(page)
    expected_welcome_text = "Welcome " + created_customer.FIRSTNAME + " " + created_customer.LASTNAME
    assert accounts_overview.get_welcome_text() == expected_welcome_text
    assert accounts_overview.is_account_table_visible()

def test_login_ui_invalid_credentials(page, base_urls, credentials):
    login = LoginPage(page)
    login.goto(base_urls["ui"])
    login.login('kvuykgugkjh', 'invalid')
    assert login.is_error_visible()
    assert login.get_credentials_error_text() == "The username and password could not be verified."
    accounts_overview = AccountsOverviewPage(page)
    assert not accounts_overview.is_account_table_visible()

def test_validate_account_details(page, base_urls, credentials, created_customer):
    login_to_app(base_urls["ui"], credentials, page)
    accounts_overview = AccountsOverviewPage(page)
    assert accounts_overview.is_account_table_visible()
    accounts_overview.click_on_first_account()
    account_details = AccountsDetailsPage(page)

    assert account_details.get_account_id() == "16674"
    assert account_details.get_account_type() == "CHECKING"
    assert "$6" in account_details.get_account_balance()
    assert not account_details.is_transaction_table_visible()


def test_transfer(page, base_urls, credentials, created_customer):
    login_to_app(base_urls["ui"], credentials, page)
    accounts_overview = AccountsOverviewPage(page)
    accounts_overview.click_on_last_account()
    account_details = AccountsDetailsPage(page)

    from_account = account_details.get_account_id()
    from_account_balance = float(account_details.get_account_balance().replace("$", ""))

    account_details.click_on_account_overview()
    accounts_overview.click_on_last_but_one_account()
    account_details = AccountsDetailsPage(page)
    to_account = account_details.get_account_id()
    to_account_balance = float(account_details.get_account_balance().replace("$", ""))

    account_details.click_on_transfer_funds()
    transfer_page = TransferFundsPage(page)
    transfer_page.select_from_account(from_account)
    transfer_page.select_to_account(to_account)
    transfer_page.enter_amount('10')
    transfer_page.click_transfer_button()

    assert transfer_page.get_transfer_result() == 'Transfer Complete!'
    assert transfer_page.get_transfer_result_amount() == '$10.00'

    transfer_page.click_on_account_overview()
    accounts_overview = AccountsOverviewPage(page)
    accounts_overview.click_on_last_account()
    account_details = AccountsDetailsPage(page)
    assert from_account_balance - float(account_details.get_account_balance().replace("$", "")) == 10

    account_details.click_on_account_overview()
    accounts_overview.click_on_last_but_one_account()
    account_details = AccountsDetailsPage(page)
    assert to_account_balance+10 == float(account_details.get_account_balance().replace("$", ""))


def login_to_app(url, credentials, page):
    login = LoginPage(page)
    login.goto(url)
    login.login(credentials["username"], credentials["password"])
