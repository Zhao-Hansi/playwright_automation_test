# playwright_automation_test
Automation test skills learning

**Initial playwright env:**

```
npm init playwright@latest
```

### Useful pytest CLI :
https://docs.pytest.org/en/6.2.x/usage.html

### Execute test commands in parallel
```
python3 -m pytest -m regression -n 2
```

### Execute the single test case:
```
python3 -m pytest -k test_case_name
```
### JS version reporter
```commandline
npx playwright test --reporter=html 
```
### JS version open the reporter
```commandline
npx playwright show-report    
```
### Python version record the video and take a screenshot when the cases is failed
```commandline
python3 -m pytest --headed --video retain-on-failure --screenshot=only-on-failure --output=./python_version_playwright/test-result -n 2
```
