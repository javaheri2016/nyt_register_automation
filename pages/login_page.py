from locators import *
from helpers import *
from test_data import *


def login_page_url(browser):
    """
    Opens login page
    """
    browser.get(login_url)


def click_login_btn(browser):
    """
    Clicks on login button
    """
    do_click(browser, LOGIN_BTN)


def click_login_email(browser):
    """
    Clicks on login button
    """
    do_click(browser, PASSWORD_INPUT)


def enter_email(browser):
    """
    Enters existing email to the email input
    """
    do_send_keys(browser, EMAIL_INPUT_LOGIN, existing_email)


def enter_password(browser):
    """
    Enters existing password to the password input
    """
    do_send_keys(browser, PASSWORD_INPUT, password)


def verify_account_settings(browser):
    """
    Verifies if account dropdown is visible after log in
    """
    assert is_visible(browser, ACCOUNT_LOGGED_IN, 25) is True
