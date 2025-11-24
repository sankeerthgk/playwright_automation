Simple BANK application
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
├── api/
├── data/
├── pages/
├── conftest.py
├── tests/
    ├── ui/
    ├── api/
└── allure-results/
```

Notes:
- Update .env to point to your base_urls.
- To install Playwright browsers run: `playwright install`
- Run UI tests: `pytest tests/ui --env=dev --alluredir=allure-results`
- Run API tests: `pytest tests/api --env=dev --alluredir=allure-results`
- Serve Allure report: `allure serve allure-results`
