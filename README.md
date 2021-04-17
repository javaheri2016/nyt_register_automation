# The New York Times sign up and log in automated script

This project for web automation of The New York Times 

Technology stack: [Python](https://www.python.org/), [Selenium](https://www.selenium.dev/), 
[PyTest](https://docs.pytest.org/en/stable/), [PyTest BDD](https://pypi.org/project/pytest-bdd/).

Page Object Model was used as a design pattern.

### Directory structure

```
├── pages                                               # folder contains page objects and suitable test cases
├── tests                                               # folder contains relevant Gherkin steps
├── driver.py                                           # webdriver settings
├── helpers.py                                          # supporting functions and data generator
├── locators.py                                         # all locators used in the project                             
├── README.md                                           
├── requirements.in                                     # using pip-compile to be compiled to reqirements.txt
├── requirements.txt                                    # pip requirements file
├── test_data.py                                        # contains test data urls, titles, messages and error texts
├── test_run.py                                         # main test runner
├── test_scenarios.feature                              # contains Gherkin scenarios  
└── README.md
```

### Local environment setup

To use this project Python 3.8. is required.

```
python3.8 -m venv venv
pip install -r requirements.txt
```

To run tests locally Selenium Webdriver is required. 
In this project Selenium Webdriver is managed automatically by 
[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager). 
Be sure that you have updated version of [Chrome Browser](https://www.google.com/chrome/).
### Requirements management 

The convention for managing Python dependencies is as follows:
- install pip-tools: 
```python -m pip install pip-tools```
- add names of the dependencies into requirements.in [more information](https://github.com/jazzband/pip-tools)
- call ```pip-compile``` to create requirements.txt
- commit both files to the repository.

### Users

Personal e-mail is needed to run the scripts.
Default account is: test.new.york.times@gmail.com.
Password should be added to the environmental variable.

How to add a password to the environmental variable?

Bash
```
nano .bash_profile
```
ZSH
```
nano .zshrc
```

Variables are case sensitive and should be added in separate line each.
Assign to a variable using an equals sign = with no blanks around it.
Use quotes when your variable consists of special characters or blanks.

Example:
```
NYT_PASS='yourpass&*'
```

You can also use your own NYT account - just replace the email and password in the relevant places inside the scripts.
New users' emails and passwords are generated automatically.

### How to run the tests?

Run test in the main project folder. Just call "pytest".

```
pytest
```

Test plan file: test_run.py

All available tests:
- test_try_to_register_with_too_short_password 
- test_successful_login_to_nyt


One chose test:

```
pytest -k [name of the chosen test]
pytest -k test_successful_login_to_nyt
```


### Parallel running

For running tests in parallel use [PyTest XDist](https://pypi.org/project/pytest-xdist/)
To send tests to multiple CPUs, use the -n option.

Example:

```
pytest -n 2
```