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
