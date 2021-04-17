from helpers import *
from test_data import *
from locators import *


def register_page_url(browser):
    """
    Opens login page
    """
    browser.get(register_url)


def click_create_btn(browser):
    """
    Clicks on Create Account button
    """
    do_click(browser, REGISTER_BTN)


def enter_generated_email(browser):
    """
    Enters generated email to the email input
    """
    do_send_keys(browser, EMAIL_INPUT_REGISTER, random_email_generator())


def enter_generated_short_password(browser):
    """
    Enters generated too short password to the password input
    """
    do_send_keys(browser, PASSWORD_INPUT, random_password_generator(5))


def verify_error_msg(browser):
    """
    Verifies if error message when provided password is too long/short
    """
    is_visible(browser, PASSWORD_ERROR_MSG)
    error_msg = get_element_text(browser, PASSWORD_ERROR_MSG)
    assert error_msg == invalid_password_error
