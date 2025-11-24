# Pytest + Playwright + Requests + Allure Example

This is a simple starter QA project with:
- Pytest for test runner
- Playwright for UI automation
- requests for API tests
- Allure for reporting

Project structure:
```
project/
├── requirements.txt
├── pytest.ini
├── README.md
├── conftest.py
├── tests/
└── allure-results/ (generated after running tests)
```

Notes:
- Update the `api_client.base_url` in `conftest.py` to point to your API.
- Replace example selectors and URLs in UI tests with real application values.
- To install Playwright browsers run: `playwright install`
- Run tests: `pytest`
- Serve Allure report: `allure serve allure-results`
