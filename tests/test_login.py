from pytest_bdd import when, then
from pages.login_page import *


@when('I go to NYT login page')
def go_to_NYT_login_pages(browser):
    login_page_url(browser)


@when('I provide my registered email')
def enter_registered_mail(browser):
    enter_email(browser)


@when('I provide my registered password')
def enter_registered_password(browser):
    enter_password(browser)


@when('I click on login button')
def click_login_button(browser):
    click_login_btn(browser)


@then('I verify account settings dropdown')
def verify_logged_in(browser):
    verify_account_settings(browser)
