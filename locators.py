from selenium.webdriver.common.by import By

EMAIL_INPUT_LOGIN = (By.XPATH, '//INPUT[@id="username"]')
EMAIL_INPUT_REGISTER = (By.XPATH, '//INPUT[@id="email"]')
PASSWORD_INPUT = (By.XPATH, '//INPUT[@id="password"]')
LOGIN_BTN = (By.XPATH, '//BUTTON[@data-testid="login-button"]')
REGISTER_BTN = (By.XPATH, '//BUTTON[@data-testid="register-button"]')
ACCOUNT_LOGGED_IN = (By.XPATH, '//BUTTON[@data-testid="user-settings-button"]')
PASSWORD_ERROR_MSG = (By.XPATH, '//SPAN[@id="err-id-password"]')
